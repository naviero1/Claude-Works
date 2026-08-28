/* ============================================================================
   THE INVENTORY DOCTRINE — behaviour
   Charts are hand-rolled SVG (no library): line/area with a crosshair+tooltip
   hover layer, plus a table view for every figure. Colours come from the CSS
   token set so both themes are one source of truth.
   ========================================================================= */
(function () {
  "use strict";

  /* ---------------------------------------------------------------- theme -- */
  var root = document.documentElement;
  var KEY = "inv-doctrine-theme";
  function stored(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  var saved = stored(KEY);
  if (saved === "dark" || saved === "light") root.setAttribute("data-theme", saved);

  function currentMode() {
    var t = root.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  var toggle = document.getElementById("theme-toggle");
  function labelToggle() {
    if (!toggle) return;
    var next = currentMode() === "dark" ? "light" : "dark";
    toggle.textContent = next === "dark" ? "Dark" : "Light";
    toggle.setAttribute("aria-label", "Switch to " + next + " theme");
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentMode() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      store(KEY, next);
      labelToggle();
      redrawAll();
    });
    labelToggle();
  }
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var onMq = function () { if (!root.getAttribute("data-theme")) { labelToggle(); redrawAll(); } };
    if (mq.addEventListener) mq.addEventListener("change", onMq);
    else if (mq.addListener) mq.addListener(onMq);
  }

  function tok(name) {
    return getComputedStyle(root).getPropertyValue(name).trim() || "#888";
  }

  /* ----------------------------------------------------------------- util -- */
  var NS = "http://www.w3.org/2000/svg";
  function el(tag, attrs, parent) {
    var n = document.createElementNS(NS, tag);
    for (var k in attrs) if (attrs[k] !== null && attrs[k] !== undefined) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  function clear(n) { while (n.firstChild) n.removeChild(n.firstChild); }
  function fmt(v, spec) {
    if (spec && spec.pre) v = spec.pre + v;
    return String(v);
  }

  /* ----------------------------------------------------- line/area figure -- */
  /* spec = {
       w, h, pad:{t,r,b,l},
       x:{min,max,ticks:[{v,label}]},
       y:{min,max,ticks:[num], fmt:fn},
       bands:[{from,to,token,label}],
       series:[{name, token, points:[[x,y]], fill:bool, dash:bool}],
       marks:[{x,y,label,token,anchor}]
     } */
  function drawLine(host, spec) {
    var W = 900, H = spec.h || 260;
    var P = spec.pad || { t: 14, r: 16, b: 26, l: 42 };
    var x0 = P.l, x1 = W - P.r, y0 = P.t, y1 = H - P.b;

    var svg = el("svg", {
      viewBox: "0 0 " + W + " " + H, role: "img",
      "aria-label": spec.alt || spec.title || "chart", preserveAspectRatio: "none"
    });
    svg.style.width = "100%";
    svg.style.height = "auto";
    svg.setAttribute("preserveAspectRatio", "xMidYMid meet");

    var sx = function (v) { return x0 + (v - spec.x.min) / (spec.x.max - spec.x.min) * (x1 - x0); };
    var sy = function (v) { return y1 - (v - spec.y.min) / (spec.y.max - spec.y.min) * (y1 - y0); };

    // era bands (behind everything)
    (spec.bands || []).forEach(function (b) {
      var bx = sx(b.from), bw = sx(b.to) - sx(b.from);
      el("rect", { x: bx, y: y0, width: bw, height: y1 - y0, fill: tok(b.token), opacity: b.opacity || 1 }, svg);
      if (b.label) {
        var t = el("text", {
          x: bx + 6, y: y0 + 12, class: "tick", "text-anchor": "start",
          fill: tok(b.textToken || "--faint")
        }, svg);
        t.textContent = b.label;
      }
    });

    // horizontal gridlines + y ticks
    spec.y.ticks.forEach(function (v) {
      var yy = Math.round(sy(v)) + .5;
      el("line", { x1: x0, x2: x1, y1: yy, y2: yy, class: "gridline" }, svg);
      var t = el("text", { x: x0 - 8, y: yy + 3.5, class: "tick", "text-anchor": "end" }, svg);
      t.textContent = spec.y.fmt ? spec.y.fmt(v) : v;
    });
    // baseline
    el("line", { x1: x0, x2: x1, y1: Math.round(sy(spec.y.min)) + .5, y2: Math.round(sy(spec.y.min)) + .5, class: "axis" }, svg);

    // horizontal reference lines
    (spec.refs || []).forEach(function (r) {
      var yy = Math.round(sy(r.y)) + .5;
      el("line", {
        x1: x0, x2: x1, y1: yy, y2: yy, stroke: tok(r.token || "--rule-strong"),
        "stroke-width": 1.4, "stroke-dasharray": "5 4"
      }, svg);
      if (r.label) {
        var t = el("text", {
          x: r.at !== undefined ? sx(r.at) : x0 + 6, y: yy + (r.below ? 13 : -6), class: "dlabel",
          "text-anchor": r.anchor || "start", fill: tok(r.token || "--muted")
        }, svg);
        t.textContent = r.label;
      }
    });

    // x ticks
    spec.x.ticks.forEach(function (t) {
      var xx = Math.round(sx(t.v)) + .5;
      var lb = el("text", { x: xx, y: H - P.b + 15, class: "tick", "text-anchor": "middle" }, svg);
      lb.textContent = t.label;
    });

    // series
    spec.series.forEach(function (s) {
      var col = tok(s.token);
      var pts = s.points;
      var d = pts.map(function (p, i) { return (i ? "L" : "M") + sx(p[0]).toFixed(2) + " " + sy(p[1]).toFixed(2); }).join(" ");
      if (s.fill) {
        var area = d + " L" + sx(pts[pts.length - 1][0]).toFixed(2) + " " + sy(spec.y.min).toFixed(2) +
          " L" + sx(pts[0][0]).toFixed(2) + " " + sy(spec.y.min).toFixed(2) + " Z";
        el("path", { d: area, fill: col, opacity: .12 }, svg);
      }
      el("path", {
        d: d, fill: "none", stroke: col, "stroke-width": 2,
        "stroke-linejoin": "round", "stroke-linecap": "round",
        "stroke-dasharray": s.dash ? "5 4" : null
      }, svg);
      // emphasised endpoint
      if (s.endpoint !== false) {
        var last = pts[pts.length - 1];
        el("circle", { cx: sx(last[0]), cy: sy(last[1]), r: 4, fill: col, stroke: tok("--panel"), "stroke-width": 2 }, svg);
      }
    });

    // annotated marks
    (spec.marks || []).forEach(function (m) {
      var col = tok(m.token || "--ink");
      el("circle", { cx: sx(m.x), cy: sy(m.y), r: 4.5, fill: col, stroke: tok("--panel"), "stroke-width": 2 }, svg);
      var anchor = m.anchor || "middle";
      var dx = anchor === "start" ? 9 : anchor === "end" ? -9 : 0;
      var dy = m.below ? 17 : -11;
      var lines = String(m.label).split("|");
      lines.forEach(function (ln, i) {
        var t = el("text", {
          x: sx(m.x) + dx, y: sy(m.y) + dy + i * 12, class: "dlabel",
          "text-anchor": anchor, fill: col
        }, svg);
        t.textContent = ln;
      });
    });

    clear(host);
    host.appendChild(svg);

    // ---- hover layer -------------------------------------------------------
    var tip = document.createElement("div");
    tip.className = "tip";
    host.appendChild(tip);
    var cross = el("line", { x1: 0, x2: 0, y1: y0, y2: y1, stroke: tok("--rule-strong"), "stroke-width": 1, opacity: 0 }, svg);
    var dots = spec.series.map(function (s) {
      return el("circle", { r: 5, fill: tok(s.token), stroke: tok("--panel"), "stroke-width": 2, opacity: 0 }, svg);
    });

    function nearest(pts, xv) {
      var best = pts[0], bd = Infinity;
      pts.forEach(function (p) { var d = Math.abs(p[0] - xv); if (d < bd) { bd = d; best = p; } });
      return best;
    }
    function move(ev) {
      var r = svg.getBoundingClientRect();
      var cx = ev.touches ? ev.touches[0].clientX : ev.clientX;
      var px = (cx - r.left) / r.width * W;
      if (px < x0 - 4 || px > x1 + 4) return out();
      var xv = spec.x.min + (px - x0) / (x1 - x0) * (spec.x.max - spec.x.min);
      var rows = [], anchorY = Infinity, anchorX = px;
      spec.series.forEach(function (s, i) {
        var p = nearest(s.points, xv);
        anchorX = sx(p[0]);
        dots[i].setAttribute("cx", sx(p[0]));
        dots[i].setAttribute("cy", sy(p[1]));
        dots[i].setAttribute("opacity", 1);
        anchorY = Math.min(anchorY, sy(p[1]));
        rows.push((spec.series.length > 1 ? s.name + " " : "") + "<b>" + (spec.tipFmt ? spec.tipFmt(p[1]) : p[1]) + "</b>");
        if (i === 0) rows.unshift(spec.xTipFmt ? spec.xTipFmt(p[0]) : String(p[0]));
      });
      cross.setAttribute("x1", anchorX); cross.setAttribute("x2", anchorX); cross.setAttribute("opacity", .55);
      tip.innerHTML = rows.join("<br>");
      // px, not %, so the tip stays put when the plot scrolls sideways on narrow screens
      var lx = anchorX / W * r.width, ly = anchorY / H * r.height;
      tip.style.left = Math.min(Math.max(lx, 62), r.width - 62) + "px";
      tip.style.top = Math.max(ly, 34) + "px";
      tip.classList.add("on");
    }
    function out() {
      cross.setAttribute("opacity", 0);
      dots.forEach(function (d) { d.setAttribute("opacity", 0); });
      tip.classList.remove("on");
    }
    svg.addEventListener("mousemove", move);
    svg.addEventListener("mouseleave", out);
    svg.addEventListener("touchmove", function (e) { move(e); }, { passive: true });
    svg.addEventListener("touchend", out);
  }

  /* ---------------------------------------------------------- chart specs -- */
  var SPECS = {};
  function register(id, factory) { SPECS[id] = factory; }
  function redrawAll() {
    Object.keys(SPECS).forEach(function (id) {
      var host = document.getElementById(id);
      if (host) drawLine(host, SPECS[id]());
    });
  }
  window.__registerChart = register;
  window.__redrawCharts = redrawAll;
  window.__drawLine = drawLine;

  /* ---------------------------------------------------------- kpi filters -- */
  var chips = Array.prototype.slice.call(document.querySelectorAll("[data-filter]"));
  var rows = Array.prototype.slice.call(document.querySelectorAll("[data-domain]"));
  var count = document.getElementById("kpi-count");
  function applyFilter(val) {
    var shown = 0;
    rows.forEach(function (r) {
      var hit = val === "all" || r.getAttribute("data-domain") === val;
      r.hidden = !hit;
      if (hit && r.classList.contains("lrow")) shown++;
    });
    chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c.getAttribute("data-filter") === val)); });
    if (count) count.textContent = shown + (shown === 1 ? " metric pair" : " metric pairs");
  }
  chips.forEach(function (c) {
    c.addEventListener("click", function () { applyFilter(c.getAttribute("data-filter")); });
  });
  if (chips.length) applyFilter("all");

  /* --------------------------------------------------- figure table views -- */
  Array.prototype.slice.call(document.querySelectorAll("[data-tableview]")).forEach(function (btn) {
    var target = document.getElementById(btn.getAttribute("data-tableview"));
    if (!target) return;
    btn.addEventListener("click", function () {
      var open = target.hidden;
      target.hidden = !open;
      btn.setAttribute("aria-expanded", String(open));
      btn.textContent = open ? "Hide data" : "Show data";
    });
  });

  /* ------------------------------------------------------------ nav state -- */
  var links = Array.prototype.slice.call(document.querySelectorAll(".tnav a"));
  var secs = links.map(function (a) { return document.querySelector(a.getAttribute("href")); }).filter(Boolean);
  if ("IntersectionObserver" in window && secs.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) {
          var on = a.getAttribute("href") === "#" + e.target.id;
          a.style.color = on ? "var(--ink)" : "";
          a.style.background = on ? "var(--panel-2)" : "";
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    secs.forEach(function (s) { io.observe(s); });
  }

  document.addEventListener("DOMContentLoaded", redrawAll);
  if (document.readyState !== "loading") redrawAll();
})();

