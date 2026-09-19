/**
 * Parma Kendo Kai — Galleria: elenco foto da Google Drive
 * =========================================================
 * Come installarlo (5 minuti):
 * 1. Crea una cartella su Google Drive (es. "Galleria Sito PKK").
 *    Da quella cartella, tasto destro → Condividi → "Chiunque abbia
 *    il link" → ruolo "Visualizzatore". Fatto questo una volta,
 *    ogni foto che trascinate dentro sarà visibile dal sito.
 * 2. Apri il link della cartella nel browser: nell'URL, dopo
 *    /folders/ trovi l'ID della cartella (una stringa lunga di
 *    lettere e numeri). Copialo.
 * 3. Vai su script.google.com → Nuovo progetto.
 * 4. Cancella il contenuto di default e incolla tutto questo file.
 * 5. Sostituisci FOLDER_ID qui sotto con l'ID copiato al punto 2.
 * 6. Distribuisci → Nuova distribuzione → tipo "App web".
 *    - Esegui come: te stesso
 *    - Chi può accedere: chiunque
 *    Distribuisci, autorizza i permessi richiesti (l'accesso a
 *    Google Drive, per poter leggere la cartella).
 * 7. Copia l'URL dell'app web che ti viene dato.
 * 8. Incollalo in js/galleria.js, al posto di
 *    "INSERISCI_QUI_URL_APPS_SCRIPT_GALLERIA".
 *
 * Da quel momento, per aggiungere foto (o video) al sito basta
 * trascinarle nella cartella di Drive: appariranno da sole alla
 * prossima apertura della pagina Galleria, senza toccare il sito.
 */

var FOLDER_ID = "INSERISCI_QUI_ID_CARTELLA_DRIVE";

function doGet(e) {
  var folder = DriveApp.getFolderById(FOLDER_ID);
  var files = folder.getFiles();
  var result = [];

  while (files.hasNext()) {
    var f = files.next();
    var mime = f.getMimeType();
    var isImage = mime.indexOf("image/") === 0;
    var isVideo = mime.indexOf("video/") === 0;
    if (isImage || isVideo) {
      result.push({
        id: f.getId(),
        name: f.getName(),
        type: isVideo ? "video" : "image",
        date: f.getDateCreated().getTime()
      });
    }
  }

  // più recenti prima
  result.sort(function (a, b) { return b.date - a.date; });

  return ContentService
    .createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}
