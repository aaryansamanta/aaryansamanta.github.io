#!/usr/bin/env python3
"""Offline integrity check for the site. Standard library only.

    python3 tools/check.py

Fails (exit 1) if index.html or 404.html has:
  - duplicate ids, or #anchors / local files that don't exist
  - images without alt text, or non-https external links
  - a .row without exactly one valid status label
  - invalid JSON-LD
  - a phone number, an unexpected email address, or placeholder text
    (this is what keeps private details and unfinished claims off the page)
  - a "Updated <Month Year>" footer that disagrees with sitemap.xml
and warns if index.html grows past the size budget.

It does not check that external links are alive (many sites block bots).
Click the public ones after each edit.
"""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ["index.html", "404.html"]
STATUS = {"status--done", "status--accepted", "status--open"}
ALLOWED_EMAILS = {"aaryan.samanta@gmail.com"}
PLACEHOLDERS = [r"\[N\]", r"\[[A-Za-z /]*\]", r"\bTODO\b", r"\bFIXME\b", r"lorem ipsum", r"\bTBD\b"]
PHONE = re.compile(r"(?<!\d)(?:\+?1[ .-]?)?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}(?!\d)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SIZE_BUDGET = 120_000  # bytes for index.html

errors, warnings = [], []


def err(page, msg):
    errors.append(f"{page}: {msg}")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.hrefs, self.srcs, self.imgs = [], [], [], []
        self.rows, self._row_depth, self._stack = [], [], []
        self.jsonld, self._in_ld = [], False
        self.text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and "href" in a:
            self.hrefs.append(a["href"])
        if tag in ("script", "link", "img", "source") and (a.get("src") or a.get("href")):
            ref = a.get("src") or a.get("href")
            if tag != "link" or "stylesheet" in (a.get("rel") or "") or "icon" in (a.get("rel") or "") or a.get("as"):
                self.srcs.append(ref)
        if tag == "img":
            self.imgs.append(a)
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
            self.jsonld.append("")
        if tag == "meta" and a.get("content", "").startswith("http"):
            self.srcs.append(a["content"])
        # row bookkeeping
        self._stack.append((tag, cls))
        if tag == "article" and "row" in cls:
            self.rows.append([])
            self._row_depth.append(len(self._stack))
        if self.rows and self._row_depth and any(c.startswith("status") and c != "status" for c in cls):
            self.rows[-1].extend(c for c in cls if c.startswith("status--"))

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_ld = False
        while self._stack:
            t, _ = self._stack.pop()
            if self._row_depth and len(self._stack) + 1 == self._row_depth[-1] and t == "article":
                self._row_depth.pop()
            if t == tag:
                break

    def handle_data(self, data):
        if self._in_ld:
            self.jsonld[-1] += data
        else:
            self.text.append(data)


def check_page(name):
    path = os.path.join(ROOT, name)
    raw = open(path, encoding="utf-8").read()
    p = Page()
    p.feed(raw)

    # ids
    seen = set()
    for i in p.ids:
        if i in seen:
            err(name, f"duplicate id '{i}'")
        seen.add(i)

    # links
    ids = set(p.ids)
    for h in p.hrefs:
        if h.startswith("#"):
            if h[1:] and h[1:] not in ids:
                err(name, f"anchor {h} has no matching id")
        elif h.startswith(("mailto:", "tel:")):
            if h.startswith("tel:"):
                err(name, "tel: links are not allowed (keep phone numbers off the site)")
        elif urlparse(h).scheme in ("http", "https"):
            if urlparse(h).scheme != "https":
                err(name, f"non-https link {h}")
        elif urlparse(h).scheme:
            err(name, f"unexpected scheme in {h}")
        else:
            target = h.split("#")[0].split("?")[0]
            if target and not os.path.exists(os.path.join(ROOT, target.lstrip("/"))):
                err(name, f"local link {h} does not exist")
    for s in p.srcs:
        if urlparse(s).scheme in ("http", "https"):
            if urlparse(s).netloc != "aaryansamanta.github.io":
                err(name, f"third-party request {s} (this site loads nothing from other hosts)")
            else:
                local = urlparse(s).path.lstrip("/")
                if local and not os.path.exists(os.path.join(ROOT, local)):
                    err(name, f"asset {s} does not exist")
        elif s and not s.startswith("data:"):
            if not os.path.exists(os.path.join(ROOT, s.split("?")[0].lstrip("/"))):
                err(name, f"asset {s} does not exist")

    # images
    for im in p.imgs:
        if "alt" not in im:
            err(name, f"<img src={im.get('src')}> has no alt attribute")

    # status labels
    if name == "index.html":
        for n, labels in enumerate(p.rows, 1):
            if len(labels) != 1 or labels[0] not in STATUS:
                err(name, f"row #{n} needs exactly one of {sorted(STATUS)}, found {labels}")

    # json-ld
    for block in p.jsonld:
        try:
            json.loads(block)
        except ValueError as e:
            err(name, f"JSON-LD does not parse: {e}")

    # privacy and placeholders (visible text plus attributes plus JSON-LD)
    visible = " ".join(p.text) + " " + " ".join(p.hrefs) + " " + " ".join(p.jsonld)
    if PHONE.search(visible):
        err(name, "looks like a phone number; remove it")
    for e in set(EMAIL.findall(visible)):
        if e.lower() not in ALLOWED_EMAILS and not e.lower().endswith(("@2x.png",)):
            err(name, f"unexpected email address {e}")
    for pat in PLACEHOLDERS:
        m = re.search(pat, " ".join(p.text), re.I)
        if m:
            err(name, f"placeholder text found: {m.group(0)!r}")
            break

    if name == "index.html":
        size = len(raw.encode("utf-8"))
        if size > SIZE_BUDGET:
            warnings.append(f"index.html is {size:,} bytes (budget {SIZE_BUDGET:,})")
        # footer date vs sitemap
        m = re.search(r'<time datetime="(\d{4})-(\d{2})-(\d{2})">([A-Za-z]+) (\d{4})</time>', raw)
        if not m:
            err(name, "footer <time datetime> not found")
        else:
            y, mo, d, month_name, y2 = m.groups()
            months = ["January", "February", "March", "April", "May", "June", "July", "August",
                      "September", "October", "November", "December"]
            if months[int(mo) - 1] != month_name or y != y2:
                err(name, f"footer says {month_name} {y2} but datetime is {y}-{mo}-{d}")
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            root = ET.parse(os.path.join(ROOT, "sitemap.xml")).getroot()
            home = [u for u in root.findall("s:url", ns) if u.findtext("s:loc", namespaces=ns) == "https://aaryansamanta.github.io/"]
            if not home:
                err("sitemap.xml", "homepage entry missing")
            elif home[0].findtext("s:lastmod", namespaces=ns) != f"{y}-{mo}-{d}":
                err("sitemap.xml", f"homepage lastmod should be {y}-{mo}-{d} to match the footer")
            if f'"dateModified": "{y}-{mo}-{d}"' not in raw:
                err(name, f"JSON-LD dateModified should be {y}-{mo}-{d}")


def main():
    for pg in PAGES:
        check_page(pg)
    for f in ("robots.txt", "sitemap.xml", "aaryan-samanta-resume.pdf", "assets/img/og.png", "assets/img/favicon.svg"):
        if not os.path.exists(os.path.join(ROOT, f)):
            err(f, "missing")
    for w in warnings:
        print("warning:", w)
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print("  -", e)
        return 1
    print("ok: no problems found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