/* ------------------------------------------------- safety-stock demonstrator */
(function () {
  "use strict";
  var slider = document.getElementById("sigmaL");
  if (!slider) return;
  var D = 500, sD = 100, L = 8, z = 1.65;
  var SS_MAX = z * Math.sqrt(L * sD * sD + D * D * 6 * 6);   // fixed scale at σ_L = 6
  var $ = function (id) { return document.getElementById(id); };

  function render() {
    var sL = parseFloat(slider.value);
    var oldSS = z * sD * Math.sqrt(L);
    var newSS = z * Math.sqrt(L * sD * sD + D * D * sL * sL);
    $("sigmaL-val").textContent = sL.toFixed(2) + " wk";
    $("ss-old").textContent = Math.round(oldSS);
    $("ss-old-wk").textContent = (oldSS / D).toFixed(2);
    $("ss-new").textContent = Math.round(newSS);
    $("ss-new-wk").textContent = (newSS / D).toFixed(2);
    $("bar-old").style.width = (oldSS / SS_MAX * 100).toFixed(1) + "%";
    $("bar-new").style.width = (newSS / SS_MAX * 100).toFixed(1) + "%";
    var m = newSS / oldSS;
    $("ss-mult").textContent = (m < 1.005 ? "exactly the same" : m.toFixed(1) + "×");
    $("ss-mult").nextSibling && null;
    var line = $("ss-mult").parentNode;
    line.firstChild.nodeValue = m < 1.005
      ? "With no lead-time variability the two formulas agree — the buffer is "
      : "The buffer the same part needs is ";
    line.lastChild.nodeValue = m < 1.005 ? "." : " larger.";
  }
  slider.addEventListener("input", render);
  render();
})();
