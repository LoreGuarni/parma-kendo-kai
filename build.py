#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generatore statico — Parma Kendo Kai, redesign nero/arancione con Tailwind CSS."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

MAIN_NAV = [
    ("Home", "index.html"),
    ("Galleria", "galleria.html"),
    ("Corso Bambini", "corso-bambini.html"),
    ("Principi del Kendo", "principi-del-kendo.html"),
    ("Modulistica", "modulistica.html"),
    ("CONAN CUP", "conan-cup.html"),
    ("Codice di Condotta", "codice-condotta.html"),
]
INFO_NAV = [
    ("Dove & Quando", "contatti-info/dove-quando.html"),
    ("Come iniziare", "contatti-info/come-iniziare.html"),
    ("Costi & Attrezzatura", "contatti-info/costi.html"),
    ("Risorse", "contatti-info/risorse.html"),
]

TAILWIND_CONFIG = """
tailwind.config = {
  theme: {
    extend: {
      colors: {
        ink: '#0a0907', panel: '#171310', paper: '#ede6d8',
        dojo: { orange: '#ff7a1a', red: '#c81e1e', yellow: '#f2b705' }
      },
      fontFamily: {
        display: ['Oswald', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
        jp: ['Shippori Mincho', 'serif']
      }
    }
  }
}
"""

HEAD = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{prefix}images/tiger-logo-icon.webp">
<script src="https://cdn.tailwindcss.com"></script>
<script>{tw_config}</script>
<link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body class="bg-ink text-paper font-body antialiased">
<a class="skip-link" href="#content">Vai al contenuto principale</a>
"""

def render_header(prefix, current_href):
    main_links = []
    for label, href in MAIN_NAV:
        full = prefix + href
        current = ' aria-current="page"' if href == current_href else ''
        main_links.append(f'<a class="nav-link px-3 py-2 text-sm" href="{full}"{current}>{label}</a>')

    info_active = any(href == current_href for _, href in INFO_NAV)
    info_links = []
    for label, href in INFO_NAV:
        full = prefix + href
        current = ' aria-current="page"' if href == current_href else ''
        info_links.append(f'<a href="{full}"{current}>{label}</a>')

    dropdown = f"""
    <div class="dropdown">
      <button type="button" class="dropdown-trigger nav-link flex items-center gap-1.5 px-3 py-2 text-sm" aria-expanded="false" aria-haspopup="true"{' aria-current="page"' if info_active else ''}>
        Contatti &amp; Info
        <svg class="dropdown-caret w-3 h-3" viewBox="0 0 12 8" fill="none" aria-hidden="true"><path d="M1 1l5 5 5-5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="dropdown-panel">
        {''.join(info_links)}
      </div>
    </div>"""

    mobile_main = "\n      ".join(
        f'<a class="block px-5 py-3 font-display text-paper-dim hover:text-dojo-orange" href="{prefix + href}"{" aria-current=\"page\"" if href == current_href else ""}>{label}</a>'
        for label, href in MAIN_NAV
    )
    mobile_info = "\n        ".join(
        f'<a class="block px-5 py-2.5 text-sm text-paper-dim hover:text-dojo-orange" href="{prefix + href}"{" aria-current=\"page\"" if href == current_href else ""}>{label}</a>'
        for label, href in INFO_NAV
    )

    return f"""
<header class="site-header">
  <div class="max-w-6xl mx-auto px-5 md:px-8 flex items-center justify-between h-16">
    <a class="flex items-center gap-3" href="{prefix}index.html">
      <img src="{prefix}images/tiger-logo-icon.webp" alt="Stemma Parma Kendo Kai" class="h-10 w-10 rounded-full shrink-0 border border-dojo-orange/40">
      <span class="font-jp text-xl md:text-2xl text-paper leading-none">パルマ剣道会</span>
      <span class="font-display text-sm md:text-base tracking-wide text-dojo-orange hidden sm:inline">PARMA KENDO KAI</span>
    </a>
    <nav class="hidden lg:flex items-center" aria-label="Menu principale">
      {''.join(main_links)}
      {dropdown}
    </nav>
    <button type="button" class="nav-toggle lg:hidden text-paper font-display text-sm border border-dojo-orange/40 px-3 py-1.5" aria-expanded="false">
      MENU
    </button>
  </div>
  <div class="mobile-menu lg:hidden border-t border-white/10">
    <nav aria-label="Menu principale (mobile)" class="py-2">
      {mobile_main}
      <button type="button" class="mobile-submenu-toggle w-full flex items-center justify-between px-5 py-3 font-display text-paper-dim hover:text-dojo-orange" aria-expanded="false">
        <span>Contatti &amp; Info</span>
        <svg class="w-3 h-3" viewBox="0 0 12 8" fill="none" aria-hidden="true"><path d="M1 1l5 5 5-5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="mobile-submenu bg-panel/60">
        {mobile_info}
      </div>
    </nav>
  </div>
</header>
"""

FOOTER = """
<footer class="site-footer">
  <div class="max-w-6xl mx-auto px-5 md:px-8 py-14 grid gap-10 sm:grid-cols-3">
    <div>
      <p class="font-display text-lg text-paper mb-3">Parma Kendo Kai a.s.d.</p>
      <p class="text-paper-dim text-sm leading-relaxed">Via San Leonardo 191a<br>Parma (Aiki Center)</p>
    </div>
    <div>
      <p class="font-display text-sm text-dojo-orange mb-3">Contatti</p>
      <p class="text-paper-dim text-sm leading-relaxed">
        <a class="hover:text-dojo-orange" href="mailto:parmakendokai@libero.it">parmakendokai@libero.it</a><br>
        349 159 5885
      </p>
    </div>
    <div>
      <p class="font-display text-sm text-dojo-orange mb-3">Federazione</p>
      <p class="text-paper-dim text-sm leading-relaxed">
        Associata a <a class="hover:text-dojo-orange" href="https://confederazioneitalianakendo.it/" target="_blank" rel="noopener">C.I.K. Confederazione Italiana Kendo</a><br>
        ed all'ente di promozione sportiva CSEN.
      </p>
    </div>
  </div>
  <div class="max-w-6xl mx-auto px-5 md:px-8 pb-8 flex flex-wrap gap-x-6 gap-y-2 text-xs text-paper-dim/50 border-t border-white/10 pt-6">
    <a href="{prefix}privacy.html" class="hover:text-dojo-orange">Privacy</a>
    <a href="{prefix}cookie-policy.html" class="hover:text-dojo-orange">Cookie Policy</a>
  </div>
</footer>

<div class="pkk-cookie-banner" id="pkk-cookie-banner" hidden role="dialog" aria-live="polite" aria-label="Informativa cookie">
  <p>Questo sito usa risorse di terze parti (Google Fonts, Maps, Forms) che possono installare cookie tecnici. <a href="{prefix}cookie-policy.html">Scopri di pi&ugrave;</a>.</p>
  <button type="button" id="pkk-cookie-accept" class="hero-cta-primary font-display text-sm px-5 py-2.5">Ho capito</button>
</div>

<button type="button" class="to-top" aria-label="Torna a inizio pagina" hidden>&uarr;</button>

<div class="lightbox" id="lightbox" hidden>
  <button type="button" class="lightbox-close" aria-label="Chiudi immagine">&times;</button>
  <img class="lightbox-img" src="" alt="">
</div>

