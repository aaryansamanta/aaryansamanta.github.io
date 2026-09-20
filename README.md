# aaryansamanta.github.io

Personal site of **Aaryan Samanta**: research, competitions, and the organizations I run.
Live at **https://aaryansamanta.github.io/**

One static page. No build step, no framework, no trackers, no third-party requests (fonts are self-hosted).
It works without JavaScript; the script only adds a nav highlight, an interactive hero figure, and copy buttons for BibTeX.

## What is on the page

| Section | What it holds |
|---|---|
| Hero | Selected results, and a figure you can drag across to read displacement, velocity and acceleration (the curves behind my Stanford project) |
| Research | Papers with a copy-BibTeX button, mentored research, projects |
| Competitions | Results with the field size where I know it |
| Building and leading | AI Ethos, NextGenAI, CogArc, teams and service |
| Outside the classroom | Track, band, languages |
| Academics | School, scores, recognition, coursework capstones |
| Sources | Where each claim can be checked, or that records are available on request |

## Repository layout

```
index.html                     the whole site: semantic HTML, JSON-LD for search engines
404.html                       custom not-found page
aaryan-samanta-resume.pdf      linked from the hero and contact section (keep this filename)
assets/css/style.css           design tokens, layout, components, dark mode, print styles
assets/js/main.js              optional enhancements (see above)
assets/fonts/                  Newsreader + Hanken Grotesk (variable, latin subset, SIL OFL)
assets/img/                    favicon, Apple touch icon, 1200x630 social preview
robots.txt, sitemap.xml        search engine hints
tools/check.py                 offline checks: links, ids, status labels, privacy, placeholders, dates
tools/build_resume.py          regenerates the resume PDF in the site's own fonts
docs/CONTENT-GUIDE.md          how to add or change an entry, and the rules I follow
.github/workflows/check.yml    runs tools/check.py on every push and pull request
```

## Preview locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
python3 tools/check.py        # run before every commit
```

## Updating content

Everything lives in `index.html`. Each entry is one `<article class="row">` (Research, Building, Outside the classroom) or one `<li>` (Competitions). Copy a nearby entry and edit it. The full guide, including the status labels and the rules for promoting an item from "in progress" to "done", is in [`docs/CONTENT-GUIDE.md`](docs/CONTENT-GUIDE.md).

After any edit that changes content:

1. Update the footer `<time>` and the JSON-LD `dateModified` in `index.html`.
2. Update `lastmod` in `sitemap.xml` (`tools/check.py` fails if these disagree).
3. If the change belongs on the resume, edit `tools/build_resume.py` and run it.
4. Run `python3 tools/check.py`, then click any external link you added or changed.

## Rebuilding the resume PDF

```bash
pip install -r tools/requirements.txt
python3 tools/build_resume.py
```

This overwrites `aaryan-samanta-resume.pdf` in place, so links to it keep working. The PDF deliberately has no phone number and no reference contact details.

## Deploying

This repository is a GitHub Pages **user site**, so it must be named exactly `aaryansamanta.github.io`.
Settings, Pages, Source: **Deploy from a branch**, branch `main`, folder `/ (root)`. The site is live within a minute of each push.
Do not add a `CNAME` file unless you intend to move the site to a custom domain: it would redirect this address.

## License

Code (HTML structure, CSS, JavaScript, tools): MIT, see `LICENSE`.
Written content, resume and personal data: all rights reserved.
Fonts: SIL Open Font License, see `assets/fonts/`.
