// Progressive enhancement only. The page is complete without this file.
//   1. Highlights the current section in the header nav.
//   2. Lets visitors drag across the hero curves and read their values.
//   3. Adds a "Copy BibTeX" button to each citation.
(function () {
  "use strict";

  /* ---------- 1. Current section in the nav ---------- */
  (function navHighlight() {
    if (!("IntersectionObserver" in window)) return;
    var links = document.querySelectorAll(".nav a[href^='#']");
    var map = {};
    links.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var sections = Object.keys(map)
      .map(function (id) { return document.getElementById(id); })
      .filter(Boolean);
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) { a.removeAttribute("aria-current"); });
        map[e.target.id].setAttribute("aria-current", "true");
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    sections.forEach(function (s) { io.observe(s); });
  })();

  /* ---------- 2. Curve scrubber ---------- */
  (function scrubber() {
    var svg = document.querySelector(".fig-svg");
    var wrap = document.querySelector(".scrub-wrap");
    var input = document.getElementById("scrub");
    if (!svg || !wrap || !input) return;

    var cursor = svg.querySelector(".fig-cursor");
    var line = svg.querySelector(".cur-line");
    var dots = [".p0", ".p1", ".p2"].map(function (s) { return svg.querySelector(s); });
    var outs = wrap.querySelectorAll("[data-ro]");
    var names = ["displacement", "velocity", "acceleration"];

    // Read the three traces straight from the SVG paths so the figure stays the single source of truth.
    var traces = [".t0", ".t1", ".t2"].map(function (sel) {
      var el = svg.querySelector(sel);
      if (!el) return null;
      var m = (el.getAttribute("d") || "").match(/-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?/g);
      if (!m || m.length < 2) return null;
      var pts = m.map(function (p) { var a = p.split(","); return [parseFloat(a[0]), parseFloat(a[1])]; });
      var base = pts[0][1], max = 0;
      pts.forEach(function (p) { max = Math.max(max, Math.abs(base - p[1])); });
      return { pts: pts, base: base, max: max || 1 };
    });
    if (traces.some(function (t) { return !t; }) || !cursor || !line || dots.some(function (d) { return !d; })) return;

    var n = traces[0].pts.length;

    function fmt(v) {
      var s = Math.abs(v).toFixed(2);
      return (v < -0.004 ? "\u2212" : "") + s;
    }

    function set(frac) {
      frac = Math.max(0, Math.min(1, frac));
      var i = Math.round(frac * (n - 1));
      var x = traces[0].pts[i][0];
      line.setAttribute("x1", x);
      line.setAttribute("x2", x);
      var spoken = [];
      traces.forEach(function (t, k) {
        var y = t.pts[i][1];
        var v = (t.base - y) / t.max;
        dots[k].setAttribute("cx", x);
        dots[k].setAttribute("cy", y);
        if (outs[k]) outs[k].textContent = fmt(v);
        spoken.push(names[k] + " " + fmt(v));
      });
      input.setAttribute("aria-valuetext", spoken.join(", "));
      cursor.classList.add("on");
    }

    wrap.hidden = false;
    input.addEventListener("input", function () { set(input.value / 1000); });

    // Mouse users can also hover over the figure itself. Touch keeps native vertical scrolling and uses the slider.
    svg.addEventListener("pointermove", function (e) {
      if (e.pointerType !== "mouse") return;
      var r = svg.getBoundingClientRect();
      var frac = (e.clientX - r.left) / r.width;
      input.value = Math.round(Math.max(0, Math.min(1, frac)) * 1000);
      set(frac);
    });
  })();

  /* ---------- 3. Copy BibTeX ---------- */
  (function copyButtons() {
    document.querySelectorAll("details.cite").forEach(function (box) {
      var pre = box.querySelector("pre");
      if (!pre) return;
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "copy";
      btn.textContent = "Copy BibTeX";
      var live = document.createElement("span");
      live.className = "sr-only";
      live.setAttribute("role", "status");
      box.appendChild(btn);
      box.appendChild(live);

      function done(ok) {
        btn.textContent = ok ? "Copied" : "Press Ctrl+C to copy";
        live.textContent = ok ? "BibTeX copied to clipboard" : "Copy failed. Select the text and copy it manually.";
        setTimeout(function () { btn.textContent = "Copy BibTeX"; live.textContent = ""; }, 2200);
      }

      btn.addEventListener("click", function () {
        var text = pre.textContent;
        if (navigator.clipboard && window.isSecureContext) {
          navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(false); });
          return;
        }
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        var ok = false;
        try { ok = document.execCommand("copy"); } catch (err) { ok = false; }
        document.body.removeChild(ta);
        done(ok);
      });
    });
  })();
})();