<script src="{prefix}js/main.js"></script>
{extra_scripts}
</body>
</html>
"""

def write_page(rel_path, title, description, content, hero="", current_href=None, extra_scripts=""):
    depth = rel_path.count("/")
    prefix = "../" * depth
    if current_href is None:
        current_href = rel_path
    html = (
        HEAD.format(title=title, description=description, prefix=prefix, tw_config=TAILWIND_CONFIG)
        + render_header(prefix, current_href)
        + hero
        + '<main id="content">' + content.format(prefix=prefix) + '</main>'
        + FOOTER.format(prefix=prefix, extra_scripts=extra_scripts.format(prefix=prefix) if extra_scripts else "")
    )
    out_path = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("scritto:", rel_path)


def page_banner(title, lede, kanji="剣道"):
    return f"""
<div class="page-banner">
  <span class="page-kanji font-jp" aria-hidden="true">{kanji}</span>
  <div class="max-w-6xl mx-auto px-5 md:px-8 py-16 md:py-20 relative">
    <h1 class="font-display text-4xl md:text-5xl text-paper mb-3">{title}</h1>
    <p class="text-paper-dim max-w-xl">{lede}</p>
  </div>
</div>
"""

CONTAINER_OPEN = '<div class="max-w-3xl mx-auto px-5 md:px-8 py-16 prose-pkk">'
CONTAINER_WIDE_OPEN = '<div class="max-w-6xl mx-auto px-5 md:px-8 py-16">'
CONTAINER_CLOSE = '</div>'

# ==================================================================
# HOME
# ==================================================================
hero_home = """
<div class="hero">
  <div class="hero-bg" aria-hidden="true">
    <img src="images/hero-dojo.webp" alt="">
    <img class="hero-tiger" src="images/tiger-logo.webp" alt="">
    <div class="hero-overlay"></div>
  </div>
  <div class="hero-content relative max-w-6xl mx-auto px-5 md:px-8 w-full">
    <p class="font-jp text-2xl text-dojo-orange mb-4">パルマ剣道会</p>
    <h1 class="font-display text-[13vw] sm:text-6xl md:text-7xl leading-[0.95] text-paper mb-6 max-w-3xl">
      PARMA<br><span class="text-dojo-orange">KENDO KAI</span>
    </h1>
    <p class="text-paper-dim text-lg max-w-md mb-10">Dal 2012, il dojo di Kendo della città di Parma. Per adulti e bambini, allenamento serio e gruppo affiatato.</p>
    <div class="flex flex-wrap gap-4">
      <a class="hero-cta-primary font-display px-7 py-3.5 text-sm tracking-wide" href="contatti-info/come-iniziare.html">Prova una lezione gratuita</a>
      <a class="hero-cta-ghost font-display px-7 py-3.5 text-sm tracking-wide" href="#chi-siamo">Scopri il dojo</a>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true"><span>SCORRI</span><span class="scroll-cue-line"></span></div>
</div>
<div class="slash-divider"></div>
"""

content_home = """
<div class="max-w-3xl mx-auto px-5 md:px-8 pt-16 prose-pkk" id="chi-siamo">
<h2 class="section-heading">Chi siamo</h2>

<p><strong>L'associazione:</strong> la Parma Kendo Kai &egrave; una realt&agrave; nata nel 2012 volta a promuovere la pratica del Kendo nella nostra citt&agrave;. I suoi componenti frequentano con assiduit&agrave; seminari con maestri Giapponesi e Koreani, inoltre partecipano a numerose competizioni sul territorio nazionale.</p>

<figure class="pkk-figure my-9">
  <img src="{prefix}images/chi-siamo-1.webp" alt="Praticanti in armatura durante un keiko">
</figure>

<p><strong>Il Kendo</strong>: &egrave; un'arte marziale Giapponese. Derivazione diretta delle tecniche di utilizzo della katana dai samurai nel periodo feudale, si traduce letteralmente con "la via della spada". Oggi si utilizza una spada di bamb&ugrave; (<em>shinai</em>) in luogo della katana e si indossa un'armatura protettiva (<em>bogu</em>) sulla quale si pu&ograve; colpire in punti prestabiliti.</p>

<figure class="pkk-figure my-9">
  <img src="{prefix}images/chi-siamo-2.webp" alt="Allenamento di gruppo alla Parma Kendo Kai">
</figure>

<p>La disciplina del Kendo si vive nel rapporto con gli altri, nella costante tensione al miglioramento di se stessi e della propria tecnica, attraverso il confronto con i compagni di pratica e gli avversari dentro e fuori dal dojo.</p>

<figure class="pkk-figure my-9">
  <img src="{prefix}images/chi-siamo-3.webp" alt="Momento di pratica in coppia">
</figure>

<p>Si pu&ograve; quindi affermare che la pratica non si limita ad allenare il fisico, ma lavora anche sulla persona e sullo sviluppo di una corretta attitudine nell'affrontare la vita di tutti i giorni.</p>

<figure class="pkk-figure my-9">
  <img src="{prefix}images/chi-siamo-4.webp" alt="Praticanti della Parma Kendo Kai in posa">
</figure>

<h2 class="section-heading">Perch&eacute; iniziare alla Parma Kendo Kai?</h2>
<p>Siamo un gruppo amichevole ed eterogeneo sia per interessi che per et&agrave;. Contiamo pi&ugrave; di una ventina di praticanti attivi e diverse cinture nere con pi&ugrave; di 20 anni di esperienza di Kendo in giro per l'Italia, l'Europa e il Giappone.</p>
</div>

<div class="max-w-6xl mx-auto px-5 md:px-8">
<div class="gallery-grid grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-1.5 mb-4">
  <img src="{prefix}images/galleria-1.webp" alt="Foto di gruppo, allenamento 1" class="aspect-[4/3] object-cover w-full">
  <img src="{prefix}images/galleria-2.webp" alt="Foto di gruppo, allenamento 2" class="aspect-[4/3] object-cover w-full">
  <img src="{prefix}images/galleria-3.webp" alt="Foto di gruppo, allenamento 3" class="aspect-[4/3] object-cover w-full">
  <img src="{prefix}images/galleria-4.webp" alt="Foto di gruppo, allenamento 4" class="aspect-[4/3] object-cover w-full">
  <img src="{prefix}images/galleria-5.webp" alt="Foto di gruppo, allenamento 5" class="aspect-[4/3] object-cover w-full">
  <img src="{prefix}images/galleria-6.webp" alt="Foto di gruppo, allenamento 6" class="aspect-[4/3] object-cover w-full">
</div>
</div>

<div class="max-w-3xl mx-auto px-5 md:px-8 pb-16 prose-pkk">
<h2 class="section-heading">Gli insegnanti</h2>
<div class="grid sm:grid-cols-2 gap-4 not-prose">
  {teachers}
</div>

<p class="mt-10">La societ&agrave; sportiva dilettantistica &egrave; associata alla <a href="https://confederazioneitalianakendo.it/" target="_blank" rel="noopener">C.I.K. Confederazione Italiana Kendo</a> e all'ente di promozione sportiva CSEN.</p>

