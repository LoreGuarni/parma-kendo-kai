

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


