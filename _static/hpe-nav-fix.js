/* sphinx-immaterial leaves page titles' |tier| raw-HTML suffix as literal
   escaped text in nav labels (it renders as a real pill in the body H1, but
   the nav re-derives its label from the plain title string). Replace that
   escaped tag soup with compact real badges (ADV/ENT/ESS) instead of just
   stripping it, so editions stay visible in the nav without blowing out its
   width. Body badges are untouched — this only rewrites the nav label. */
(function () {
  var MARK = '<span class="tier-badge';
  var ABBR = { advanced: 'ADV', enterprise: 'ENT', essentials: 'ESS' };
  var TIER_RE = /tier-(advanced|enterprise|essentials)"[^]*?>[A-Z]+</g;
  function fix(scope) {
    (scope || document).querySelectorAll('.md-nav__link .md-ellipsis').forEach(function (el) {
      var t = el.textContent;
      var i = t.indexOf(MARK);
      if (i === -1) return;
      var tiers = [];
      var m;
      TIER_RE.lastIndex = 0;
      while ((m = TIER_RE.exec(t))) tiers.push(m[1]);
      el.textContent = t.slice(0, i).replace(/\s+$/, '');
      if (!tiers.length) return;
      var wrap = document.createElement('span');
      wrap.className = 'md-nav__tier-badges';
      tiers.forEach(function (tier) {
        var badge = document.createElement('span');
        badge.className = 'tier-badge tier-badge--nav tier-' + tier;
        badge.textContent = ABBR[tier];
        wrap.appendChild(badge);
      });
      el.parentNode.insertBefore(wrap, el.nextSibling);
    });
  }
  if (document.readyState !== 'loading') fix();
  else document.addEventListener('DOMContentLoaded', function () { fix(); });
})();

/* Populate the footer copyright year so it stays current regardless of when the
   docs were last built. */
(function () {
  function setYear() {
    var el = document.getElementById('year');
    if (el) el.textContent = new Date().getFullYear();
  }
  if (document.readyState !== 'loading') setYear();
  else document.addEventListener('DOMContentLoaded', setYear);
})();

/* Chromium bug (crbug.com/1020072): a focused <input> nested inside a
   `position: sticky` ancestor (our .md-header) makes the browser auto-scroll
   the page toward the caret on every keystroke, even though nothing is
   obscured. Only the header search box is affected. Snapshot the scroll
   position on keydown and re-pin it on keyup/input, once synchronously (the
   browser's spurious scroll has already landed by then) and once more on the
   next frame as a safety net for slower devices. */
(function () {
  function guard() {
    var input = document.querySelector('.app-header__search');
    if (!input) return;
    var savedY = null;
    input.addEventListener('keydown', function () { savedY = window.scrollY; });
    function restore() {
      if (savedY === null) return;
      var y = savedY;
      if (window.scrollY !== y) window.scrollTo(window.scrollX, y);
      requestAnimationFrame(function () {
        if (window.scrollY !== y) window.scrollTo(window.scrollX, y);
      });
    }
    input.addEventListener('keyup', restore);
    input.addEventListener('input', restore);
  }
  if (document.readyState !== 'loading') guard();
  else document.addEventListener('DOMContentLoaded', guard);
})();

/* Version + locale selectors (POC). Docs deploy RTD-style at
   /<lang>/<version>/<page>. One build is cloned across the version dirs, so the
   current version isn't known at build time — both the current lang and version
   are read from the URL at runtime and used to build every option link. The
   page path is baked server-side as data-page. Menus float (position:fixed) so
   neither the sidebar's scroll container nor the header can clip them. */