<p class="text-sm text-paper-dim/70 mt-10">44.801485, 10.327904 &mdash; Parma</p>
</div>
"""

TEACHERS = [
    ("Francesco Paterlini", "Istruttore C.I.K.&ndash;UISP&ndash;CSEN", 5),
    ("Federico Ghirardini", "Allenatore", 4),
    ("Jacopo Bracciali", "Allenatore", 3),
    ("Alessia Martorana", "Allenatore", 3),
    ("Leonardo Rossi", "Allenatore", 3),
    ("Davide Biacca", "&nbsp;", 2),
]
DAN_MAX = 8  # il kendo va da I a VIII dan (Hachidan)
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII"}

def teacher_card(name, role, dan):
    ticks = "".join(f'<div class="dan-tick{" filled" if i < dan else ""}"></div>' for i in range(DAN_MAX))
    return f"""<div class="teacher-card">
    <div class="flex items-baseline justify-between gap-3">
      <span class="font-display text-paper">{name}</span>
      <span class="font-display text-dojo-yellow text-sm">{ROMAN[dan]}&deg; Dan</span>
    </div>
    <p class="text-xs text-paper-dim/70 mt-1">{role}</p>
    <div class="dan-bar">{ticks}</div>
  </div>"""

write_page("index.html",
    "Parma Kendo Kai パルマ剣道会 | Dojo di Kendo a Parma",
    "La Parma Kendo Kai è nata nel 2012 per promuovere la pratica del Kendo a Parma, per adulti e bambini.",
    content_home.replace("{teachers}", "\n  ".join(teacher_card(n, r, d) for n, r, d in TEACHERS)),
    hero=hero_home)

# ==================================================================
# CORSO BAMBINI
# ==================================================================
content_bambini = page_banner("Corso Bambini e Ragazzi", "Il corso per la stagione sportiva 2026&ndash;2027 inizier&agrave; mercoled&igrave; 30 settembre.", "子供") + CONTAINER_OPEN + """
<figure class="pkk-figure my-2 mb-10">
  <img src="{prefix}images/bambini-1.webp" alt="Bambini durante un allenamento di Kendo">
</figure>

<div class="info-panel mb-10 not-prose">
  <h3>Dove?</h3>
  <p class="text-paper-dim text-sm mb-0">Presso Aiki Center, in via San Leonardo 191a, 43122 Parma.</p>
  <h3>Quando?</h3>
  <p class="text-paper-dim text-sm mb-0">Mercoled&igrave; e venerd&igrave;, dalle 17:30 alle 18:30.</p>
  <h3>Insegnanti del corso</h3>
  <p class="text-paper-dim text-sm mb-0">Federico Ghirardini (IV&deg; Dan) e Davide Biacca (I&deg; Dan), coadiuvati da Francesco Paterlini (V&deg; Dan).</p>
</div>

<h2 class="section-heading">Quali sono i benefici della pratica del Kendo nei bambini?</h2>
<p>I bambini che praticano Kendo hanno l'opportunit&agrave; di acquisire una forte sicurezza in se stessi, sviluppare tenacia e concentrazione.</p>

<blockquote class="kquote">Il Kendo inizia con un rei (il saluto) e finisce con un rei</blockquote>

<p>Sono fondamentali le buone maniere verso i propri compagni e gli insegnanti, al fine di creare un gruppo dove sia piacevole apprendere e migliorare se stessi.</p>

<p>Bench&eacute; si possa iniziare in pantaloncini e maglietta, con l'avanzare dell'esperienza si indosseranno hakama e gi e si avr&agrave; una <em>shinai</em> (la spada di bamb&ugrave;) di cui prendersi cura, fino ad arrivare al bogu (armatura). La cura del vestiario e dell'attrezzatura sono parti fondamentali del processo educativo del giovane praticante: la gradualit&agrave; nell'introduzione di questi elementi fa s&igrave; che badare ai propri strumenti diventi pian piano un'abitudine.</p>

<p>Il Kendo &egrave; una disciplina di contatto, ma questo avviene in totale sicurezza grazie all'armatura che si indossa e all'addestramento impartito ai praticanti.</p>

<div class="gallery-grid grid grid-cols-2 gap-2 my-9 not-prose">
  <img src="{prefix}images/bambini-2.webp" alt="Allenamento bambini 1" class="aspect-[4/3] object-cover w-full">
  <img src="{prefix}images/bambini-3.webp" alt="Allenamento bambini 2" class="aspect-[4/3] object-cover w-full">
</div>

<h2 class="section-heading">Quanto costa praticare Kendo?</h2>
<p>Uno degli obiettivi della Parma Kendo Kai nella sua attivit&agrave; di insegnamento e diffusione del Kendo &egrave; quello di renderlo accessibile a tutti, a partire dalle quote annuali contenute e dalla possibilit&agrave; di utilizzare l'attrezzatura di propriet&agrave; dell'associazione. Un approfondimento sul tema &egrave; disponibile nella pagina <a href="{prefix}contatti-info/costi.html">Costi &amp; Attrezzatura</a>.</p>

<h2 class="section-heading">Per informazioni</h2>
<div class="info-panel not-prose">
  <p class="text-paper-dim text-sm mb-0">WhatsApp: 349 159 5885 &mdash; Francesco<br>
  Mail: <a href="mailto:parmakendokai@libero.it" class="text-dojo-orange">parmakendokai@libero.it</a></p>
</div>
""" + CONTAINER_CLOSE

write_page("corso-bambini.html",
    "Corso Bambini e Ragazzi | Parma Kendo Kai",
    "Corso di Kendo per bambini e ragazzi a Parma: orari, insegnanti e benefici della pratica.",
    content_bambini)

# ==================================================================
# PRINCIPI DEL KENDO
# ==================================================================
PRINCIPI = [
    ("Ningen-keisei", "&Egrave; la ricerca della perfezione di mente e di corpo come essere umano. Divenire un essere umano eccellente attraverso il Kend&ocirc; &egrave; la meta ultima del Kend&ocirc;."),
    ("Shugy&ocirc;", "&Egrave; l'addestramento nei principi dell'arte del maneggio della spada giapponese. Il processo di rigoroso addestramento e affinamento della mente e del corpo richiede la continuit&agrave; della pratica ed &egrave; legato al modo di vita e alla creazione di un nuovo s&eacute;."),
    ("Ri-h&ocirc;", "Sono i principi dell'arte del maneggio della spada giapponese: indicano il modo in cui sforzarsi di realizzare il corretto movimento d'attacco, armonicamente e con la corretta attitudine mentale, postura e pienezza di spirito."),
    ("Waza", "&Egrave; l'arte del maneggio della spada giapponese: un movimento d'attacco dotato di forma tipica in cui si manifesta una capacit&agrave; motoria acquisita attraverso un lungo e duro addestramento."),
    ("Keiko", "&Egrave; la pratica dell'arte del maneggio della spada giapponese. Non indica semplicemente la ripetizione, ma include l'importanza dell'attitudine nei confronti dell'arte praticata. Keiko inizia e finisce con Rei-h&ocirc; e comprende Kata-geiko e Keiko-h&ocirc;."),
    ("Kata-geiko", "&Egrave; la pratica della sola forma: l'insegnamento e l'apprendimento di Waza da parte di Uchidachi e Shidachi, per apprendere con il corpo i vari Waza e comprenderne il significato spirituale."),
    ("Keiko-h&ocirc;", "&Egrave; il metodo di apprendimento del modo di esecuzione di Waza, fondato sulla presenza di Motodachi. Include Kihon-geiko, Gokaku-geiko (Ji-geiko), Hikitate-geiko, Shiai-geiko e forme speciali come Kan-geiko e Gasshuku-geiko."),
    ("Shi-ai", "&Egrave; la competizione tra due contendenti per Y&ucirc;k&ocirc; Datotsu. Shin-pan &egrave; la decisione sull'esito dello Shi-ai secondo lo Shinpan-h&ocirc;."),
    ("Shin-sa", "&Egrave; l'attestazione del livello raggiunto nell'addestramento: l'esame che decide se promuovere o meno il candidato a un rango pi&ugrave; elevato (Dan-to-ky&ucirc;)."),
    ("Ippon", "&Egrave; l'esecuzione di Waza che raggiunge il proprio scopo: il colpo valido eseguito con Ki-ken-tai-itchi, quando spirito, maneggio dello Shinai e movimento del corpo si accordano con la corretta tempestivit&agrave;."),
    ("Y&ucirc;k&ocirc; Datotsu", "&Egrave; l'esecuzione di un colpo valido: Waza eseguito nella sua completezza, con pienezza di spirito, postura appropriata, corretto Ha-suji ed espressione di Zan-shin."),
]

def principio_item(i, name, text):
    return f"""<div class="border-t border-white/10 py-6 grid sm:grid-cols-[3rem_1fr] gap-3 sm:gap-6">
    <span class="font-display text-dojo-orange/70 text-2xl">{i:02d}</span>
    <div>
      <h3 class="font-display text-paper mb-2">{name}</h3>
      <p class="text-paper-dim text-sm mb-0">{text}</p>
    </div>
  </div>"""

content_principi = page_banner("I Principi del Kend&ocirc;", "Dai documenti ufficiali Zen Nippon Kendo Renmei (ZNKR) &mdash; All Japan Kendo Federation (AJKF).", "理法") + CONTAINER_OPEN + """
<p>Kend&ocirc; &egrave; un modo di vita qualificato dalla ricerca della perfezione come essere umano attraverso l'addestramento nei principi dell'arte del maneggio della spada giapponese.</p>

