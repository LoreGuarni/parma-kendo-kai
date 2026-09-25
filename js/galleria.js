document.addEventListener('DOMContentLoaded', function () {
  // ⚠️ Dopo aver distribuito lo script Google Apps Script (vedi
  // apps-script/Code-Galleria.gs e il README), incolla qui l'URL:
  var GALLERY_ENDPOINT = "INSERISCI_QUI_URL_APPS_SCRIPT_GALLERIA";

  var grid = document.getElementById('pkk-gallery-grid');
  var statusEl = document.getElementById('pkk-gallery-status');
  if (!grid) return;

  function driveImageUrl(id, size) {
    return 'https://drive.google.com/thumbnail?id=' + id + '&sz=w' + (size || 900);
  }

  function openLightbox(src, alt) {
    var lightbox = document.getElementById('lightbox');
    if (!lightbox) return;
    var img = lightbox.querySelector('.lightbox-img');
    img.src = src;
    img.alt = alt || '';
    lightbox.hidden = false;
    document.body.classList.add('lightbox-open');
    var closeBtn = lightbox.querySelector('.lightbox-close');
    if (closeBtn) closeBtn.focus();
  }

  // il resto della logica di chiusura (bottone, click fuori, Esc) è
  // già gestita da js/main.js sullo stesso elemento #lightbox

  if (GALLERY_ENDPOINT.indexOf('INSERISCI_QUI') === 0) {
    if (statusEl) statusEl.textContent = 'La galleria non è ancora collegata a Google Drive (manca l\u2019URL dello script).';
    return;
  }

  if (statusEl) statusEl.textContent = 'Caricamento foto...';

  fetch(GALLERY_ENDPOINT)
    .then(function (res) { return res.json(); })
    .then(function (files) {
      if (!files || files.length === 0) {
        if (statusEl) statusEl.textContent = 'Nessuna foto ancora nella galleria.';
        return;
      }
      if (statusEl) statusEl.textContent = '';

      grid.innerHTML = files.map(function (f) {
        var thumb = driveImageUrl(f.id, 500);
        var full = driveImageUrl(f.id, 1600);
        return (
          '<img src="' + thumb + '" data-full="' + full + '" alt="' + (f.name || 'Foto Parma Kendo Kai') + '" ' +
          'loading="lazy" class="pkk-gallery-img aspect-square object-cover w-full cursor-zoom-in">'
        );
      }).join('');

      grid.querySelectorAll('.pkk-gallery-img').forEach(function (img) {
        img.addEventListener('click', function () {
          openLightbox(img.dataset.full, img.alt);
        });
      });
    })
    .catch(function () {
      if (statusEl) statusEl.textContent = 'Non riesco a caricare le foto in questo momento. Riprova più tardi.';
    });
});