(function () {
  function wire() {
    var seg = window.location.pathname.split('/');
    var lang = seg[1] || 'en';
    var version = seg[2] || '';

    var configs = [
      {
        box: document.querySelector('.hpe-version'),
        attr: 'data-version',
        current: version,
        valueSel: '[data-hpe-version-value]',
        align: 'left',
        href: function (key, page) { return '/' + lang + '/' + key + '/' + page + '.html'; },
      },
      {
        box: document.querySelector('.hpe-locale'),
        attr: 'data-lang',
        current: lang,
        valueSel: '[data-hpe-locale-value]',
        align: 'right',
        href: function (key, page) { return '/' + key + '/' + version + '/' + page + '.html'; },
      },
    ];

    configs.forEach(function (c) {
      var box = c.box;
      if (!box) return;
      var toggle = box.querySelector('summary');
      var menu = box.querySelector('[role="menu"]');
      var valueEl = box.querySelector(c.valueSel);
      var page = box.getAttribute('data-page') || 'index';
      var opts = box.querySelectorAll('[role="menuitem"]');

      Array.prototype.forEach.call(opts, function (o) {
        var key = o.getAttribute(c.attr);
        o.setAttribute('href', c.href(key, page));
        if (key === c.current) {
          if (valueEl) valueEl.textContent = o.textContent.trim();
          o.setAttribute('aria-current', 'true');
        } else {
          o.removeAttribute('aria-current');
        }
      });

      // A fixed menu doesn't follow its toggle, so anchor it on open and keep it
      // there while the sidebar/page scrolls or the window resizes.
      function place() {
        if (!box.open || !toggle || !menu) return;
        var r = toggle.getBoundingClientRect();
        menu.style.top = r.bottom + 4 + 'px';
        if (c.align === 'right') {
          menu.style.left = 'auto';
          menu.style.right = window.innerWidth - r.right + 'px';
        } else {
          menu.style.right = 'auto';
          menu.style.left = r.left + 'px';
          menu.style.minWidth = r.width + 'px';
        }
      }
      box.addEventListener('toggle', place);
      window.addEventListener('resize', place);
      window.addEventListener('scroll', place, true);
      box.addEventListener('keydown', function (e) { if (e.key === 'Escape') box.open = false; });
      // Don't let a click inside toggle the mobile drawer (label for=__drawer).
      box.addEventListener('click', function (e) { e.stopPropagation(); });
      document.addEventListener('click', function (e) {
        if (box.open && !box.contains(e.target)) box.open = false;
      });
    });
  }
  if (document.readyState !== 'loading') wire();
  else document.addEventListener('DOMContentLoaded', wire);
})();

/* Fix the "On this page" (secondary TOC) scroll-spy off-by-one. immaterial marks
   a heading active only once it reaches the theme's header-height line, but
   hpe-header.css lands anchor jumps at `scroll-padding-top` (84px = the 68px
   header + breathing room), which sits BELOW that line — so the theme keeps the
   PREVIOUS item highlighted. Re-derive the active item ourselves against
   scroll-padding-top using live heading positions, and re-assert it whenever the
   theme re-marks a different one. */
(function () {
  var ACTIVE = 'md-nav__link--active';
  var nav, links = [], observer;

  function activeLine() {
    var v = parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop);
    return (isNaN(v) ? 84 : v) + 4;   // +epsilon so a click-landed heading counts
  }
  function targetOf(a) {
    var h = a.getAttribute('href') || '';
    if (h.charAt(0) !== '#') return null;
    try { return document.getElementById(decodeURIComponent(h.slice(1))); }
    catch (e) { return null; }
  }
  function collect() {
    nav = document.querySelector('.md-sidebar--secondary .md-nav--secondary');
    links = nav ? [].slice.call(nav.querySelectorAll('a.md-nav__link[href^="#"]')) : [];
    return links.length > 0;
  }
  function computeIndex() {
    var line = activeLine(), idx = -1, t;
    for (var i = 0; i < links.length; i++) {
      t = targetOf(links[i]);
      if (t && t.getBoundingClientRect().top <= line) idx = i;
    }
    return (idx === -1 && links.length) ? 0 : idx;   // above all headings -> first
  }
  function enforce() {
    if (!links.length) return;
    var idx = computeIndex(), dirty = false, i;
    for (i = 0; i < links.length; i++) {
      if (links[i].classList.contains(ACTIVE) !== (i === idx)) { dirty = true; break; }
    }
    if (!dirty) return;
    if (observer) observer.disconnect();   // don't observe our own writes
    for (i = 0; i < links.length; i++) links[i].classList.toggle(ACTIVE, i === idx);
    if (observer) observer.observe(nav, { subtree: true, attributes: true, attributeFilter: ['class'] });
  }

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { ticking = false; enforce(); });
  }
  function init() {
    if (!collect()) return;
    observer = new MutationObserver(enforce);   // re-correct when the theme re-marks
    observer.observe(nav, { subtree: true, attributes: true, attributeFilter: ['class'] });
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    window.addEventListener('hashchange', onScroll);
    enforce();
  }
  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