<div class="not-prose mt-10">
""" + "\n  ".join(principio_item(i, n, t) for i, (n, t) in enumerate(PRINCIPI, start=1)) + """
</div>

<p class="text-sm text-paper-dim/60 mt-12">(testo tratto dallo Statuto della Confederazione Italiana Kendo C.I.K.)</p>
""" + CONTAINER_CLOSE

write_page("principi-del-kendo.html",
    "Principi del Kendo | Parma Kendo Kai",
    "I principi del Kendô secondo i documenti ufficiali della Zen Nippon Kendo Renmei (ZNKR / AJKF).",
    content_principi)

# ==================================================================
# MODULISTICA
# ==================================================================
DOCS = [
    ("documenti/modulo-iscrizione-parma-kendo-kai.pdf", "Modulo iscrizione Parma Kendo Kai", False),
    ("documenti/informativa-trattamento-dati-cik.pdf", "Informativa trattamento dati personali (C.I.K.)", False),
    ("https://www.confederazioneitalianakendo.org/Italiano/Reg_pdf/CONSENSO%20e%20DICHIARAZIONE.pdf", "Modulo Privacy CIK", True),
    ("documenti/coordinate-bancarie-pkk.pdf", "Coordinate bancarie Parma Kendo Kai", False),
    ("documenti/centri-medici-convenzionati.pdf", "Centri medici convenzionati", False),
    ("documenti/manuale-manutenzione-attrezzatura-kendo.pdf", "Manuale per la manutenzione dell'attrezzatura di Kend&ocirc;", False),
    ("https://docs.google.com/forms/d/e/1FAIpQLSfnNHKdVhUGce8sMeX9uMnWULfXbj8wx0irQVN0fqEkM2_lhg/viewform?usp=sf_link", "Upload documenti &ndash; Certificato medico &amp; Modulo privacy", True),
]

def doc_card(href, label, external):
    attrs = ' target="_blank" rel="noopener"' if external else ''
    real_href = href if external else "{prefix}" + href
    return f"""<a class="doc-card" href="{real_href}"{attrs}>
    <svg class="w-5 h-5 text-dojo-orange shrink-0" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6z" stroke="currentColor" stroke-width="1.6"/><path d="M14 2v6h6" stroke="currentColor" stroke-width="1.6"/></svg>
    <span class="text-sm">{label}</span>
  </a>"""

content_modulistica = page_banner("Modulistica", "Documenti e moduli utili per gli associati.", "書類") + CONTAINER_OPEN + """
<div class="grid gap-3 not-prose">
""" + "\n  ".join(doc_card(h, l, e) for h, l, e in DOCS) + """
</div>
""" + CONTAINER_CLOSE

write_page("modulistica.html",
    "Modulistica | Parma Kendo Kai",
    "Moduli e documenti utili per gli associati della Parma Kendo Kai: iscrizione, privacy, coordinate bancarie.",
    content_modulistica)

# ==================================================================
# CONAN CUP
# ==================================================================
def ranking(items):
    lis = "".join(f'<li class="flex items-baseline gap-3 py-2 border-b border-white/10"><span class="font-display text-dojo-yellow w-6">{i+1}&deg;</span><span class="text-paper-dim text-sm">{t}</span></li>' for i, t in enumerate(items))
    return f'<ol class="not-prose list-none p-0 m-0">{lis}</ol>'

content_conan = page_banner("CONAN CUP", "La competizione interna della Parma Kendo Kai.", "大会") + CONTAINER_OPEN + """
<figure class="pkk-figure mb-10">
  <img src="{prefix}images/conan-hero.webp" alt="Immagine di gruppo Conan Cup">
</figure>

<h2 class="section-heading">Che cos'&egrave;?</h2>
<p>La Conan Cup &egrave; la competizione (individuali e squadre) interna della Parma Kendo Kai. Si tiene nel mese di dicembre.</p>

<h2 class="section-heading">Organizzazione</h2>
<p>Negli anni pari si svolge la gara a squadre, in quelli dispari quella individuale.</p>

<h3 class="font-display text-paper mt-8 mb-3">Categorie gara individuale</h3>
<div class="flex flex-wrap gap-2 not-prose mb-6">
  <span class="badge-cat">Valle dei Cuccioli</span>
  <span class="badge-cat">Accademia dei Lividi</span>
  <span class="badge-cat">Tana delle Tigri</span>
</div>
<p>Dai neofiti che hanno appena messo l'armatura (Valle dei Cuccioli), a chi &egrave; da poco nel mondo dello shiai (Accademia dei Lividi), fino ai pi&ugrave; esperti con anni di gare alle spalle (Tana delle Tigri).</p>

<h3 class="font-display text-paper mt-8 mb-3">Categorie gara a squadre</h3>
<div class="flex flex-wrap gap-2 not-prose mb-6">
  <span class="badge-cat">Blue Tornado con Schiaffoni</span>
  <span class="badge-cat">Brucomela con Abbracci</span>
</div>
<p>Esperti e praticanti di medio livello nella prima, chi &egrave; alle prime armi o ha pochi mesi di pratica nella seconda.</p>

<blockquote class="kquote">KOTEEEEEEEE!!!! &mdash; Conan il Barbaro, PKK Version</blockquote>

<h2 class="section-heading">Regolamento (sintesi)</h2>
<p><strong>Sistema a pool</strong>: le squadre vengono suddivise in pool da 3 (con eventuali pool da 2 o 4 per i resti). Tempo di gara: 2 minuti per ogni incontro individuale; se non si ottiene un risultato entro il tempo assegnato, l'incontro &egrave; dichiarato in pareggio.</p>
<p>La squadra vincente in pool si determina in base a: numero di vittorie individuali &rarr; punti fatti &rarr; ippon fatti &rarr; eventuale spareggio (ippon-shobu senza limiti di tempo).</p>
<p>Punteggio: vittoria di squadra 3 punti, pareggio 1 punto, sconfitta 0 punti. Le due squadre con pi&ugrave; punti accedono alla fase finale.</p>
<p><strong>Tabellone ad eliminazione diretta</strong>: semifinali e finale durano 3 minuti; in caso di parit&agrave; si procede come sopra, fino a un eventuale spareggio.</p>
<p>Nella categoria Valle dei Cuccioli si esegue uchikomi geiko, giudicato con Hantei.</p>

<h2 class="section-heading">La maglietta</h2>
<p>A ciascuna edizione la sua maglietta, rigorosamente <em>@biacca design</em>.</p>
<figure class="pkk-figure mb-10">
  <img src="{prefix}images/conan-maglietta.webp" alt="Maglietta ufficiale Conan Cup">
