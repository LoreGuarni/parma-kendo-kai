document.addEventListener('DOMContentLoaded', function () {
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Menu mobile ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var mobileMenu = document.querySelector('.mobile-menu');
  var mobileSubToggle = document.querySelector('.mobile-submenu-toggle');
  var mobileSubmenu = document.querySelector('.mobile-submenu');

  function closeMobileMenu() {
    if (!mobileMenu || !toggle) return;
    mobileMenu.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.focus();
  }

  if (toggle && mobileMenu) {
    toggle.addEventListener('click', function () {
      var isOpen = mobileMenu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeMobileMenu);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMobileMenu();
    });
  }
  if (mobileSubToggle && mobileSubmenu) {
    mobileSubToggle.addEventListener('click', function () {
      var isOpen = mobileSubmenu.classList.toggle('open');
      mobileSubToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  /* ---------- Dropdown desktop (tocco/tastiera, oltre a hover via CSS) ---------- */
  document.querySelectorAll('.dropdown').forEach(function (dd) {
    var btn = dd.querySelector('.dropdown-trigger');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var isOpen = dd.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    document.addEventListener('click', function (e) {
      if (!dd.contains(e.target)) {
        dd.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  });

  /* ---------- Header sticky ---------- */
  var siteHeader = document.querySelector('.site-header');
  var toTopBtn = document.querySelector('.to-top');
  var ticking = false;

  /* ---------- Hero: svanisce e si restringe scendendo ---------- */
  var heroContent = document.querySelector('.hero-content');
  var heroFigure = document.querySelector('.hero-bg');
  var hero = document.querySelector('.hero');

  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (siteHeader) siteHeader.classList.toggle('is-stuck', y > 8);
    if (toTopBtn) toTopBtn.hidden = y < 480;

    if (hero && heroContent && !reduceMotion) {
      var heroH = hero.offsetHeight || 800;
      var progress = Math.min(y / (heroH * 0.75), 1);
      heroContent.style.opacity = String(1 - progress);
      heroContent.style.transform = 'translateY(' + (progress * 40) + 'px)';
      if (heroFigure) {
        heroFigure.style.opacity = String(1 - progress * 1.1);
        heroFigure.style.transform = 'translateY(' + (progress * 60) + 'px) scale(' + (1 - progress * 0.08) + ')';
      }
    }
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(onScroll);
      ticking = true;
    }
  }, { passive: true });
  onScroll();

  if (toTopBtn) {
    toTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  /* ---------- Lightbox per le foto - a11y improved ---------- */
  var lightbox = document.getElementById('lightbox');
  if (lightbox) {
    var lightboxImg = lightbox.querySelector('.lightbox-img');
    var lightboxClose = lightbox.querySelector('.lightbox-close');
    var lastFocused = null;

    function openLightbox(img) {
      lastFocused = document.activeElement;
      lightboxImg.src = img.currentSrc || img.src;
      lightboxImg.alt = img.alt || '';
      lightbox.hidden = false;
      lightbox.setAttribute('aria-modal', 'true');
      lightbox.setAttribute('role', 'dialog');
      document.body.classList.add('lightbox-open');
      lightboxClose.focus();
    }
    function closeLightbox() {
      lightbox.hidden = true;
      lightbox.removeAttribute('aria-modal');
      lightboxImg.src = '';
      document.body.classList.remove('lightbox-open');
      if (lastFocused) lastFocused.focus();
    }

    document.querySelectorAll('main figure img, main .gallery-grid img').forEach(function (img) {
      img.addEventListener('click', function () { openLightbox(img); });
    });
    lightboxClose.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', function (e) { if (e.target === lightbox) closeLightbox(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !lightbox.hidden) closeLightbox(); });
  }

  /* ---------- Mappa Google: caricata solo su consenso esplicito ---------- */
  var mapConsent = document.getElementById('pkk-map-consent');
  var mapBtn = document.getElementById('pkk-map-load-btn');
  if (mapConsent && mapBtn) {
    mapBtn.addEventListener('click', function () {
      var iframe = document.createElement('iframe');
      iframe.className = 'map-frame not-prose';
      iframe.loading = 'lazy';
      iframe.title = mapConsent.dataset.mapTitle || 'Mappa';
      iframe.src = mapConsent.dataset.mapSrc;
      iframe.setAttribute('allowfullscreen', '');
      iframe.referrerPolicy = 'no-referrer-when-downgrade';
      mapConsent.replaceWith(iframe);
    });
  }

  /* ---------- Banner cookie ---------- */
  var cookieBanner = document.getElementById('pkk-cookie-banner');
  if (cookieBanner) {
    var consentGiven = false;
    try { consentGiven = localStorage.getItem('pkk_cookie_consent') === '1'; } catch (e) {}
    if (!consentGiven) cookieBanner.hidden = false;
    var acceptBtn = document.getElementById('pkk-cookie-accept');
    if (acceptBtn) {
      acceptBtn.addEventListener('click', function () {
        cookieBanner.hidden = true;
        try { localStorage.setItem('pkk_cookie_consent', '1'); } catch (e) {}
      });
    }
  }
});
