# Parma Kendo Kai — sito statico (redesign nero/arancione, Tailwind CSS)

Stessa struttura e stessi contenuti del sito originale, nuova pelle: sfondo
quasi nero, arancione come colore guida (i colori del dojo), rosso e giallo
come accenti. Un solo segno grafico ricorrente — il "fendente" diagonale —
usato tra hero e contenuto e nelle testate di pagina.

## Struttura

```
index.html                     ← Home, con hero a schermo intero che
                                  sfuma/si rimpicciolisce scendendo
corso-bambini.html
principi-del-kendo.html
modulistica.html
conan-cup.html
codice-condotta.html
contatti-info/
  dove-quando.html
  come-iniziare.html
  costi.html
  risorse.html
css/style.css                  ← layer custom sopra Tailwind (font, hero,
                                  fendente, dropdown, lightbox, ecc.)
js/main.js                     ← menu mobile, dropdown, fade dell'hero
                                  allo scroll, lightbox, header sticky
images/                        ← SEGNAPOSTO nero/arancione, da sostituire
images/hero-kendoka.svg        ← illustrazione originale (non una foto),
                                  usata nella hero della home
documenti/                     ← da riempire con i PDF, vedi sotto
build.py                       ← script sorgente: se vuoi cambiare un
                                  testo, modificalo qui e rilancia
                                  `python3 build.py`
make_placeholders.py           ← rigenera i segnaposto colore, se serve
```

## Stile: Tailwind via CDN

Ogni pagina carica `https://cdn.tailwindcss.com` con una configurazione
inline (colori `ink/panel/paper/dojo-orange/dojo-red/dojo-yellow`, font
`display` = Oswald, `body` = Inter, `jp` = Shippori Mincho). Funziona subito,
senza build step: perfetto per GitHub Pages. Se in futuro vuoi ottimizzare
le performance, si può compilare Tailwind in un file CSS statico — dimmelo
e te lo preparo.

## 1. Le tue foto (formato webp, già pronte)

Le immagini sono ancora segnaposto arancione/nero generati da
`make_placeholders.py`. Basta **sostituire i file dentro `images/` con le
tue foto vere, usando esattamente questi nomi** (nessuna modifica all'HTML
necessaria):

hero-dojo.webp · chi-siamo-1.webp … chi-siamo-4.webp ·
galleria-1.webp … galleria-6.webp · dove-1.webp · locandina.webp ·
hakama-gi.webp · shinai.webp · bokken.webp · bogu.webp ·
bambini-1.webp … bambini-3.webp · conan-hero.webp · conan-maglietta.webp ·
conan-2024-risultati.webp · conan-2023-gruppo.webp

La hero della home (`images/hero-kendoka.svg`) è un'illustrazione, non una
foto: se preferisci una foto vera di un kendoka in armatura al posto del
disegno, mandamela e la inserisco al posto della silhouette.

## 2. I tuoi PDF

Crea/riempi la cartella `documenti/` con questi file (usati in Modulistica
e CONAN CUP):

modulo-iscrizione-parma-kendo-kai.pdf · informativa-trattamento-dati-cik.pdf ·
coordinate-bancarie-pkk.pdf · centri-medici-convenzionati.pdf ·
manuale-manutenzione-attrezzatura-kendo.pdf · stats-tana-delle-tigri.pdf ·
stats-accademia-dei-lividi.pdf · stats-valle-dei-cuccioli.pdf

## 3. Form di contatto

Il modulo in "Come iniziare" è solo HTML: per farlo funzionare davvero
(ricevere email) collega l'attributo `action` del `<form>` a un servizio
gratuito come Formspree o Netlify Forms.

## 4. La Galleria (foto sempre aggiornabili)

La pagina `galleria.html` legge le foto da una cartella condivisa su
Google Drive, tramite `js/galleria.js`. Non serve toccare il sito per
aggiungere foto: basta trascinarle nella cartella di Drive, in
qualsiasi momento, da telefono o computer.

Per farla funzionare:

1. Crea una cartella su Google Drive, condividila come "chiunque
   abbia il link — visualizzatore".
2. Vai su script.google.com → Nuovo progetto, incolla il contenuto di
   `apps-script/Code-Galleria.gs` (istruzioni passo passo nei
   commenti in cima al file).
3. Cambia `FOLDER_ID` nello script con l'ID della cartella (si trova
   nell'URL della cartella su Drive).
4. Distribuisci come App web (chiunque può accedere), copia l'URL.
5. Incolla quell'URL in `js/galleria.js`, al posto di
   `"INSERISCI_QUI_URL_APPS_SCRIPT_GALLERIA"`.

Finché non è collegata, la pagina mostra solo un avviso al posto
delle foto.

## 5. Pubblicare su GitHub Pages

1. Crea un repository pubblico su GitHub.
2. Carica tutto il contenuto di questa cartella nella root del repository.
3. Settings → Pages → sorgente: branch `main`, cartella `/ (root)`.
4. Dopo qualche minuto il sito è online su `https://<utente>.github.io/<repo>/`.