</figure>

<hr class="border-white/10 my-14">

<h2 class="section-heading">Risultati edizione 2024</h2>
<figure class="pkk-figure mb-10">
  <img src="{prefix}images/conan-2024-risultati.webp" alt="Tabellone risultati Conan Cup 2024">
</figure>

<div class="grid sm:grid-cols-2 gap-10 not-prose">
  <div>
    <h3 class="font-display text-paper mb-2">Blu Tornado degli Schiaffoni</h3>
    """ + ranking(["Le Bimbe di Moretti &mdash; Grandi, Pesci, Bracciali", "I guerrieri della nebbia &mdash; Bergamin, Rossi, Noci", "Noticed by Sempai &mdash; Paterlini, Biacca, Valentini"]) + """
  </div>
  <div>
    <h3 class="font-display text-paper mb-2">Brucomela con Abbracci</h3>
    """ + ranking(["Otamajakushi", "I Tanuki", "Men o Male"]) + """
  </div>
</div>

<hr class="border-white/10 my-14">

<h2 class="section-heading">Risultati edizione 2023</h2>
<div class="grid sm:grid-cols-3 gap-8 not-prose mb-10">
  <div>
    <h3 class="font-display text-paper mb-2">Tana delle Tigri</h3>
    """ + ranking(["Ghirardini", "Tabellini", "Paterlini"]) + """
  </div>
  <div>
    <h3 class="font-display text-paper mb-2">Accademia dei Lividi</h3>
    """ + ranking(["Biacca", "Negri", "Guarnieri"]) + """
  </div>
  <div>
    <h3 class="font-display text-paper mb-2">Valle dei Cuccioli</h3>
    """ + ranking(["Frisone", "Caravaggio", "Cappellaro"]) + """
  </div>
</div>

<figure class="pkk-figure mb-10">
  <img src="{prefix}images/conan-2023-gruppo.webp" alt="Foto di gruppo, partecipanti Conan Cup 2023">
  <figcaption>Partecipanti alla Conan Cup 2023</figcaption>
</figure>

<h3 class="font-display text-paper mt-10 mb-3">Statistiche edizione 2023</h3>
<div class="grid gap-3 not-prose mb-10">
""" + "\n  ".join(doc_card(h, l, False) for h, l in [
    ("documenti/stats-tana-delle-tigri.pdf", "Statistiche &ndash; Tana delle Tigri"),
    ("documenti/stats-accademia-dei-lividi.pdf", "Statistiche &ndash; Accademia dei Lividi"),
    ("documenti/stats-valle-dei-cuccioli.pdf", "Statistiche &ndash; Valle dei Cuccioli"),
]) + """
</div>

<p>Ci vediamo alla prossima Conan Cup!</p>
""" + CONTAINER_CLOSE

write_page("conan-cup.html",
    "CONAN CUP | Parma Kendo Kai",
    "La Conan Cup, competizione interna di Kendo della Parma Kendo Kai: regolamento, categorie e risultati.",
    content_conan)

# ==================================================================
# CODICE DI CONDOTTA
# ==================================================================
SAFEGUARD_SECTIONS = [
    ("Nessuno escluso", [
        "Rispettiamo la dignit&agrave; e l'integrit&agrave; di tutte le persone coinvolte nelle attivit&agrave; sportive, senza discriminazioni di alcun genere.",
        "Trattiamo tutti con cortesia, gentilezza e rispetto, evitando linguaggio offensivo o comportamenti intimidatori.",
        "Creiamo attivit&agrave; tese a promuovere l'inclusione attraverso lo sport.",
    ]),
    ("Sensibilizzazione, sicurezza e benessere", [
        "Garantiamo chiarezza sui concetti di abuso, molestia, violenza di genere o discriminazione.",
        "Mettiamo al primo posto la sicurezza e il benessere di tutti i tesserati, specie se minori.",
        "Rispettiamo i diritti e le opinioni degli altri, garantendo un ambiente in cui esprimere preoccupazioni o segnalare comportamenti inappropriati.",
    ]),
    ("Comportamenti non verbali", [
        "Chiediamo a tutti comportamenti professionali e appropriati, evitando qualsiasi contatto fisico inappropriato.",
        "Garantiamo che eventuali comportamenti inappropriati siano interrotti tempestivamente.",
    ]),
    ("Informazioni, comunicazioni e privacy", [
        "Informiamo i tesserati sui contatti del Responsabile Safeguarding e del Safeguarding Office nazionale CSEN APS.",
        "Comunichiamo in modo chiaro, aperto e rispettoso, fornendo copia del codice di condotta e del modulo di segnalazione.",
        "Rispettiamo la privacy dei tesserati e la riservatezza delle informazioni personali.",
    ]),
    ("Formazione", [
        "Partecipiamo a programmi di formazione sulla tutela safeguarding.",
        "Riconosciamo il nostro ruolo nel proteggere i tesserati e segnalare ogni sospetto di abuso.",
    ]),
]

def safeguard_block(i, title, items):
    lis = "".join(f'<li class="text-paper-dim text-sm mb-2">{it}</li>' for it in items)
    return f"""<div class="border-t border-white/10 py-6">
    <h3 class="font-display text-paper mb-3">{i}. {title}</h3>
    <ul class="list-disc pl-5 m-0">{lis}</ul>
  </div>"""

content_condotta = page_banner("Codice di Condotta &ndash; Safeguarding", "A tutela dei minori e per la prevenzione delle molestie, della violenza di genere e di ogni altra condizione di discriminazione.", "規範") + CONTAINER_OPEN + """
<p>I destinatari del presente Codice di condotta sono gli istruttori, i tecnici, i dirigenti, i collaboratori a qualsiasi titolo, livello e qualifica, i lavoratori ed i volontari.</p>

<p>I soggetti sopra indicati sono responsabili della crescita dei giovani allievi e tesserati, nonch&eacute; della creazione di un ambiente positivo, sicuro e stimolante per la pratica sportiva. A tal fine sono chiamati a dare il buon esempio e ad essere un modello per gli allievi affiliati alla ASD/SSD.</p>

<p>Tutti i soggetti sopra indicati che hanno un contatto diretto con allievi e tesserati minorenni sono obbligati a rispettare il Codice di condotta, che accettano integralmente dopo averne preso visione. Ogni presunta violazione deve essere segnalata al Responsabile Safeguarding nominato dalla ASD/SSD. Le misure e le sanzioni potranno andare dall'ammonimento verbale fino alla cessazione della collaborazione.</p>

<p>La ASD Parma Kendo Kai si impegna a garantire un ambiente sicuro, rispettoso e inclusivo per tutti i tesserati, inclusi i minori e gli adulti vulnerabili.</p>

<div class="not-prose mt-4">
""" + "\n  ".join(safeguard_block(i, t, its) for i, (t, its) in enumerate(SAFEGUARD_SECTIONS, start=1)) + """
</div>

<h2 class="section-heading mt-12">Impegni di tutti i destinatari del codice</h2>
<p>Tutti i soggetti destinatari si impegnano, fra le altre cose, a rispettare la dignit&agrave; di ogni tesserato senza discriminazioni; a promuovere fair play e correttezza; a non tollerare linguaggi o comportamenti offensivi; a valorizzare gli sforzi dei giovani atleti indipendentemente dai risultati; a educare al rispetto e alla collaborazione; a garantire la sicurezza e la supervisione dei minori durante attivit&agrave; e trasferte; a non pubblicare fotografie o informazioni sui minori senza liberatoria firmata dai genitori; e a segnalare sempre eventuali dubbi al Responsabile Safeguarding.</p>

<p class="text-sm text-paper-dim/60 mt-8">Il testo integrale del codice, con l'elenco completo degli impegni, &egrave; disponibile su richiesta presso l'associazione.</p>
""" + CONTAINER_CLOSE

write_page("codice-condotta.html",
    "Codice di Condotta – Safeguarding | Parma Kendo Kai",
    "Codice di condotta ASD Parma Kendo Kai a tutela dei minori e per la prevenzione di molestie e discriminazioni.",
    content_condotta)

# ==================================================================
# DOVE & QUANDO
# ==================================================================
content_dove = page_banner("Dove &amp; Quando", "Il luogo e gli orari dei nostri allenamenti.", "場所") + CONTAINER_OPEN + """
<h2 class="section-heading">Dove si trova il luogo di pratica</h2>
<p>Il corso adulti e il corso bambini-ragazzi si svolgono a Parma negli spazi dell'<strong>Aiki Center</strong>, in Via San Leonardo 191a.</p>

<figure class="pkk-figure mb-10">
  <img src="{prefix}images/dove-1.webp" alt="Ingresso della palestra Aiki Center">
</figure>

<div class="map-consent not-prose" id="pkk-map-consent" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1744.393042620377!2d10.340512033165542!3d44.834950018994085!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47806bb9a919e16d:0xf02d43684efd83c3!2sParma%20Kendo%20Kai%20A.S.D.!5e1!3m2!1sen!2sit" data-map-title="Mappa Aiki Center, Via San Leonardo 191a, Parma">
  <p class="text-paper-dim text-sm mb-3">Qui sotto puoi caricare la mappa di Google Maps. Caricandola, il tuo browser scambia dati con i server di Google (vedi la nostra <a href="{prefix}privacy.html">Privacy &amp; Cookie Policy</a>).</p>
  <button type="button" class="hero-cta-ghost font-display text-sm px-5 py-2.5" id="pkk-map-load-btn">Carica la mappa di Google</button>
</div>

<h2 class="section-heading">Quando</h2>
<table class="schedule not-prose">
  <tr><th>Corso</th><th>Giorni</th><th>Orario</th></tr>
  <tr><td>Adulti</td><td>Luned&igrave; e mercoled&igrave;</td><td>20:00 &ndash; 21:30</td></tr>
  <tr><td>Bambini &ndash; Ragazzi</td><td>Mercoled&igrave; e venerd&igrave;</td><td>17:30 &ndash; 18:30</td></tr>
</table>

<div class="info-panel my-10 not-prose">
  <h3>Stagione 2026/2027</h3>
  <p class="text-paper-dim text-sm mb-0">Luned&igrave; 7 settembre: inizio corso adulti<br>
  Mercoled&igrave; 30 settembre: inizio corso bambini</p>
</div>

<p>La via in cui si trova la palestra offre parcheggio sia ad automobili che a motorini.</p>
""" + CONTAINER_CLOSE

write_page("contatti-info/dove-quando.html",
    "Dove & Quando | Parma Kendo Kai",
    "Dove si allena la Parma Kendo Kai a Parma e gli orari dei corsi adulti e bambini.",
    content_dove)

# ==================================================================
# COME INIZIARE
# ==================================================================
content_come = page_banner("Come iniziare", "Lezioni di prova gratuite, senza impegno.", "入門") + CONTAINER_OPEN + """
<figure class="pkk-figure mb-10">
  <img src="{prefix}images/locandina.webp" alt="Locandina Parma Kendo Kai">
</figure>

<h2 class="section-heading">Corso Adulti</h2>
<p>L'associazione d&agrave; a tutti gli interessati la possibilit&agrave; di frequentare 2 lezioni di prova gratuite nei mesi di settembre e gennaio, in modo da permettere una visione complessiva di quella che &egrave; la disciplina.</p>
<p>Negli altri mesi dell'anno sar&agrave; prevista la possibilit&agrave; di fare 1 lezione di prova gratuita.</p>
<p>Nel primo periodo sar&agrave; sufficiente partecipare alle lezioni in tuta da ginnastica: l'attrezzatura con la quale si svolge la pratica verr&agrave; prestata dall'associazione per i primi mesi. Successivamente si concorder&agrave; l'acquisto di una propria.</p>
<p>All'atto di iscrizione sar&agrave; inoltre necessario presentare un certificato di buona salute, oppure un certificato medico per la pratica agonistica.</p>

<h2 class="section-heading">Corso Bambini &ndash; Ragazzi</h2>
<p>Verr&agrave; organizzato un Open Day a fine settembre e, da ottobre, sar&agrave; possibile fare una lezione di prova gratuita la prima settimana di ogni mese.</p>
<p>Anche in questo caso, nel primo periodo &egrave; sufficiente partecipare alle lezioni in tuta da ginnastica: l'attrezzatura viene prestata dall'associazione per i primi mesi.</p>
<p>All'atto di iscrizione sar&agrave; necessario presentare un certificato di buona salute, oppure un certificato medico per la pratica agonistica.</p>

<h2 class="section-heading">Per contattarci</h2>
<div class="info-panel not-prose mb-10">
  <h3>Mail</h3>
  <p class="text-paper-dim text-sm mb-0"><a href="mailto:parmakendokai@libero.it" class="text-dojo-orange">parmakendokai@libero.it</a></p>
  <h3>Telefono</h3>
  <p class="text-paper-dim text-sm mb-0">349 159 5885 &mdash; Cellulare &amp; WhatsApp (Francesco)</p>
  <h3>Facebook &amp; Instagram</h3>
  <p class="text-paper-dim text-sm mb-0">Messaggio diretto sulle nostre pagine</p>
</div>

<h2 class="section-heading">Scrivici</h2>
<form class="not-prose grid gap-4" action="#" method="post">
  <div>
    <label class="block font-display text-sm text-paper mb-2" for="nome">Nome</label>
    <input class="w-full bg-panel border border-white/15 focus:border-dojo-orange px-4 py-3 text-paper" type="text" id="nome" name="nome" required>
  </div>
  <div>
    <label class="block font-display text-sm text-paper mb-2" for="email">Email</label>
    <input class="w-full bg-panel border border-white/15 focus:border-dojo-orange px-4 py-3 text-paper" type="email" id="email" name="email" required>
  </div>
  <div>
    <label class="block font-display text-sm text-paper mb-2" for="messaggio">Messaggio</label>
    <textarea class="w-full bg-panel border border-white/15 focus:border-dojo-orange px-4 py-3 text-paper min-h-[130px]" id="messaggio" name="messaggio" required></textarea>
  </div>
  <button class="hero-cta-primary font-display px-7 py-3.5 text-sm tracking-wide w-fit" type="submit">Invia messaggio</button>
</form>
<p class="text-sm text-paper-dim/60 mt-4">Nota tecnica: per far funzionare davvero questo modulo su un sito statico serve collegarlo a un servizio come Formspree o Netlify Forms.</p>
""" + CONTAINER_CLOSE

write_page("contatti-info/come-iniziare.html",
    "Come iniziare | Parma Kendo Kai",
    "Come iniziare a praticare Kendo alla Parma Kendo Kai: lezioni di prova e contatti.",
    content_come)

# ==================================================================
# COSTI & ATTREZZATURA
# ==================================================================
content_costi = page_banner("Costi &ndash; Quota &amp; Attrezzatura", "Quanto costa iniziare, davvero.", "費用") + CONTAINER_OPEN + """
<h2 class="section-heading">Associarsi e praticare</h2>
<p>La Parma Kendo Kai a.s.d. <strong>&egrave; un'associazione senza scopo di lucro</strong> e l'insegnante non percepisce alcun compenso o rimborso spese dalle quote: tutto il denaro versato all'associazione viene utilizzato per pagare l'affitto della palestra, le iscrizioni alla federazione, all'ente di promozione sportiva e i canoni del conto corrente.</p>
<p>L'attivit&agrave; di Parma Kendo Kai asd si rivolge esclusivamente ai propri associati.</p>

<div class="info-panel my-8 not-prose">
  <h3>Quota 2026&ndash;2027</h3>
  <p class="text-paper text-2xl font-display mb-0">360&euro; <span class="text-sm text-paper-dim font-body">per entrambi i corsi</span></p>
</div>

<p>All'atto dell'adesione sar&agrave; necessario portare un certificato per la pratica non agonistica, oppure un certificato medico per la pratica agonistica: quest'ultimo permette inoltre di partecipare alle competizioni organizzate durante l'anno dalla federazione o da altre associazioni.</p>

<h2 class="section-heading">L'attrezzatura</h2>
<p>Come indicato nella sezione &laquo;Come iniziare&raquo;, l'attrezzatura nei primi mesi viene fornita dall'associazione. Ma quanto costa acquistarne una propria? Quali sono i criteri di scelta? &Egrave; necessario comprare tutto in un'unica soluzione o si pu&ograve; scaglionare gli acquisti dei vari pezzi? Proviamo a rispondere.</p>

<figure class="pkk-figure mb-10">
  <img src="{prefix}images/hakama-gi.webp" alt="Esempio di hakama e gi">
  <figcaption>Esempio di hakama e gi</figcaption>
</figure>

<p>Il Kendo si pratica con una divisa specifica: si indossa una casacca (<em>gi</em>) che copre la parte superiore del corpo e dei larghi pantaloni con una serie di pieghe (<em>hakama</em>). Questi indumenti si trovano sul mercato singolarmente oppure in set e sono la prima cosa che si indossa appena si lasciano maglietta e pantaloncini della tuta, dopo le prime lezioni di prova.</p>
<p>I negozi online offrono una scelta molto ampia per quanto riguarda qualit&agrave; e materiali. Un buon set basico costa fra i 50&euro; e i 90&euro;, con <em>gi</em> in cotone e <em>hakama</em> in tetron. L'attrezzatura ha poi una durata molto lunga: si pu&ograve; tranquillamente praticare con lo stesso set per pi&ugrave; di 6/7 anni prima di avere una reale necessit&agrave; di cambiarlo.</p>

<div class="gallery-grid grid grid-cols-2 gap-2 my-9 not-prose">
  <img src="{prefix}images/shinai.webp" alt="Esempio di shinai" class="aspect-square object-cover w-full">
  <img src="{prefix}images/bokken.webp" alt="Esempio di bokken" class="aspect-square object-cover w-full">
</div>

<p><em>Shinai</em> &egrave; la spada di bamb&ugrave; con la quale si svolge la maggior parte della pratica: la si usa per gli esercizi di base, per i combattimenti e le gare. Essendo di materiale flessibile permette di colpirsi a vicenda sulle protezioni senza provocare danni. Una <em>shinai</em> per gli allenamenti costa dai 20&euro; ai 45&euro; e, se mantenuta regolarmente, pu&ograve; durare dai 6 mesi a un anno.</p>
<p><em>Bokken</em> o <em>Bokuto</em> &egrave; una spada in legno pieno di quercia o ciliegio, utilizzata per eseguire i 10 <em>Kata</em> (forme) presenti nel Kendo. Non usurandosi, il suo acquisto (circa 30&euro;) pu&ograve; essere fatto una sola volta.</p>
<p>Con questi tre elementi abbiamo gi&agrave; tutto quello che serve per i primi mesi di allenamento e anche per gran parte della pratica futura.</p>

<figure class="pkk-figure mb-10">
  <img src="{prefix}images/bogu.webp" alt="Esempio di bogu, l'armatura da Kendo">
</figure>

<p>L'immagine qui sopra mostra un <em>bogu</em>, l'armatura con la quale ci si allena e che permette di combattere in tutta sicurezza. &Egrave; composta da <em>Men</em> (protezione per il capo), <em>Do</em> (protezione per il busto), <em>Kote</em> (protezioni per mani e polsi) e <em>Tare</em> (protezione per il basso ventre e i fianchi).</p>
<p>Dopo qualche mese, quando si sono acquisite in modo abbastanza solido le basi, si pu&ograve; cominciare a indossarla. Il nostro approccio &egrave; quello di cominciare dal <em>tare</em> e dal <em>do</em>, per abituarsi a svolgere gli esercizi con due ingombri in pi&ugrave; rispetto alle settimane precedenti; successivamente si passa a indossare anche <em>kote</em> e <em>men</em>.</p>
<p>Un'armatura completa parte dai 350&euro; in su: gli store online offrono spesso sconti e offerte che permettono di risparmiare o di aggiungere altri componenti all'acquisto.</p>
""" + CONTAINER_CLOSE

write_page("contatti-info/costi.html",
    "Costi – Quota & Attrezzatura | Parma Kendo Kai",
    "Quote associative e costi indicativi dell'attrezzatura da Kendo: gi, hakama, shinai, bokken e bogu.",
    content_costi)

# ==================================================================
# RISORSE
# ==================================================================
def link_group(title, links):
    items = "".join(f'<li><a class="doc-card" href="{h}" target="_blank" rel="noopener"><span class="text-sm">{l}</span></a></li>' for h, l in links)
    return f'<h2 class="section-heading">{title}</h2><ul class="not-prose grid gap-3 list-none p-0 m-0 mb-10">{items}</ul>'

content_risorse = page_banner("Risorse", "Link utili per approfondire il Kendo.", "資料") + CONTAINER_OPEN + \
    link_group("Siti istituzionali", [
        ("https://confederazioneitalianakendo.it/", "Confederazione Italiana Kendo"),
        ("http://www.ekf-eu.com/", "European Kendo Federation"),
        ("https://www.kendo-fik.org/", "International Kendo Federation"),
    ]) + \
    link_group("Forum &amp; blog", [
        ("https://kenshi247.net/", "Kenshi247.net"),
        ("https://kendojidai.com/", "Kendo Jidai International"),
        ("http://kendoinfo.net/", "Kendoinfo.net"),
        ("https://kendonellemarche.wordpress.com/", "Kendo nelle Marche"),
        ("https://www.kendo-world.com/", "Kendo World"),
    ]) + \
    link_group("Attrezzatura", [
        ("https://www.tozandoshop.com/", "Tozando"),
        ("https://alljapanbudogu.world/", "Zen Nihon Budogu"),
        ("https://www.ninecircles.co.uk/", "Nine Circles"),
        ("https://kendostar.com/", "Kendo Star"),
    ]) + CONTAINER_CLOSE

write_page("contatti-info/risorse.html",
    "Risorse | Parma Kendo Kai",
    "Link utili su Kendo: federazioni, forum, blog e negozi di attrezzatura.",
    content_risorse)

# ==================================================================
# GALLERIA
# ==================================================================
content_galleria = page_banner("Galleria", "Le foto della Parma Kendo Kai &mdash; allenamenti, eventi, momenti di dojo.", "写真") + """
<div class="max-w-6xl mx-auto px-5 md:px-8 py-16">
<p class="text-paper-dim/60 text-sm mb-8" id="pkk-gallery-status" role="status">Caricamento foto...</p>
<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-1.5 not-prose" id="pkk-gallery-grid"></div>
</div>
"""

write_page("galleria.html",
    "Galleria | Parma Kendo Kai",
    "Foto della Parma Kendo Kai: allenamenti, eventi e momenti di vita del dojo.",
    content_galleria,
    extra_scripts='<script src="{prefix}js/galleria.js"></script>')

# ==================================================================
# PRIVACY POLICY
# ==================================================================
content_privacy = page_banner("Informativa sulla Privacy", "Trattamento dei dati personali ai sensi degli artt. 13-14 del Regolamento (UE) 2016/679 (GDPR).", "個人情報") + CONTAINER_OPEN + """
<p class="text-sm text-paper-dim/60 mb-8"><em>Ultimo aggiornamento: da compilare alla pubblicazione.</em></p>

<h2 class="section-heading">Titolare del trattamento</h2>
<p>Parma Kendo Kai a.s.d., con sede in Via San Leonardo 191a, Parma (Aiki Center) &mdash; email: <a href="mailto:parmakendokai@libero.it">parmakendokai@libero.it</a>.</p>

<h2 class="section-heading">Quali dati raccogliamo e perch&eacute;</h2>
<p>Raccogliamo dati personali attraverso i moduli collegati al sito (Google Forms), in particolare:</p>
<ul>
  <li><strong>Modulo di iscrizione</strong>: nome, cognome, dati anagrafici e di contatto, certificato medico &mdash; per gestire il tesseramento associativo, CSEN e C.I.K. (Confederazione Italiana Kendo).</li>
  <li><strong>Modulo di contatto</strong>: nome, email, messaggio &mdash; per rispondere a richieste di informazioni.</li>
  <li><strong>Upload documenti</strong> (certificato medico, modulo privacy): per gli obblighi di tesseramento sportivo.</li>
</ul>
<p>Se l'iscritto &egrave; minorenne, il trattamento avviene sulla base del consenso di chi esercita la responsabilit&agrave; genitoriale. Per le regole di tutela dei minori all'interno delle attivit&agrave; sportive, vedi il <a href="{prefix}codice-condotta.html">Codice di Condotta &ndash; Safeguarding</a>.</p>

<h2 class="section-heading">Base giuridica</h2>
<p>Il trattamento si fonda sul consenso dell'interessato (art. 6.1.a GDPR) e, per le finalit&agrave; di tesseramento sportivo, sull'esecuzione del rapporto associativo e sugli obblighi verso gli enti affilianti (CSEN, C.I.K.).</p>

<h2 class="section-heading">Come trattiamo i dati</h2>
<p>I moduli del sito sono gestiti tramite <strong>Google Forms, Google Sheets e Google Drive</strong> (fornitore: Google Ireland Limited), che agisce come responsabile del trattamento per conto dell'associazione. I dati sono trattati con strumenti elettronici e misure di sicurezza adeguate a prevenirne la perdita, l'uso illecito o l'accesso non autorizzato. Google pu&ograve; trattare i dati anche al di fuori dello Spazio Economico Europeo, sulla base delle clausole contrattuali standard previste dalla normativa europea.</p>

<h2 class="section-heading">A chi comunichiamo i dati</h2>
<p>I dati raccolti per il tesseramento vengono comunicati a CSEN e alla Confederazione Italiana Kendo, nella misura necessaria all'affiliazione e alla partecipazione a corsi e competizioni. Non cediamo dati a terzi per finalit&agrave; commerciali o pubblicitarie.</p>

<h2 class="section-heading">Per quanto tempo conserviamo i dati</h2>
<p>I dati sono conservati per il tempo necessario alle finalit&agrave; sopra indicate e comunque non oltre la durata del rapporto associativo, salvo obblighi di legge o contabili/fiscali che richiedano una conservazione pi&ugrave; lunga.</p>

<h2 class="section-heading">I tuoi diritti</h2>
<p>In qualsiasi momento puoi richiedere: accesso ai tuoi dati, rettifica, cancellazione, limitazione del trattamento, opposizione, portabilit&agrave; dei dati. Puoi esercitare questi diritti scrivendo a <a href="mailto:parmakendokai@libero.it">parmakendokai@libero.it</a>. Hai inoltre diritto di proporre reclamo al Garante per la Protezione dei Dati Personali (<a href="https://www.garanteprivacy.it/" target="_blank" rel="noopener">www.garanteprivacy.it</a>).</p>

<p class="text-sm text-paper-dim/60 mt-10">Per l'uso di cookie e strumenti di terze parti sul sito, vedi la <a href="{prefix}cookie-policy.html">Cookie Policy</a>.</p>
""" + CONTAINER_CLOSE

write_page("privacy.html",
    "Informativa sulla Privacy | Parma Kendo Kai",
    "Informativa sul trattamento dei dati personali della Parma Kendo Kai, ai sensi del GDPR.",
    content_privacy)

# ==================================================================
# COOKIE POLICY
# ==================================================================
content_cookie = page_banner("Cookie Policy", "Quali cookie e strumenti di terze parti usa questo sito.", "クッキー") + CONTAINER_OPEN + """
<h2 class="section-heading">Cookie di questo sito</h2>
<p>Questo sito, di per s&eacute;, non installa cookie di profilazione propri e non traccia gli utenti a fini pubblicitari. Alcune pagine usano <strong>localStorage</strong> del browser (non un cookie in senso tecnico) solo per ricordare, sul tuo dispositivo, il carrello o le preferenze di visualizzazione: questi dati restano sul tuo dispositivo e non vengono mai inviati a noi.</p>

<h2 class="section-heading">Servizi di terze parti incorporati</h2>
<p>Alcune pagine caricano risorse da server di terze parti, che potrebbero installare cookie tecnici o di loro propriet&agrave;:</p>
<ul>
  <li><strong>Google Fonts</strong>: per caricare i caratteri tipografici del sito (pagina <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">informativa privacy di Google</a>).</li>
  <li><strong>Google Maps</strong>: nella pagina <a href="{prefix}contatti-info/dove-quando.html">Dove &amp; Quando</a> la mappa <strong>non si carica automaticamente</strong>: viene mostrata solo dopo che l'utente clicca sull'apposito pulsante "Carica la mappa di Google", cos&igrave; da evitare cookie di terze parti finch&eacute; non lo decidi tu.</li>
  <li><strong>Google Forms / Drive</strong>: i moduli e la galleria foto del sito si appoggiano a Google Forms, Sheets e Drive, soggetti anch'essi all'informativa privacy di Google.</li>
</ul>
<p>Questi servizi sono forniti da Google Ireland Limited. Per maggiori dettagli, consulta la <a href="https://policies.google.com/technologies/cookies" target="_blank" rel="noopener">cookie policy di Google</a>.</p>

<h2 class="section-heading">Come gestire i cookie dal browser</h2>
<p>Puoi bloccare o eliminare i cookie in qualsiasi momento dalle impostazioni del tuo browser. Ecco le guide ufficiali per i browser pi&ugrave; comuni:</p>
<ul>
  <li><a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener">Google Chrome</a></li>
  <li><a href="https://support.mozilla.org/it/kb/protezione-antitracciamento-avanzata-firefox-desktop" target="_blank" rel="noopener">Mozilla Firefox</a></li>
  <li><a href="https://support.apple.com/it-it/guide/safari/sfri11471/mac" target="_blank" rel="noopener">Safari</a></li>
</ul>

<p class="text-sm text-paper-dim/60 mt-10">Per informazioni su come trattiamo i dati raccolti tramite i moduli del sito, vedi l'<a href="{prefix}privacy.html">Informativa sulla Privacy</a>.</p>
""" + CONTAINER_CLOSE

write_page("cookie-policy.html",
    "Cookie Policy | Parma Kendo Kai",
    "Quali cookie e servizi di terze parti (Google Fonts, Maps, Forms) usa il sito della Parma Kendo Kai.",
    content_cookie)

print("\nFatto. Sito generato in", ROOT)
