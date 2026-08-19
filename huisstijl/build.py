#!/usr/bin/env python3
"""Bouwt drie huisstijlvoorstellen voor projectnaam HIERO (Dirk de Derdelaan, Vlaardingen).

Elke richting wordt een losse HTML van ~17 liggende pagina's (280x210mm) die met
headless Chromium naar PDF wordt geprint. Alle beeld is vector: er is nog geen
projectfotografie, en beeldbanken zijn in deze omgeving niet bereikbaar.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = HERE

# ---------------------------------------------------------------- fonts

def face(fam, weight, style, fname):
    return (
        "@font-face{font-family:'%s';font-weight:%s;font-style:%s;"
        "src:url('file://%s/%s') format('truetype');font-display:block}"
        % (fam, weight, style, FONTS, fname)
    )

FONT_CSS = "".join([
    face("Fraunces", 400, "normal", "Fraunces-400.ttf"),
    face("Fraunces", 700, "normal", "Fraunces-700.ttf"),
    face("Fraunces", 900, "normal", "Fraunces-900.ttf"),
    face("Inter", 400, "normal", "Inter-400.ttf"),
    face("Inter", 500, "normal", "Inter-500.ttf"),
    face("Inter", 600, "normal", "Inter-600.ttf"),
    face("Inter", 700, "normal", "Inter-700.ttf"),
    face("Archivo", 500, "normal", "Archivo-500.ttf"),
    face("Archivo", 700, "normal", "Archivo-700.ttf"),
    face("Archivo", 900, "normal", "Archivo-900.ttf"),
    face("Bricolage", 400, "normal", "BricolageGrotesque-400.ttf"),
    face("Bricolage", 600, "normal", "BricolageGrotesque-600.ttf"),
    face("Bricolage", 800, "normal", "BricolageGrotesque-800.ttf"),
    face("Newsreader", 400, "normal", "Newsreader-400.ttf"),
    face("Newsreader", 600, "normal", "Newsreader-600.ttf"),
    face("Newsreader", 400, "italic", "Newsreader-400i.ttf"),
    face("Karla", 400, "normal", "Karla-400.ttf"),
    face("Karla", 700, "normal", "Karla-700.ttf"),
])

# ---------------------------------------------------------------- thema's

THEMES = {
    "1018": {
        "key": "1018",
        "nr": "01",
        "titel": "Anno 1018",
        "onderkop": "De richting van het zegel",
        "belofte": "Hier begon Holland voor zichzelf.",
        "kernidee": (
            "Het straatnaambord is geen probleem maar de bron. Dirk de Derdelaan is vernoemd naar "
            "Dirk III, bijgenaamd Hierosolymita, die hier tol hief, een burcht bouwde en in 1018 de "
            "keizer versloeg. Deze richting geeft het adres zijn geschiedenis terug."
        ),
        "houding": "Geworteld, zelfbewust, licht rebels. Oud zonder kostuumdrama.",
        "display": "Fraunces", "body": "Inter", "quote": "Fraunces",
        "bg": "#EFE6D6", "ink": "#2E3234", "paper": "#F7F1E5",
        "accent": "#7B2E26", "accent2": "#B4643C", "accent3": "#5A6B4A", "accent4": "#C08A2E",
        "kleuren": [
            ("Burchtrood", "#7B2E26", "Hoofdkleur. Logo, koppen, vlakken."),
            ("Perkament", "#EFE6D6", "Basis. Achtergrond van vrijwel alles."),
            ("Baksteen", "#B4643C", "Steun. Vlakken, illustratie, kaders."),
            ("Oker", "#C08A2E", "Accent. Alleen klein: jaartal, markering."),
            ("Mos", "#5A6B4A", "Steun. Groen van het erf en de polder."),
            ("Leisteen", "#2E3234", "Tekstkleur en fijne lijnen."),
        ],
        "boodschappen": [
            ("Het adres is ouder dan zijn reputatie",
             "Twintig jaar bijnaam tegenover duizend jaar geschiedenis. Wij zetten dat naast elkaar en laten het rekenen."),
            ("Eigen grond, eigen regels",
             "Dirk III hief tol zonder toestemming. Hier beslissen bewoners samen, vastgelegd in een akte."),
            ("Wat blijft is de constructie en het uitzicht",
             "De rest wordt vervangen. Dat is geen verfbeurt, dat is een nieuw begin op een oud fundament."),
        ],
        "wel": ["Feiten met een jaartal", "Korte, stevige zinnen", "Woorden die al bestonden", "Trots zonder stemverheffing"],
        "niet": ["Riddertaal of pseudo-oud", "Luxe, exclusief, premium", "Grappen over de bijnaam", "Uitroeptekens"],
        "motiefnaam": "Metselverband en keper",
        "motieftekst": "Het verband van de gevel wordt het patroon van de huisstijl. De keperband komt van het zegel en markeert waar iets begint.",
    },
    "bord": {
        "key": "bord",
        "nr": "02",
        "titel": "Het bord",
        "onderkop": "De richting van het straatnaambord",
        "belofte": "Hiero. Dirk de Derdelaan 167–319.",
        "kernidee": (
            "Als het adres het probleem is, zet het adres dan op de gevel. Deze richting leent de vorm "
            "van het Nederlandse emaille straatnaambord: wit op blauw, geen opsmuk, niet te betwisten. "
            "Het merk is een bordje dat zegt waar je bent."
        ),
        "houding": "Zakelijk, direct, stadse nuchterheid. Geen belofte die niet nagekomen kan worden.",
        "display": "Archivo", "body": "Inter", "quote": "Archivo",
        "bg": "#F2F1EC", "ink": "#20242A", "paper": "#FFFFFF",
        "accent": "#14509B", "accent2": "#E4552B", "accent3": "#7E8A93", "accent4": "#9FC8E8",
        "kleuren": [
            ("Bordblauw", "#14509B", "Hoofdkleur. Bord, vlakken, koppen."),
            ("Emaille wit", "#F2F1EC", "Basis. Achtergrond en tekstvlakken."),
            ("Tomaat", "#E4552B", "Accent. Actie, markering, nummers."),
            ("Luchtblauw", "#9FC8E8", "Steun. Hoogte, lucht, uitzicht."),
            ("Beton", "#7E8A93", "Steun. Lijnen, secundaire tekst."),
            ("Asfalt", "#20242A", "Tekstkleur en zwart waar nodig."),
        ],
        "boodschappen": [
            ("Wij noemen het adres als eerste",
             "Wie het verzwijgt, geeft de reputatie het laatste woord. Wij zetten het op het bouwhek."),
            ("Dertien lagen, één richting: omhoog",
             "Elke verdieping is een ander uitzicht en een andere prijs. Dat maken we zichtbaar in plaats van gelijk."),
            ("Alles staat in de akte",
             "Zelfbewoningsplicht, antispeculatiebeding, professioneel beheer. Geen sfeer, maar afspraken."),
        ],
        "wel": ["Getallen en adressen", "Actieve, korte regels", "Kapitalen voor feiten", "Zeggen wat er niet is"],
        "niet": ["Sfeerwoorden zonder bewijs", "Engels", "Bijvoeglijke naamwoorden stapelen", "Vaag over prijs"],
        "motiefnaam": "Bordsysteem en verdiepingsnummers",
        "motieftekst": "Elk bord is een feit. De nummers 01 tot 13 vormen een eigen systeem dat hoogte tot merkbezit maakt.",
    },
    "erf": {
        "key": "erf",
        "nr": "03",
        "titel": "Het erf",
        "onderkop": "De richting van de boog",
        "belofte": "Hiero ken je je buren.",
        "kernidee": (
            "De grootste angst van de doelgroep is niet de prijs maar de vraag wie er straks naast hen "
            "woont en wie hiervoor zorgt. Deze richting antwoordt met het maaiveld: 2.742 m² met "
            "volwassen bomen, twee entreehallen, gedeelde dakterrassen, eigen beheer."
        ),
        "houding": "Warm, gewoon, verzorgd. Menselijk zonder gezellig te doen.",
        "display": "Bricolage", "body": "Inter", "quote": "Newsreader",
        "bg": "#F4EDE2", "ink": "#2C2A26", "paper": "#FBF7F0",
        "accent": "#C05B33", "accent2": "#4C6146", "accent3": "#A9CFE0", "accent4": "#DFCDA9",
        "kleuren": [
            ("Terracotta", "#C05B33", "Hoofdkleur. Boog, logo, koppen."),
            ("Room", "#F4EDE2", "Basis. Achtergrond van vrijwel alles."),
            ("Mosgroen", "#4C6146", "Steun. Bomen, erf, rust."),
            ("Hemel", "#A9CFE0", "Steun. Hoogte en dakterras."),
            ("Zand", "#DFCDA9", "Steun. Vlakken en kaders."),
            ("Inkt", "#2C2A26", "Tekstkleur en fijne lijnen."),
        ],
        "boodschappen": [
            ("Van passanten naar bewoners",
             "Leeg opgeleverd, opnieuw ingericht, en dit keer met eigenaren die blijven."),
            ("Het erf is van iedereen samen",
             "Parkeervakken tussen de bestaande bomen, twee hallen van 92 m², twee dakterrassen van 63 m²."),
            ("Iemand zorgt hiervoor",
             "Een eigen VvE met professioneel beheer. Zichtbaar onderhoud is hier het belangrijkste marketingmiddel."),
        ],
        "wel": ["Spreektaal, korte zinnen", "Namen van plekken en mensen", "Zeggen wie iets doet", "Rustige, hele beelden"],
        "niet": ["Gezellig doen", "Verkleinwoorden", "Beloftes over de buurt", "Stockglimlach"],
        "motiefnaam": "Boog, boom en erf",
        "motieftekst": "De boog komt van de entree en wordt kader, bord en badge. De bomen op het erf staan er al vijftig jaar; die tekenen we niet weg.",
    },
}

# ---------------------------------------------------------------- basis-css

BASE_CSS = """
@page{size:280mm 210mm;margin:0}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;padding:0;background:transparent;font-family:var(--body),sans-serif;color:var(--ink)}
.page{width:280mm;height:210mm;position:relative;overflow:hidden;background:var(--bg);
  page-break-after:always;break-after:page}
.page:last-child{page-break-after:auto;break-after:auto}
.pad{position:absolute;inset:13mm}
.pad-s{position:absolute;inset:9mm}
.lbl{font-family:var(--body);font-weight:600;font-size:6.1pt;letter-spacing:.3em;
  text-transform:uppercase;color:var(--ink);opacity:.55}
.lbl.on-dark{color:#fff;opacity:.6}
.lbl.acc{color:var(--acc);opacity:.85}
.pnum{position:absolute;right:13mm;bottom:11mm;font-family:var(--body);font-weight:500;
  font-size:6.4pt;letter-spacing:.22em;color:var(--ink);opacity:.45}
.brand-foot{position:absolute;left:13mm;bottom:11mm;font-family:var(--body);font-weight:600;
  font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;color:var(--ink);opacity:.45}
h1,h2,h3,p{margin:0}
.hd{font-family:var(--display);font-weight:900;line-height:.94;letter-spacing:-.01em}
.hd-2{font-family:var(--display);font-weight:700;font-size:23pt;line-height:1.02}
.hd-3{font-family:var(--display);font-weight:700;font-size:14pt;line-height:1.12}
.body{font-size:8.8pt;line-height:1.55;max-width:78mm}
.body.wide{max-width:none}
.small{font-size:7.4pt;line-height:1.5;opacity:.72}
.tiny{font-size:6.3pt;line-height:1.45;opacity:.6}
.row{display:flex}
.col{display:flex;flex-direction:column}
.grow{flex:1}
.rule{height:1px;background:var(--ink);opacity:.16}
.rule.acc{background:var(--acc);opacity:.5}
.chip{display:inline-block;padding:1.6mm 3.4mm;border-radius:99mm;font-size:6.6pt;
  font-weight:600;letter-spacing:.14em;text-transform:uppercase}
.mono{font-variant-numeric:tabular-nums}
.sw{position:relative;border-radius:1.2mm;overflow:hidden}
.sw .meta{position:absolute;left:0;right:0;bottom:0;padding:3mm 3.4mm}
.card{background:var(--paper);border-radius:1.6mm}
.dark{background:var(--acc);color:#fff}
.dark .lbl{color:#fff;opacity:.6}
.dark .body,.dark .small,.dark .tiny{color:#fff}
table{border-collapse:collapse;width:100%}
td,th{text-align:left;vertical-align:top;padding:2.4mm 3mm;font-size:7.6pt}
tr+tr td{border-top:1px solid rgba(0,0,0,.1)}
th{font-size:6.1pt;letter-spacing:.26em;text-transform:uppercase;opacity:.55;font-weight:600}
"""

def theme_css(t):
    return (
        ":root{--bg:%s;--ink:%s;--paper:%s;--acc:%s;--acc2:%s;--acc3:%s;--acc4:%s;"
        "--display:'%s';--body:'%s';--quote:'%s'}"
        % (t["bg"], t["ink"], t["paper"], t["accent"], t["accent2"], t["accent3"],
           t["accent4"], t["display"], t["body"], t["quote"])
    )

# ---------------------------------------------------------------- logo's

def logo_1018(w=62, fill="#7B2E26", ink_on="#EFE6D6", tag=True):
    """Zegel: schild met boogtekst, HIERO, en het jaartal."""
    t = ""
    if tag:
        t = (
            '<text x="100" y="196" text-anchor="middle" font-family="Inter" font-weight="600"'
            ' font-size="11" letter-spacing="3.2" fill="%s">ANNO 1018</text>' % ink_on
        )
    return f'''<svg viewBox="0 0 200 240" style="width:{w}mm;height:auto;display:block">
<path d="M14 14 H186 V150 C186 196 148 222 100 232 C52 222 14 196 14 150 Z" fill="{fill}"/>
<path d="M22 22 H178 V149 C178 191 143 214 100 223 C57 214 22 191 22 149 Z"
 fill="none" stroke="{ink_on}" stroke-width="1.6" opacity=".5"/>
<defs><path id="arcT" d="M42 74 A64 64 0 0 1 158 74"/></defs>
<text font-family="Inter" font-weight="600" font-size="10.4" letter-spacing="2.6" fill="{ink_on}" opacity=".85">
<textPath href="#arcT" startOffset="50%" text-anchor="middle">DIRK DE DERDELAAN</textPath></text>
<text x="100" y="132" text-anchor="middle" font-family="Fraunces" font-weight="900"
 font-size="54" letter-spacing="-1" fill="{ink_on}">HIERO</text>
<g fill="{ink_on}" opacity=".9">
<rect x="76" y="148" width="6" height="14"/><rect x="86" y="148" width="6" height="14"/>
<rect x="96" y="148" width="6" height="14"/><rect x="106" y="148" width="6" height="14"/>
<rect x="116" y="148" width="6" height="14"/><rect x="76" y="160" width="46" height="14"/></g>
<rect x="62" y="180" width="76" height="1.4" fill="{ink_on}" opacity=".45"/>
{t}</svg>'''

def mark_1018(w=18, fill="#7B2E26", ink_on="#EFE6D6"):
    return f'''<svg viewBox="0 0 200 240" style="width:{w}mm;height:auto;display:block">
<path d="M14 14 H186 V150 C186 196 148 222 100 232 C52 222 14 196 14 150 Z" fill="{fill}"/>
<text x="100" y="150" text-anchor="middle" font-family="Fraunces" font-weight="900"
 font-size="118" fill="{ink_on}">H</text></svg>'''

def logo_bord(w=96, blue="#14509B", white="#F2F1EC", sub=True):
    s = ""
    if sub:
        s = ('<text x="180" y="112" text-anchor="middle" font-family="Inter" font-weight="600"'
             ' font-size="12.5" letter-spacing="2.2" fill="%s" opacity=".85">'
             'DIRK DE DERDELAAN 167–319</text>' % white)
    return f'''<svg viewBox="0 0 360 140" style="width:{w}mm;height:auto;display:block">
<rect x="0" y="0" width="360" height="140" rx="10" fill="{blue}"/>
<rect x="8" y="8" width="344" height="124" rx="5" fill="none" stroke="{white}"
 stroke-width="2.4" opacity=".55"/>
<text x="180" y="78" text-anchor="middle" font-family="Archivo" font-weight="900"
 font-size="62" letter-spacing="4" fill="{white}">HIERO</text>
{s}</svg>'''

def mark_bord(w=18, blue="#14509B", white="#F2F1EC"):
    return f'''<svg viewBox="0 0 140 140" style="width:{w}mm;height:auto;display:block">
<rect width="140" height="140" rx="10" fill="{blue}"/>
<rect x="8" y="8" width="124" height="124" rx="5" fill="none" stroke="{white}"
 stroke-width="2.6" opacity=".55"/>
<text x="70" y="99" text-anchor="middle" font-family="Archivo" font-weight="900"
 font-size="76" fill="{white}">H</text></svg>'''

def logo_erf(w=58, fill="#C05B33", ink_on="#F4EDE2", groen="#4C6146", sub=True):
    s = ""
    if sub:
        s = ('<text x="100" y="222" text-anchor="middle" font-family="Inter" font-weight="600"'
             ' font-size="10" letter-spacing="3.4" fill="%s" opacity=".85">VLAARDINGEN</text>' % ink_on)
    return f'''<svg viewBox="0 0 200 250" style="width:{w}mm;height:auto;display:block">
<path d="M16 244 V96 A84 84 0 0 1 184 96 V244 Z" fill="{fill}"/>
<path d="M25 236 V96 A75 75 0 0 1 175 96 V236 Z" fill="none" stroke="{ink_on}"
 stroke-width="1.5" opacity=".45"/>
<g opacity=".95" fill="{ink_on}">
<rect x="62" y="62" width="76" height="5"/>
<rect x="66" y="72" width="5.5" height="9"/><rect x="78" y="72" width="5.5" height="9"/>
<rect x="90" y="72" width="5.5" height="9"/><rect x="102" y="72" width="5.5" height="9"/>
<rect x="114" y="72" width="5.5" height="9"/><rect x="126" y="72" width="5.5" height="9"/>
<circle cx="48" cy="70" r="10"/><rect x="46.5" y="70" width="3" height="12"/>
<circle cx="152" cy="70" r="10"/><rect x="150.5" y="70" width="3" height="12"/></g>
<text x="100" y="164" text-anchor="middle" font-family="Bricolage" font-weight="800"
 font-size="52" letter-spacing="-.5" fill="{ink_on}">HIERO</text>
<text x="100" y="188" text-anchor="middle" font-family="Newsreader" font-style="italic"
 font-weight="400" font-size="20" fill="{ink_on}" opacity=".9">op het erf</text>
<rect x="64" y="200" width="72" height="1.3" fill="{ink_on}" opacity=".45"/>
{s}</svg>'''

def mark_erf(w=18, fill="#C05B33", ink_on="#F4EDE2"):
    return f'''<svg viewBox="0 0 200 250" style="width:{w}mm;height:auto;display:block">
<path d="M16 244 V96 A84 84 0 0 1 184 96 V244 Z" fill="{fill}"/>
<text x="100" y="196" text-anchor="middle" font-family="Bricolage" font-weight="800"
 font-size="128" fill="{ink_on}">H</text></svg>'''

def mark_mono(t, w=22):
    """Eén kleur, wit op donker: verplicht op foto en op het hek van de aannemer."""
    k = t["key"]
    if k == "1018":
        return mark_1018(w, fill="#FFFFFF", ink_on=t["ink"])
    if k == "bord":
        return mark_bord(w, blue="#FFFFFF", white=t["ink"])
    return mark_erf(w, fill="#FFFFFF", ink_on=t["ink"])

LOGOS = {"1018": logo_1018, "bord": logo_bord, "erf": logo_erf}
MARKS = {"1018": mark_1018, "bord": mark_bord, "erf": mark_erf}

def logo(t, w=None, on_dark=False):
    """Logo in de juiste kleurstelling voor het thema."""
    k = t["key"]
    if k == "1018":
        return logo_1018(w or 62, fill=("#EFE6D6" if on_dark else t["accent"]),
                         ink_on=(t["accent"] if on_dark else "#EFE6D6"))
    if k == "bord":
        return logo_bord(w or 96, blue=("#F2F1EC" if on_dark else t["accent"]),
                         white=(t["accent"] if on_dark else "#F2F1EC"))
    return logo_erf(w or 58, fill=("#F4EDE2" if on_dark else t["accent"]),
                    ink_on=(t["accent"] if on_dark else "#F4EDE2"))

def mark(t, w=18, on_dark=False):
    k = t["key"]
    if k == "1018":
        return mark_1018(w, fill=("#EFE6D6" if on_dark else t["accent"]),
                         ink_on=(t["accent"] if on_dark else "#EFE6D6"))
    if k == "bord":
        return mark_bord(w, blue=("#F2F1EC" if on_dark else t["accent"]),
                         white=(t["accent"] if on_dark else "#F2F1EC"))
    return mark_erf(w, fill=("#F4EDE2" if on_dark else t["accent"]),
                    ink_on=(t["accent"] if on_dark else "#F4EDE2"))

# ---------------------------------------------------------------- illustraties

def gebouw(w=120, ink="#2E3234", acc="#7B2E26", lucht=None, nummers=False, opak=".14"):
    """Schematische kopgevel van het complex: 12 woonlagen, toplaag, actieve plint."""
    rows = []
    for i in range(12):
        y = 20 + i * 13
        rows.append(f'<rect x="10" y="{y}" width="580" height="10.4" fill="{ink}" opacity="{opak}"/>')
        rows.append(f'<rect x="10" y="{y + 9.6}" width="580" height="1.5" fill="{ink}" opacity=".33"/>')
    verts = "".join(
        f'<rect x="{10 + 52.7 * k}" y="20" width="1.3" height="156" fill="{ink}" opacity=".26"/>'
        for k in range(1, 11)
    )
    nrs = ""
    if nummers:
        nrs = "".join(
            f'<text x="598" y="{31 + i * 13}" font-family="Inter" font-weight="600" font-size="8.4"'
            f' fill="{ink}" opacity=".5">{13 - i:02d}</text>' for i in range(12)
        )
    sky = f'<rect x="0" y="0" width="620" height="18" fill="{lucht}" opacity=".55"/>' if lucht else ""
    return f'''<svg viewBox="0 0 620 220" style="width:{w}mm;height:auto;display:block">
{sky}
<rect x="10" y="8" width="580" height="12" fill="{acc}" opacity=".85"/>
<rect x="70" y="9" width="120" height="10" fill="{acc}"/><rect x="410" y="9" width="120" height="10" fill="{acc}"/>
{"".join(rows)}{verts}
<rect x="10" y="176" width="580" height="26" fill="{acc}"/>
<rect x="120" y="181" width="86" height="21" fill="#fff" opacity=".82"/>
<rect x="392" y="181" width="86" height="21" fill="#fff" opacity=".82"/>
<rect x="250" y="181" width="100" height="21" fill="#fff" opacity=".45"/>
<rect x="10" y="202" width="580" height="3" fill="{ink}" opacity=".45"/>
<g fill="{ink}" opacity=".3">
<rect x="34" y="205" width="24" height="7" rx="3"/><rect x="86" y="205" width="24" height="7" rx="3"/>
<rect x="512" y="205" width="24" height="7" rx="3"/><rect x="560" y="205" width="24" height="7" rx="3"/></g>
{nrs}</svg>'''

def kaart(w=120, ink="#2E3234", acc="#7B2E26", groen="#5A6B4A", water="#9FC8E8", papier="#EFE6D6"):
    """Schematische situatie: polder, snelweg, wijk, rivier, metro."""
    blokken = []
    for r in range(4):
        for c in range(9):
            if r == 1 and 3 <= c <= 6:
                continue
            blokken.append(
                f'<rect x="{60 + c * 52}" y="{182 + r * 40}" width="38" height="26" rx="2"'
                f' fill="{ink}" opacity=".13"/>'
            )
    return f'''<svg viewBox="0 0 600 400" style="width:{w}mm;height:auto;display:block">
<rect width="600" height="400" fill="{papier}"/>
<path d="M0 0 H600 V96 C430 118 210 104 0 132 Z" fill="{groen}" opacity=".42"/>
<text x="24" y="42" font-family="Inter" font-weight="600" font-size="13" letter-spacing="2.4"
 fill="{ink}" opacity=".72">BROEKPOLDER</text>
<text x="24" y="60" font-family="Inter" font-size="10.5" fill="{ink}" opacity=".55">400 ha natuur- en recreatiegebied</text>
<path d="M0 150 C160 132 330 150 600 128" stroke="{ink}" stroke-width="9" fill="none" opacity=".3"/>
<path d="M0 150 C160 132 330 150 600 128" stroke="{papier}" stroke-width="1.6" fill="none"
 stroke-dasharray="7 7"/>
<text x="500" y="122" font-family="Inter" font-weight="700" font-size="12" fill="{ink}" opacity=".6">A20</text>
{"".join(blokken)}
<rect x="212" y="216" width="176" height="15" rx="2" fill="{acc}"/>
<circle cx="300" cy="223.5" r="30" fill="none" stroke="{acc}" stroke-width="1.6" opacity=".55"/>
<text x="300" y="200" text-anchor="middle" font-family="Inter" font-weight="700" font-size="12.5"
 fill="{acc}">HIERO</text>
<text x="300" y="272" text-anchor="middle" font-family="Inter" font-size="10.5" fill="{ink}"
 opacity=".62">Dirk de Derdelaan 167–319</text>
<text x="60" y="352" font-family="Inter" font-weight="600" font-size="12" letter-spacing="2.2"
 fill="{ink}" opacity=".6">WESTWIJK</text>
<path d="M0 372 H600 V400 H0 Z" fill="{water}" opacity=".75"/>
<text x="24" y="391" font-family="Inter" font-weight="600" font-size="11" letter-spacing="2"
 fill="{ink}" opacity=".62">HET SCHEUR</text>
<circle cx="470" cy="300" r="7" fill="{ink}" opacity=".7"/>
<text x="484" y="298" font-family="Inter" font-weight="600" font-size="10.5" fill="{ink}"
 opacity=".7">Metro Vlaardingen West</text>
<text x="484" y="313" font-family="Inter" font-size="9.6" fill="{ink}" opacity=".5">15 min lopen</text>
<path d="M540 336 h34 m0 0 l-7 -5 m7 5 l-7 5" stroke="{ink}" stroke-width="1.7" fill="none" opacity=".6"/>
<text x="484" y="332" font-family="Inter" font-size="9.6" fill="{ink}" opacity=".55">Rotterdam 30 min</text>
</svg>'''

def patroon(t, w=120, h=40):
    ww = "100%" if w is None else "%smm" % w
    """Grafisch motief per richting."""
    k, acc, ink = t["key"], t["accent"], t["ink"]
    if k == "1018":
        br = []
        for r in range(6):
            off = 0 if r % 2 == 0 else -21
            for c in range(16):
                br.append(f'<rect x="{off + c * 42}" y="{r * 20}" width="38" height="16" rx="1.5"'
                          f' fill="{acc}" opacity="{0.16 + 0.05 * (r % 3)}"/>')
        return (f'<svg viewBox="0 0 600 120" preserveAspectRatio="xMinYMid slice"'
                f' style="width:{ww};height:{h}mm;display:block">{"".join(br)}</svg>')
    if k == "bord":
        cells = []
        for c in range(13):
            cells.append(f'<rect x="{6 + c * 46}" y="18" width="38" height="38" rx="4" fill="{acc}"/>'
                         f'<text x="{25 + c * 46}" y="45" text-anchor="middle" font-family="Archivo"'
                         f' font-weight="900" font-size="20" fill="#F2F1EC">{c + 1:02d}</text>')
        arrows = "".join(
            f'<path d="M{14 + c * 46} 84 h26 m0 0 l-8 -6 m8 6 l-8 6" stroke="{t["accent2"]}"'
            f' stroke-width="2.6" fill="none"/>' for c in range(12)
        )
        return (f'<svg viewBox="0 0 600 120" preserveAspectRatio="xMinYMid meet"'
                f' style="width:{ww};height:{h}mm;display:block">{"".join(cells)}{arrows}</svg>')
    bogen = []
    for c in range(10):
        x = 4 + c * 60
        bogen.append(f'<path d="M{x} 120 V52 A24 24 0 0 1 {x + 48} 52 V120 Z" fill="{acc}"'
                     f' opacity="{0.22 + 0.14 * (c % 3)}"/>')
    return (f'<svg viewBox="0 0 600 120" preserveAspectRatio="xMidYMax meet"'
            f' style="width:{ww};height:{h}mm;display:block">{"".join(bogen)}</svg>')

def bomenrij(w=60, kleur="#4C6146", n=7):
    g = []
    for i in range(n):
        x = 10 + i * 40
        g.append(f'<path d="M{x} 70 c0-20 12-34 22-34 s22 14 22 34 z" fill="{kleur}" opacity=".8"/>')
        g.append(f'<rect x="{x + 20}" y="70" width="4" height="16" fill="{kleur}" opacity=".8"/>')
    return f'<svg viewBox="0 0 {n * 40 + 20} 90" style="width:{w}mm;height:auto;display:block">{"".join(g)}</svg>'

# ---------------------------------------------------------------- pagina-frame

PAGES = []

def page(inner, bg=None, num=None, label=None, dark=False):
    st = f' style="background:{bg}"' if bg else ""
    cls = "page dark-page" if dark else "page"
    foot = ""
    if num:
        c = "#fff" if dark else "var(--ink)"
        foot = (f'<div class="brand-foot" style="color:{c}">Hiero · huisstijlvoorstel</div>'
                f'<div class="pnum" style="color:{c}">{num}</div>')
    lb = ""
    if label:
        c = ' on-dark' if dark else ''
        lb = f'<div class="lbl{c}" style="position:absolute;left:13mm;top:12mm">{label}</div>'
    return f'<section class="{cls}"{st}>{lb}{inner}{foot}</section>'

# ---------------------------------------------------------------- pagina 1: omslag

def p_cover(t):
    k = t["key"]
    if k == "bord":
        inner = f'''
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">
  {logo_bord(140, blue=t["accent"], white="#F2F1EC")}
</div>
<div class="pad">
  <div class="lbl on-dark">Huisstijlvoorstel {t["nr"]} — {t["titel"]}</div>
  <div style="position:absolute;left:0;bottom:0;color:#fff">
    <div style="font-family:var(--body);font-weight:600;font-size:10pt;letter-spacing:.04em">
      Dirk de Derdelaan 167–319, Vlaardingen-Westwijk</div>
    <div style="font-family:var(--body);font-size:8.4pt;opacity:.7;margin-top:1.6mm">
      146 woningen · verkoopstart H2 2028 · augustus 2026</div>
  </div>
  <div style="position:absolute;right:0;bottom:0;text-align:right;color:#fff;opacity:.75">
    <div style="font-family:var(--display);font-weight:700;font-size:12pt">{t["belofte"]}</div>
  </div>
</div>'''
        return page(inner, bg=t["accent"], dark=True)

    if k == "erf":
        inner = f'''
<div style="position:absolute;left:0;right:0;bottom:0;height:64mm;overflow:hidden">
  {patroon(t, 300, 60)}
</div>
<div class="pad">
  <div class="lbl">Huisstijlvoorstel {t["nr"]} — {t["titel"]}</div>
  <div style="position:absolute;left:0;top:26mm">
    <div class="hd" style="font-size:104pt;color:var(--acc)">Hiero</div>
    <div class="hd-2" style="margin-top:5mm;max-width:120mm;color:var(--ink)">
      Dirk de Derdelaan 167–319, Vlaardingen-Westwijk</div>
    <div class="small" style="margin-top:4mm">146 woningen · verkoopstart H2 2028 · augustus 2026</div>
  </div>
  <div style="position:absolute;right:0;top:14mm">{logo_erf(56, fill=t["accent"], ink_on="#F4EDE2")}</div>
</div>'''
        return page(inner)

    inner = f'''
<div style="position:absolute;left:0;right:0;top:0;height:26mm;overflow:hidden;opacity:.5">
  {patroon(t, 300, 26)}
</div>
<div class="pad">
  <div class="lbl" style="margin-top:16mm">Huisstijlvoorstel {t["nr"]} — {t["titel"]}</div>
  <div style="position:absolute;left:0;top:52mm">
    <div class="hd" style="font-size:112pt;color:var(--acc)">Hiero</div>
    <div class="hd-2" style="margin-top:6mm;max-width:118mm">
      Dirk de Derdelaan 167–319, Vlaardingen-Westwijk</div>
    <div class="small" style="margin-top:4mm">146 woningen · verkoopstart H2 2028 · augustus 2026</div>
  </div>
  <div style="position:absolute;right:0;bottom:0">{logo_1018(60, fill=t["accent"])}</div>
</div>'''
    return page(inner)

# ---------------------------------------------------------------- pagina 2: de naam

def p_naam(t):
    inner = f'''
<div class="pad">
  <div style="display:flex;gap:14mm;height:100%">
    <div style="width:112mm;padding-top:16mm">
      <div class="hd" style="font-size:40pt;color:var(--acc)">Waarom Hiero</div>
      <p class="body" style="margin-top:7mm;max-width:104mm">
        Het adres is het probleem: wie <em>Dirk de Derdelaan</em> intypt, krijgt twintig jaar reputatie
        als eerste resultaat. De naam Hiero lost dat niet op door weg te kijken, maar door dieper te
        graven dan de zoekmachine.</p>
      <p class="body" style="margin-top:4mm;max-width:104mm">
        De straat is vernoemd naar Dirk III, graaf van West-Frisia van 993 tot 1039, in de Annalen van
        Egmond vermeld met de bijnaam <em>Hierosolymita</em> — de Jeruzalemganger. Hij bouwde een burcht
        in Vlaardingen, hief daar eigenmachtig tol op de Merwede en versloeg op 29 juli 1018 het veel
        grotere leger van keizer Hendrik II. Historici noemen hem de grondlegger van de Hollandse
        zelfstandigheid.</p>
      <p class="body" style="margin-top:4mm;max-width:104mm">
        <strong>Hiero</strong> is de eerste lettergreep van die bijnaam. En het is tegelijk gewoon
        Vlaardings voor <em>hier</em>. Een naam met twee bodems die beide waar zijn: de plek, en de
        man die hier bepaalde dat dit stukje land voor zichzelf begon.</p>
      <div class="rule acc" style="margin:7mm 0 5mm;width:70mm"></div>
      <div class="lbl acc">Aandachtspunt</div>
      <p class="small" style="margin-top:2.5mm;max-width:100mm">
        Voor de 55-plusser met overwaarde — je belangrijkste eerste verkoopfase — kan Hiero als
        straattaal landen. Dat vraagt een serieus woordmerk en het jaartal dicht bij de naam, zodat de
        herkomst meteen meeleest.</p>
    </div>
    <div style="flex:1;background:var(--acc);border-radius:2mm;position:relative;color:#fff;
      padding:14mm 12mm;display:flex;flex-direction:column;justify-content:space-between">
      <div>
        <div class="lbl on-dark">De keten</div>
        <div style="margin-top:8mm">
          <div style="font-family:var(--display);font-weight:900;font-size:30pt;line-height:1">1018</div>
          <div class="small" style="margin-top:2mm;opacity:.8">Slag bij Vlaardingen. Dirk III verslaat
            keizer Hendrik II en houdt zijn tol.</div>
        </div>
        <div style="margin-top:9mm">
          <div style="font-family:var(--display);font-weight:900;font-size:30pt;line-height:1">1967</div>
          <div class="small" style="margin-top:2mm;opacity:.8">De flat wordt gebouwd. Dertien lagen,
            136 woningen, dak op 38,4 meter.</div>
        </div>
        <div style="margin-top:9mm">
          <div style="font-family:var(--display);font-weight:900;font-size:30pt;line-height:1">2028</div>
          <div class="small" style="margin-top:2mm;opacity:.8">146 woningen, eigen VvE. Het adres wordt
            van bewoners in plaats van van passanten.</div>
        </div>
      </div>
      <div>
        <div class="rule" style="background:#fff;opacity:.3;margin-bottom:5mm"></div>
        <div style="font-family:var(--quote);font-weight:700;font-size:15pt;line-height:1.15">
          {t["belofte"]}</div>
      </div>
    </div>
  </div>
</div>'''
    return page(inner, num="02 / 17", label="De naam")

# ---------------------------------------------------------------- pagina 3: ligging

def p_ligging(t):
    feiten = [
        ("38,4 m", "dakhoogte; opbouw tot 41,2 m"),
        ("2.742 m²", "perceel met volwassen bomen"),
        ("400 ha", "Broekpolder in het noorden"),
        ("15 min", "lopen naar metro Vlaardingen West"),
        ("30 min", "naar Rotterdam Centraal"),
        ("55 + 14", "parkeerplaatsen en garageboxen"),
    ]
    cards = "".join(
        f'<div style="width:38mm"><div style="font-family:var(--display);font-weight:900;'
        f'font-size:17pt;color:var(--acc);line-height:1">{a}</div>'
        f'<div class="tiny" style="margin-top:1.6mm">{b}</div></div>' for a, b in feiten
    )
    inner = f'''
<div class="pad">
  <div style="display:flex;gap:12mm;height:100%;padding-top:14mm">
    <div style="width:104mm">
      <div class="hd" style="font-size:38pt;color:var(--acc)">De ligging<br>doet het werk</div>
      <p class="body" style="margin-top:6mm;max-width:96mm">
        Dertien lagen in een omgeving van laagbouw, met in het noorden vierhonderd hectare Broekpolder:
        tussen 1958 en 1975 opgehoogd met havenslib, afgekeurd voor woningbouw en daardoor per ongeluk
        natuurgebied geworden. Dat is in dit stukje Vlaardingen het levende bewijs dat een afgeschreven
        reputatie omkeerbaar is — en het is wat je vanaf boven ziet.</p>
      <div style="display:flex;flex-wrap:wrap;gap:6mm 8mm;margin-top:9mm">{cards}</div>
    </div>
    <div style="flex:1;display:flex;align-items:flex-start;justify-content:flex-end">
      <div style="border-radius:2mm;overflow:hidden">
        {kaart(126, ink=t["ink"], acc=t["accent"], groen=t["accent3"] if t["key"] != "bord" else "#6E8A5E",
               water=t["accent4"] if t["key"] != "1018" else "#9FC8E8", papier=t["paper"])}
      </div>
    </div>
  </div>
  <div class="tiny" style="position:absolute;left:0;bottom:9mm;opacity:.5">
    Situatieschets, niet op schaal. Ter vervanging door kaartmateriaal en dronebeeld uit fase 0.</div>
</div>'''
    return page(inner, num="03 / 17", label="Ligging")

# ---------------------------------------------------------------- pagina 4: richting

def p_richting(t):
    stalen = "".join(
        f'<div style="flex:1;height:36mm;background:{h};border-radius:1.4mm"></div>'
        for _, h, _ in t["kleuren"][:6]
    )
    inner = f'''
<div class="pad">
  <div style="padding-top:13mm;display:flex;gap:12mm">
    <div style="width:96mm">
      <div class="lbl acc">Richting {t["nr"]}</div>
      <div class="hd" style="font-size:44pt;color:var(--acc);margin-top:4mm">{t["titel"]}</div>
      <div class="hd-3" style="margin-top:5mm;opacity:.75">{t["onderkop"]}</div>
      <p class="body" style="margin-top:6mm;max-width:90mm">{t["kernidee"]}</p>
      <div class="rule" style="margin:6mm 0;width:60mm"></div>
      <div class="lbl">Houding</div>
      <p class="small" style="margin-top:2mm;max-width:88mm">{t["houding"]}</p>
    </div>
    <div style="flex:1">
      <div style="display:flex;gap:2.4mm">{stalen}</div>
      <div style="margin-top:8mm">{patroon(t, 148, 32)}</div>
      <div style="margin-top:8mm">{gebouw(148, ink=t["ink"], acc=t["accent"], lucht=t["accent4"])}</div>
    </div>
  </div>
</div>'''
    return page(inner, num="04 / 17", label="De richting")

# ---------------------------------------------------------------- pagina 5: primair logo

def p_logo(t):
    inner = f'''
<div style="position:absolute;inset:0;display:flex">
  <div style="width:50%;background:var(--acc);display:flex;align-items:center;justify-content:center">
    {logo(t, None, on_dark=True)}
  </div>
  <div style="width:50%;display:flex;align-items:center;justify-content:center">
    {logo(t)}
  </div>
</div>
<div class="lbl on-dark" style="position:absolute;left:13mm;top:12mm">Primair logo — op kleur</div>
<div class="lbl" style="position:absolute;right:13mm;top:12mm">Op basis</div>
<div class="pnum">05 / 17</div>'''
    return page(inner)

# ---------------------------------------------------------------- pagina 6: varianten

def p_varianten(t):
    cel = ("display:flex;flex-direction:column;align-items:center;justify-content:center;"
           "gap:5mm;border-radius:1.6mm;padding:8mm 6mm")
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm">
    <div class="hd-2" style="color:var(--acc)">Varianten en minimale maten</div>
    <p class="small" style="margin-top:3mm;max-width:120mm">
      Het primaire logo is de standaard. De liggende variant is voor smalle dragers, het beeldmerk voor
      social, favicon en bouwstickers. Monochroom is verplicht op foto en op het bouwhek van de aannemer.</p>
  </div>
  <div style="display:flex;gap:5mm;margin-top:9mm">
    <div style="flex:1;background:var(--paper);{cel}">
      {logo(t, 44)}<div class="lbl">Primair</div></div>
    <div style="flex:1;background:var(--acc);{cel}">
      {logo(t, 44, on_dark=True)}<div class="lbl on-dark">Op kleur</div></div>
    <div style="flex:1;background:var(--paper);{cel}">
      {mark(t, 22)}<div class="lbl">Beeldmerk</div></div>
    <div style="flex:1;background:{t["ink"]};{cel}">
      {mark_mono(t, 22)}<div class="lbl on-dark">Monochroom</div></div>
  </div>
  <div style="display:flex;gap:5mm;margin-top:5mm">
    <div style="flex:2;background:var(--paper);border-radius:1.6mm;padding:7mm 8mm">
      <div class="lbl">Liggende variant</div>
      <div style="display:flex;align-items:center;gap:5mm;margin-top:5mm">
        {mark(t, 15)}
        <div>
          <div style="font-family:var(--display);font-weight:900;font-size:23pt;color:var(--acc);
            letter-spacing:.06em;line-height:1">HIERO</div>
          <div class="tiny" style="margin-top:1.2mm;letter-spacing:.22em;text-transform:uppercase">
            Dirk de Derdelaan 167–319</div>
        </div>
      </div>
    </div>
    <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:7mm 8mm">
      <div class="lbl">Minimale maat</div>
      <div style="display:flex;align-items:flex-end;gap:6mm;margin-top:5mm">
        {mark(t, 9)}
        <div class="tiny">Beeldmerk<br>vanaf 9 mm</div>
      </div>
    </div>
    <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:7mm 8mm">
      <div class="lbl">Vrije ruimte</div>
      <div style="margin-top:4mm;border:1px dashed var(--acc);padding:4mm;display:inline-block">
        {mark(t, 12)}
      </div>
      <div class="tiny" style="margin-top:2.5mm">Rondom minimaal de hoogte van de letter H.</div>
    </div>
  </div>
</div>'''
    return page(inner, num="06 / 17", label="Logovarianten")

# ---------------------------------------------------------------- pagina 7: kleur

def p_kleur(t):
    def rgb(h):
        h = h.lstrip("#")
        return " ".join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))
    groot = t["kleuren"][0]
    rest = t["kleuren"][1:]
    cellen = "".join(
        f'<div class="sw" style="flex:1;height:64mm;background:{h}">'
        f'<div class="meta" style="background:rgba(255,255,255,.86)">'
        f'<div style="font-family:var(--body);font-weight:700;font-size:7.6pt">{n}</div>'
        f'<div class="tiny mono" style="margin-top:.8mm;opacity:.8">{h.upper()} · RGB {rgb(h)}</div>'
        f'<div class="tiny" style="margin-top:1mm;opacity:.65">{d}</div></div></div>'
        for n, h, d in rest
    )
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm;display:flex;gap:12mm;align-items:flex-end">
    <div style="flex:1">
      <div class="hd-2" style="color:var(--acc)">Kleur</div>
      <p class="small" style="margin-top:3mm;max-width:118mm">
        Eén hoofdkleur, één basis en vier steunkleuren. De verhouding is belangrijker dan het palet:
        de basis vult het vlak, de hoofdkleur markeert, de steunkleuren blijven klein. Geen goud,
        geen glans — dit gebouw wordt goed onderhouden, niet luxe.</p>
    </div>
    <div style="width:78mm">
      <div class="sw" style="height:38mm;background:{groot[1]};box-shadow:inset 0 0 0 1px rgba(0,0,0,.13)">
        <div class="meta">
          <div style="font-family:var(--body);font-weight:700;font-size:8.6pt;color:#fff">{groot[0]}</div>
          <div class="tiny mono" style="color:#fff;opacity:.85;margin-top:.8mm">
            {groot[1].upper()} · RGB {rgb(groot[1])}</div>
        </div>
      </div>
      <div class="tiny" style="margin-top:2mm">{groot[2]}</div>
    </div>
  </div>
  <div style="display:flex;gap:3mm;margin-top:9mm">{cellen}</div>
  <div style="display:flex;gap:3mm;margin-top:6mm;align-items:center">
    <div class="lbl" style="width:36mm">Verhouding</div>
    <div style="flex:1;display:flex;height:7mm;border-radius:1mm;overflow:hidden">
      <div style="flex:62;background:{t["kleuren"][1][1]}"></div>
      <div style="flex:22;background:{groot[1]}"></div>
      <div style="flex:6;background:{t["kleuren"][2][1]}"></div>
      <div style="flex:4;background:{t["kleuren"][3][1]}"></div>
      <div style="flex:4;background:{t["kleuren"][4][1]}"></div>
      <div style="flex:2;background:{t["kleuren"][5][1]}"></div>
    </div>
  </div>
</div>'''
    return page(inner, num="07 / 17", label="Kleurenpalet")

BOOMKLEUR = {"1018": "#5A6B4A", "bord": "#5F7A54", "erf": "#4C6146"}

FONTNAAM = {"Fraunces": "Fraunces", "Inter": "Inter", "Archivo": "Archivo",
            "Bricolage": "Bricolage Grotesque", "Newsreader": "Newsreader", "Karla": "Karla"}

# ---------------------------------------------------------------- pagina 8: typografie

def p_typografie(t):
    d, b, q = t["display"], t["body"], t["quote"]
    rol = {"1018": ("Koppen en getallen", "Broodtekst, labels, cijfers", "Citaten en payoff"),
           "bord": ("Koppen, borden, kapitalen", "Broodtekst en specificaties", "Payoff op borden"),
           "erf": ("Koppen en naam", "Broodtekst en labels", "Citaten, cursief tussenwerk")}[t["key"]]
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm;display:flex;gap:12mm;height:100%">
    <div style="width:120mm">
      <div class="hd-2" style="color:var(--acc)">Typografie</div>
      <div style="margin-top:8mm;background:var(--paper);border-radius:1.6mm;padding:7mm 8mm">
        <div class="lbl">{FONTNAAM[d]} — {rol[0]}</div>
        <div style="font-family:'{d}';font-weight:900;font-size:40pt;line-height:1.05;
          color:var(--acc);margin-top:3mm">Aa Bb Cc</div>
        <div style="font-family:'{d}';font-weight:400;font-size:12pt;margin-top:3mm;opacity:.8">
          1018 · 1967 · 2028 · 38,4 m · 146 woningen</div>
      </div>
      <div style="margin-top:5mm;background:var(--paper);border-radius:1.6mm;padding:7mm 8mm">
        <div class="lbl">{FONTNAAM[b]} — {rol[1]}</div>
        <div style="font-family:'{b}';font-weight:600;font-size:25pt;margin-top:3mm">Aa Bb Cc</div>
        <div style="font-family:'{b}';font-size:8.4pt;line-height:1.5;margin-top:3mm;opacity:.8;
          max-width:100mm">Twee gemeenschappelijke dakterrassen van elk 63 m², 55 parkeerplaatsen op
          eigen terrein en een plint die opengaat.</div>
      </div>
      <div style="margin-top:5mm;background:var(--paper);border-radius:1.6mm;padding:7mm 8mm">
        <div class="lbl">{FONTNAAM[q]} — {rol[2]}</div>
        <div style="font-family:'{q}';{'font-style:italic;' if q == 'Newsreader' else ''}
          font-weight:{'400' if q == 'Newsreader' else '700'};font-size:19pt;margin-top:2.5mm;
          color:var(--acc)">{t["belofte"]}</div>
      </div>
    </div>
    <div style="flex:1;border-left:1px solid rgba(0,0,0,.12);padding-left:12mm">
      <div class="lbl">Hiërarchie in gebruik</div>
      <div style="font-family:'{d}';font-weight:900;font-size:30pt;line-height:.98;color:var(--acc);
        margin-top:6mm">Dertien lagen,<br>één uitzicht</div>
      <div style="font-family:'{b}';font-weight:600;font-size:9.4pt;margin-top:5mm;line-height:1.4">
        Vanaf de bovenste lagen kijk je over de Broekpolder, de Westwijk en het Scheur.</div>
      <div style="font-family:'{b}';font-size:8.4pt;line-height:1.55;margin-top:4mm;opacity:.78">
        Het complex wordt leeg opgeleverd en van binnen vernieuwd. Wat blijft is de constructie en het
        uitzicht; de rest wordt vervangen. Er komt een eigen VvE met professioneel beheer.</div>
      <div style="margin-top:6mm;padding-top:5mm;border-top:1px solid rgba(0,0,0,.12)">
        <div class="lbl">Regels</div>
        <ul style="font-family:'{b}';font-size:7.6pt;line-height:1.6;margin:3mm 0 0;padding-left:4.5mm;
          opacity:.8">
          <li>Koppen altijd links uitgelijnd, nooit gecentreerd behalve in het logo.</li>
          <li>Getallen in de displayletter: hoogte, jaartal en aantal zijn het verhaal.</li>
          <li>Labels in kapitalen met ruime letterafstand, maximaal vier woorden.</li>
          <li>Broodtekst nooit onder 8 pt in print, nooit over volle breedte.</li>
        </ul>
      </div>
    </div>
  </div>
</div>'''
    return page(inner, num="08 / 17", label="Typografie")

# ---------------------------------------------------------------- pagina 9: motief

def p_motief(t):
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm;display:flex;gap:12mm;align-items:stretch">
    <div style="width:96mm">
      <div class="hd-2" style="color:var(--acc)">{t["motiefnaam"]}</div>
      <p class="body" style="margin-top:5mm;max-width:90mm">{t["motieftekst"]}</p>
      <div class="rule" style="margin:6mm 0;width:56mm"></div>
      <div class="lbl">Toepassing</div>
      <p class="small" style="margin-top:2.5mm;max-width:88mm">
        Het motief is nooit decoratie. Het markeert een overgang: de kop van een pagina, de rand van
        een bord, de onderkant van een banner. Maximaal één keer per drager.</p>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;gap:4mm;height:158mm">
      <div style="background:var(--paper);border-radius:1.6mm;padding:6mm;flex:1;
        display:flex;align-items:center;overflow:hidden">{patroon(t, None, 30)}</div>
      <div style="background:var(--acc);border-radius:1.6mm;padding:6mm;flex:1;
        display:flex;align-items:center;overflow:hidden">
        <div style="filter:brightness(0) invert(1);opacity:.9;width:100%">{patroon(t, None, 30)}</div>
      </div>
      <div style="display:flex;gap:4mm;flex:1.15">
        <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:5mm;
          display:flex;align-items:center;justify-content:center">
          {bomenrij(52, kleur=BOOMKLEUR[t["key"]])}</div>
        <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:5mm;
          display:flex;align-items:center">
          {gebouw(60, ink=t["ink"], acc=t["accent"], nummers=True)}</div>
      </div>
    </div>
  </div>
</div>'''
    return page(inner, num="09 / 17", label="Grafisch element")

# ---------------------------------------------------------------- pagina 10: toon

def p_toon(t):
    kern = "".join(
        f'<div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:7mm 6mm">'
        f'<div style="font-family:var(--display);font-weight:700;font-size:12.5pt;color:var(--acc);'
        f'line-height:1.15">{a}</div>'
        f'<div class="small" style="margin-top:3mm">{b}</div></div>'
        for a, b in t["boodschappen"]
    )
    wel = "".join(f'<li>{x}</li>' for x in t["wel"])
    niet = "".join(f'<li>{x}</li>' for x in t["niet"])
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm">
    <div class="hd-2" style="color:var(--acc)">Toon en kernboodschap</div>
    <p class="small" style="margin-top:3mm;max-width:126mm">
      De doelgroep vraagt zich niet af of dit mooi is, maar of het klopt. Elke regel moet een feit
      dragen of een afspraak. De grootste angst is niet de prijs of de plattegrond, maar: wie zijn
      straks mijn buren, en wie zorgt hiervoor?</p>
  </div>
  <div style="display:flex;gap:4mm;margin-top:8mm">{kern}</div>
  <div style="display:flex;gap:4mm;margin-top:5mm">
    <div style="flex:1;background:var(--acc);color:#fff;border-radius:1.6mm;padding:7mm 6mm">
      <div class="lbl on-dark">Wel</div>
      <ul style="font-size:8pt;line-height:1.7;margin:3mm 0 0;padding-left:4.5mm">{wel}</ul>
    </div>
    <div style="flex:1;border:1px solid rgba(0,0,0,.16);border-radius:1.6mm;padding:7mm 6mm">
      <div class="lbl">Niet</div>
      <ul style="font-size:8pt;line-height:1.7;margin:3mm 0 0;padding-left:4.5mm;opacity:.75">{niet}</ul>
    </div>
    <div style="flex:1.3;background:var(--paper);border-radius:1.6mm;padding:7mm 6mm">
      <div class="lbl">Voorbeeldregels</div>
      <div style="font-family:var(--quote);font-weight:{'400' if t["quote"] == 'Newsreader' else '700'};
        {'font-style:italic;' if t["quote"] == 'Newsreader' else ''}font-size:12pt;line-height:1.3;
        color:var(--acc);margin-top:4mm">“{t["belofte"]}”</div>
      <div class="small" style="margin-top:4mm">“Leeg in 2027. Vernieuwd in 2028. Van bewoners vanaf dag één.”</div>
      <div class="small" style="margin-top:2.5mm">“Kom kijken vóór het klaar is. Neem een helm mee.”</div>
      <div class="small" style="margin-top:2.5mm">“Dertien hoog, 52 m², eigen VvE. Reken zelf mee.”</div>
    </div>
  </div>
</div>'''
    return page(inner, num="10 / 17", label="Toon of voice")

# ---------------------------------------------------------------- pagina 11: bouwhek

def p_bouwhek(t):
    k = t["key"]
    if k == "bord":
        hek = f'''<div style="background:{t["accent"]};height:62mm;position:relative;
          display:flex;align-items:center;padding:0 12mm;gap:12mm">
          {logo_bord(70, blue="#F2F1EC", white=t["accent"])}
          <div style="color:#fff">
            <div style="font-family:'Archivo';font-weight:900;font-size:20pt;line-height:1.05">
              HIER KOMEN 146 WONINGEN</div>
            <div style="font-family:var(--body);font-size:9pt;margin-top:2.5mm;opacity:.85">
              Dirk de Derdelaan 167–319 · verkoop vanaf H2 2028 · hiero.nl</div>
          </div>
          <div style="position:absolute;right:0;top:0;bottom:0;width:26mm;
            background:{t["accent2"]};display:flex;align-items:center;justify-content:center">
            <div style="font-family:'Archivo';font-weight:900;font-size:15pt;color:#fff;
              transform:rotate(-90deg);white-space:nowrap">SCHRIJF JE IN</div></div>
        </div>'''
    elif k == "erf":
        hek = f'''<div style="background:{t["accent"]};height:62mm;position:relative;
          display:flex;align-items:center;padding:0 12mm;gap:10mm;overflow:hidden">
          {logo_erf(34, fill="#F4EDE2", ink_on=t["accent"], sub=False)}
          <div style="color:#fff;z-index:2">
            <div style="font-family:'Bricolage';font-weight:800;font-size:20pt;line-height:1.05">
              Hier komt het erf</div>
            <div style="font-family:'Newsreader';font-style:italic;font-size:12pt;margin-top:2mm;
              opacity:.9">146 woningen, 2.742 m² met de bomen die er al staan</div>
            <div style="font-family:var(--body);font-size:8.4pt;margin-top:2.5mm;opacity:.8">
              hiero.nl · verkoop vanaf H2 2028</div>
          </div>
          <div style="position:absolute;right:-6mm;bottom:-4mm;opacity:.3">
            {bomenrij(60, kleur="#F4EDE2", n=5)}</div>
        </div>'''
    else:
        hek = f'''<div style="background:{t["accent"]};height:62mm;position:relative;
          display:flex;align-items:center;padding:0 12mm;gap:12mm;overflow:hidden">
          <div style="position:absolute;left:0;top:0;right:0;height:8mm;opacity:.35">
            {patroon(t, 260, 8)}</div>
          {logo_1018(36, fill="#EFE6D6", ink_on=t["accent"], tag=False)}
          <div style="color:#fff">
            <div style="font-family:'Fraunces';font-weight:900;font-size:21pt;line-height:1.03">
              Hier begon Holland<br>voor zichzelf</div>
            <div style="font-family:var(--body);font-size:8.6pt;margin-top:2.5mm;opacity:.85">
              146 woningen aan de Dirk de Derdelaan · hiero.nl</div>
          </div>
          <div style="position:absolute;right:12mm;bottom:8mm;font-family:'Fraunces';font-weight:900;
            font-size:34pt;color:#fff;opacity:.28">1018</div>
        </div>'''
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm">
    <div class="hd-2" style="color:var(--acc)">Bouwhek</div>
    <p class="small" style="margin-top:3mm;max-width:126mm">
      Dagelijks zichtbaar voor de hele wijk en gratis. Dit is het enige middel dat de reputatie
      aanspreekt op de plek waar hij is ontstaan, dus hier staat het adres voluit — niet verstopt.</p>
  </div>
  <div style="margin-top:8mm;border-radius:1.4mm;overflow:hidden">{hek}</div>
  <div style="display:flex;gap:4mm;margin-top:5mm;height:58mm">
    <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:6mm">
      <div class="lbl">Losse panelen</div>
      <div style="display:flex;gap:2.5mm;margin-top:4mm">
        <div style="flex:1;aspect-ratio:1/1.1;background:var(--acc);border-radius:1mm;
          display:flex;align-items:center;justify-content:center">{mark(t, 14, on_dark=True)}</div>
        <div style="flex:1;aspect-ratio:1/1.1;background:{t["accent2"]};border-radius:1mm;
          display:flex;align-items:flex-end;padding:3mm">
          <div style="font-family:var(--display);font-weight:900;font-size:11pt;color:#fff;
            line-height:1.05">146<br>woningen</div></div>
        <div style="flex:1;aspect-ratio:1/1.1;background:var(--acc4);border-radius:1mm;
          display:flex;align-items:flex-end;padding:3mm">
          <div style="font-family:var(--display);font-weight:900;font-size:11pt;color:var(--ink);
            line-height:1.05">38,4<br>meter</div></div>
      </div>
    </div>
    <div style="flex:2;background:var(--paper);border-radius:1.6mm;padding:6mm">
      <div class="lbl">Waarom dit werkt</div>
      <p class="small" style="margin-top:3mm">
        Wie het adres verzwijgt, geeft de reputatie het laatste woord. Op het bouwhek staat daarom het
        volledige adres, het aantal woningen en één plek om je in te schrijven. De e-maillijst is
        volgens het marketingplan de belangrijkste asset van de hele aanloop; het hek is de goedkoopste
        manier om die te vullen.</p>
    </div>
  </div>
</div>'''
    return page(inner, num="11 / 17", label="Toepassing — bouwhek")

# ---------------------------------------------------------------- pagina 12: gevel

def p_gevel(t):
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm;display:flex;gap:12mm">
    <div style="width:88mm">
      <div class="hd-2" style="color:var(--acc)">Gevelbanner</div>
      <p class="body" style="margin-top:5mm;max-width:84mm">
        Achtendertig meter zichtbaarheid vanuit de hele wijk, dagelijks, zonder mediabudget. De banner
        hangt over de volle hoogte en doet één ding: de naam en het jaar van oplevering. Op deze afstand
        leest niemand een zin.</p>
      <div class="rule" style="margin:6mm 0;width:52mm"></div>
      <div class="lbl">Specificatie</div>
      <table style="margin-top:3mm">
        <tr><td style="width:32mm;opacity:.6">Formaat</td><td>ca. 4 × 24 m, geperforeerd gaasdoek</td></tr>
        <tr><td style="opacity:.6">Inhoud</td><td>beeldmerk, naam, jaartal, domein</td></tr>
        <tr><td style="opacity:.6">Kleur</td><td>hoofdkleur vol, tekst in basis</td></tr>
        <tr><td style="opacity:.6">Fase</td><td>vanaf start werkzaamheden Q1 2027</td></tr>
      </table>
    </div>
    <div style="flex:1;position:relative;display:flex;align-items:flex-start;justify-content:center;
      padding-top:2mm">
      <div style="position:relative;width:142mm">
        {gebouw(142, ink=t["ink"], acc=t["accent"], lucht=t["accent4"])}
        <div style="position:absolute;left:42%;top:6.5%;width:13mm;height:76%;background:var(--acc);
          display:flex;flex-direction:column;align-items:center;justify-content:space-between;
          padding:3mm 0;border-radius:.6mm">
          <div style="font-family:var(--display);font-weight:900;font-size:12pt;color:#fff;
            writing-mode:vertical-rl;letter-spacing:.22em">HIERO</div>
          <div style="font-family:var(--body);font-weight:600;font-size:6.4pt;color:#fff;opacity:.85;
            writing-mode:vertical-rl;letter-spacing:.18em">2028</div>
        </div>
      </div>
    </div>
  </div>
  <div class="tiny" style="position:absolute;left:0;bottom:9mm;opacity:.5">
    Schematische weergave van de bestaande gevelopbouw: twaalf woonlagen met doorlopende balkons,
    toplaag, en de nieuwe plint met commerciële ruimte.</div>
</div>'''
    return page(inner, num="12 / 17", label="Toepassing — gevel")

# ---------------------------------------------------------------- pagina 13: projectpagina

def p_web(t):
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm">
    <div class="hd-2" style="color:var(--acc)">Projectpagina</div>
    <p class="small" style="margin-top:3mm;max-width:126mm">
      De pagina moet vanaf fase 0 geïndexeerd staan, zodat het eigen zoekresultaat er al is voordat
      iemand de reputatie tegenkomt. Eén doel boven de vouw: inschrijven op de lijst.</p>
  </div>
  <div style="margin-top:7mm;background:var(--paper);border-radius:2mm;overflow:hidden;
    border:1px solid rgba(0,0,0,.1)">
    <div style="height:7mm;background:rgba(0,0,0,.06);display:flex;align-items:center;padding:0 4mm;gap:2mm">
      <div style="width:2mm;height:2mm;border-radius:9mm;background:rgba(0,0,0,.2)"></div>
      <div style="width:2mm;height:2mm;border-radius:9mm;background:rgba(0,0,0,.2)"></div>
      <div style="width:2mm;height:2mm;border-radius:9mm;background:rgba(0,0,0,.2)"></div>
      <div style="margin-left:4mm;background:#fff;border-radius:9mm;padding:.8mm 4mm;
        font-family:var(--body);font-size:6pt;opacity:.6">hiero.nl</div>
    </div>
    <div style="background:var(--acc);padding:6mm 8mm;display:flex;align-items:center;
      justify-content:space-between">
      <div style="display:flex;align-items:center;gap:4mm">
        {mark(t, 9, on_dark=True)}
        <div style="font-family:var(--display);font-weight:900;font-size:11pt;color:#fff;
          letter-spacing:.08em">HIERO</div>
      </div>
      <div style="display:flex;gap:6mm;font-family:var(--body);font-size:7pt;color:#fff;opacity:.85">
        <div>Het gebouw</div><div>De verbouwing</div><div>Uitzicht</div><div>Woningen</div>
        <div style="background:#fff;color:var(--acc);border-radius:9mm;padding:1mm 3.4mm;
          font-weight:600;opacity:1">Inschrijven</div>
      </div>
    </div>
    <div style="display:flex">
      <div style="width:56%;padding:10mm 8mm 9mm">
        <div style="font-family:var(--display);font-weight:900;font-size:26pt;line-height:1;
          color:var(--acc)">146 woningen<br>op 38 meter</div>
        <div class="small" style="margin-top:4mm;max-width:78mm">
          Aan de Dirk de Derdelaan wordt een gebouw uit 1967 leeg opgeleverd, van binnen vernieuwd en
          uitgebreid met tien woningen. Verkoop vanaf de tweede helft van 2028.</div>
        <div style="display:flex;gap:3mm;margin-top:6mm;align-items:center">
          <div style="background:var(--acc);color:#fff;border-radius:1mm;padding:2.6mm 6mm;
            font-family:var(--body);font-weight:600;font-size:7.6pt">Zet mij op de lijst</div>
          <div style="font-family:var(--body);font-size:7pt;opacity:.6">1.500 mensen volgen dit project</div>
        </div>
      </div>
      <div style="width:44%;background:{t["accent4"]};position:relative;display:flex;
        align-items:flex-end;overflow:hidden">
        <div style="width:100%">{gebouw(112, ink=t["ink"], acc=t["accent"])}</div>
      </div>
    </div>
    <div style="display:flex;gap:0;border-top:1px solid rgba(0,0,0,.1)">
      <div style="flex:1;padding:6mm 7mm">
        <div class="lbl">Deze week</div>
        <div class="small" style="margin-top:2mm">Het uitzicht vanaf de elfde, richting de Broekpolder.</div>
      </div>
      <div style="flex:1;padding:6mm 7mm;border-left:1px solid rgba(0,0,0,.1)">
        <div class="lbl">Uitzichtviewer</div>
        <div class="small" style="margin-top:2mm">Kies verdieping en windrichting, zie wat je ziet.</div>
      </div>
      <div style="flex:1;padding:6mm 7mm;border-left:1px solid rgba(0,0,0,.1)">
        <div class="lbl">Maandlasten</div>
        <div class="small" style="margin-top:2mm">Hypotheek, VvE-bijdrage en energie in één bedrag.</div>
      </div>
    </div>
  </div>
</div>'''
    return page(inner, num="13 / 17", label="Toepassing — online")

# ---------------------------------------------------------------- pagina 14: social

def p_social(t):
    q_it = 'font-style:italic;' if t["quote"] == "Newsreader" else ""
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm">
    <div class="hd-2" style="color:var(--acc)">Social</div>
    <p class="small" style="margin-top:3mm;max-width:126mm">
      Drie vaste stromen uit het marketingplan: de transformatie, het uitzicht, en het gebouw uit 1967.
      Elke tegel is herkenbaar aan één ding — de kleur, het beeldmerk of het getal. Nooit alle drie.</p>
  </div>
  <div style="display:flex;gap:5mm;margin-top:8mm">
    <div style="flex:1;aspect-ratio:1;background:var(--acc);border-radius:1.6mm;padding:7mm;
      display:flex;flex-direction:column;justify-content:space-between;color:#fff">
      <div class="lbl on-dark">De transformatie</div>
      <div>
        <div style="font-family:var(--display);font-weight:900;font-size:22pt;line-height:1">
          Alles eruit.<br>Alles opnieuw.</div>
        <div class="tiny" style="margin-top:3mm;opacity:.8">Week 34 · gestript casco, achtste verdieping</div>
      </div>
      {mark(t, 11, on_dark=True)}
    </div>
    <div style="flex:1;aspect-ratio:1;background:{t["accent4"]};border-radius:1.6mm;padding:7mm;
      display:flex;flex-direction:column;justify-content:space-between">
      <div class="lbl">Het uitzicht</div>
      <div style="font-family:var(--quote);{q_it}font-weight:{'400' if t["quote"] == 'Newsreader' else '700'};
        font-size:17pt;line-height:1.15;color:var(--ink)">
        Vanaf de elfde zie je de mist over de Broekpolder liggen.</div>
      <div class="tiny" style="opacity:.7">hiero.nl · elke week één beeld van boven</div>
    </div>
    <div style="flex:1;aspect-ratio:1;background:var(--paper);border-radius:1.6mm;padding:7mm;
      display:flex;flex-direction:column;justify-content:space-between;
      border:1px solid rgba(0,0,0,.1)">
      <div class="lbl">1967</div>
      <div style="font-family:var(--display);font-weight:900;font-size:44pt;color:var(--acc);
        line-height:.9">1967</div>
      <div class="small">Dertien lagen, 136 woningen, dak op 38,4 meter. Het bouwarchief van
        naoorlogs Vlaardingen.</div>
    </div>
  </div>
  <div style="display:flex;gap:5mm;margin-top:5mm">
    <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:5mm 6mm">
      <div class="lbl">Cadans</div>
      <div class="small" style="margin-top:2mm">Wekelijks transformatie en uitzicht, maandelijks archief.</div>
    </div>
    <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:5mm 6mm">
      <div class="lbl">Doel</div>
      <div class="small" style="margin-top:2mm">Alles leidt naar één actie: inschrijven op de lijst.</div>
    </div>
    <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:5mm 6mm">
      <div class="lbl">Verbod</div>
      <div class="small" style="margin-top:2mm">Geen sfeerbeeld dat niet op deze plek is gemaakt.</div>
    </div>
  </div>
</div>'''
    return page(inner, num="14 / 17", label="Toepassing — social")

# ---------------------------------------------------------------- pagina 15: drukwerk

def p_drukwerk(t):
    inner = f'''
<div class="pad">
  <div style="padding-top:12mm">
    <div class="hd-2" style="color:var(--acc)">Drukwerk</div>
    <p class="small" style="margin-top:3mm;max-width:126mm">
      Brochure, briefpapier en kaartje. Bij oplevering ligt hier ook het VvE-dossier in dezelfde stijl:
      beheer dat er verzorgd uitziet is in dit project een verkoopargument, niet een formaliteit.</p>
  </div>
  <div style="display:flex;gap:6mm;margin-top:8mm;align-items:flex-start">
    <div style="width:72mm;aspect-ratio:1/1.414;background:var(--acc);border-radius:1.2mm;
      padding:8mm 7mm;display:flex;flex-direction:column;justify-content:space-between;color:#fff">
      <div class="lbl on-dark">Brochure</div>
      <div style="display:flex;justify-content:center">{logo(t, 34, on_dark=True)}</div>
      <div>
        <div style="font-family:var(--display);font-weight:900;font-size:15pt;line-height:1.05">
          146 woningen<br>aan de Dirk<br>de Derdelaan</div>
        <div class="tiny" style="margin-top:3mm;opacity:.8">Vlaardingen-Westwijk · H2 2028</div>
      </div>
    </div>
    <div style="width:72mm;aspect-ratio:1/1.414;background:var(--paper);border-radius:1.2mm;
      padding:8mm 7mm;display:flex;flex-direction:column;border:1px solid rgba(0,0,0,.1)">
      <div style="display:flex;justify-content:space-between;align-items:flex-start">
        {mark(t, 11)}
        <div class="tiny" style="text-align:right;opacity:.6;line-height:1.5">
          hiero.nl<br>Dirk de Derdelaan 167–319<br>3132 Vlaardingen</div>
      </div>
      <div style="margin-top:12mm">
        <div class="tiny" style="opacity:.75">Vlaardingen, 12 maart 2027</div>
        <div style="font-family:var(--display);font-weight:700;font-size:10pt;margin-top:5mm;
          color:var(--acc)">Uitnodiging uitzichtbezoek</div>
        <div class="tiny" style="margin-top:3mm;line-height:1.7;opacity:.7">
          Beste mevrouw De Wit,<br><br>
          Op zaterdag 3 april zetten we de lift aan tot de elfde verdieping. De woning is nog
          gestript en er ligt geen vloer, dus stevige schoenen zijn geen slecht idee.<br><br>
          U bent welkom tussen tien en twaalf.</div>
      </div>
      <div style="margin-top:auto;padding-top:6mm">
        <div style="height:1px;background:rgba(0,0,0,.12)"></div>
        <div class="tiny" style="margin-top:2.5mm;opacity:.5">
          Hiero is een ontwikkeling aan de Dirk de Derdelaan 167–319, Vlaardingen.</div>
      </div>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;gap:5mm">
      <div style="background:var(--acc);border-radius:1.2mm;padding:6mm;aspect-ratio:1.75/1;
        display:flex;flex-direction:column;justify-content:space-between;color:#fff">
        <div style="display:flex;justify-content:space-between;align-items:flex-start">
          {mark(t, 9, on_dark=True)}
          <div class="tiny" style="opacity:.75;text-align:right">hiero.nl</div>
        </div>
        <div>
          <div style="font-family:var(--body);font-weight:600;font-size:8.4pt">Emily van Duijnhoven</div>
          <div class="tiny" style="opacity:.8;margin-top:.8mm">Marketing en positionering</div>
        </div>
      </div>
      <div style="background:var(--paper);border-radius:1.2mm;padding:6mm;flex:1">
        <div class="lbl">Papier en afwerking</div>
        <table style="margin-top:3mm">
          <tr><td style="width:26mm;opacity:.6">Brochure</td><td>ongestreken, 140 g, mat</td></tr>
          <tr><td style="opacity:.6">Brief</td><td>ongestreken, 120 g</td></tr>
          <tr><td style="opacity:.6">Kaartje</td><td>400 g, gekleurde kern</td></tr>
          <tr><td style="opacity:.6">Verbod</td><td>geen glans, geen folie, geen reliëf</td></tr>
        </table>
      </div>
    </div>
  </div>
</div>'''
    return page(inner, num="15 / 17", label="Toepassing — drukwerk")

# ---------------------------------------------------------------- pagina 16: overzicht

def p_overzicht(t):
    stalen = "".join(f'<div style="flex:1;height:14mm;background:{h}"></div>' for _, h, _ in t["kleuren"])
    inner = f'''
<div class="pad-s">
  <div style="position:absolute;left:4mm;top:3mm" class="lbl">De richting in één beeld</div>
  <div style="position:absolute;inset:0;padding:12mm 4mm 4mm;display:flex;gap:5mm">
    <div style="width:78mm;display:flex;flex-direction:column;gap:5mm">
      <div style="background:var(--acc);border-radius:1.6mm;flex:1;display:flex;align-items:center;
        justify-content:center">{logo(t, 44, on_dark=True)}</div>
      <div style="display:flex;gap:0;border-radius:1.2mm;overflow:hidden">{stalen}</div>
      <div style="background:var(--paper);border-radius:1.6mm;padding:5mm 6mm">
        <div style="font-family:var(--quote);
          {'font-style:italic;' if t["quote"] == 'Newsreader' else ''}
          font-weight:{'400' if t["quote"] == 'Newsreader' else '700'};font-size:13pt;
          color:var(--acc);line-height:1.2">{t["belofte"]}</div>
      </div>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;gap:5mm">
      <div style="display:flex;gap:5mm;flex:1">
        <div style="flex:1;background:var(--paper);border-radius:1.6mm;padding:5mm;
          display:flex;align-items:center;overflow:hidden">{patroon(t, None, 26)}</div>
        <div style="width:36mm;background:{t["accent4"]};border-radius:1.6mm;
          display:flex;align-items:center;justify-content:center">{mark(t, 16)}</div>
      </div>
      <div style="background:var(--paper);border-radius:1.6mm;padding:5mm 6mm">
        {gebouw(122, ink=t["ink"], acc=t["accent"], nummers=True)}</div>
      <div style="display:flex;gap:5mm">
        <div style="flex:1;background:var(--acc);color:#fff;border-radius:1.6mm;padding:5mm 6mm">
          <div class="lbl on-dark">Kernidee</div>
          <div class="tiny" style="margin-top:2mm;opacity:.9">{t["kernidee"][:186]}…</div>
        </div>
        <div style="width:52mm;background:var(--paper);border-radius:1.6mm;padding:5mm 6mm">
          <div class="lbl">Typografie</div>
          <div style="font-family:'{t["display"]}';font-weight:900;font-size:15pt;margin-top:2mm;
            color:var(--acc)">Aa Bb Cc</div>
          <div class="tiny" style="margin-top:1.5mm">{FONTNAAM[t["display"]]} + {FONTNAAM[t["body"]]}</div>
        </div>
      </div>
    </div>
  </div>
  <div class="pnum">16 / 17</div>
</div>'''
    return page(inner)

# ---------------------------------------------------------------- pagina 17: verantwoording

def p_slot(t):
    inner = f'''
<div class="pad">
  <div style="padding-top:14mm;display:flex;gap:12mm">
    <div style="width:104mm">
      <div class="hd-2" style="color:var(--acc)">Verantwoording</div>
      <div class="lbl" style="margin-top:8mm">Wat vaststaat</div>
      <p class="small" style="margin-top:2.5mm;max-width:96mm">
        Bouwjaar 1967, dertien bouwlagen, dak op 38,4 meter, 136 bestaande woningen, uitbreiding met
        acht woningen in de plint en twee op de toplaag, twee dakterrassen van 63 m², circa 125 m²
        commerciële ruimte, twee entreehallen van 92 m², perceel van 2.742 m², 55 parkeerplaatsen en
        veertien garageboxen. Planning: vergunning Q4 2026, start Q1 2027, verkoop en levering H2 2028.</p>
      <div class="lbl" style="margin-top:6mm">Wat aanname is</div>
      <p class="small" style="margin-top:2.5mm;max-width:96mm">
        De naam Hiero is een voorstel, niet een besluit. De VvE met professioneel beheer en de
        verdeling koop–huur staan in de aangeleverde stukken als aanname. Prijzen, woningaantallen per
        type en de renovatiediepte zijn nog niet vastgesteld; die bepalen of we “vernieuwd” of “als
        nieuw” mogen zeggen.</p>
      <div class="lbl" style="margin-top:6mm">Beeld</div>
      <p class="small" style="margin-top:2.5mm;max-width:96mm">
        Alle illustraties in dit document zijn vector en zelf getekend. Er is nog geen projectfotografie:
        nulfotografie en dronebeeld vanaf elke verdieping staan in fase 0 van het marketingplan. Zodra
        die er zijn, vervangen ze de schematische vlakken in dit boek. Er is bewust geen stockbeeld
        gebruikt.</p>
      <div class="lbl" style="margin-top:6mm">Typografie</div>
      <p class="small" style="margin-top:2.5mm;max-width:96mm">
        {FONTNAAM[t["display"]]}, {FONTNAAM[t["body"]]} en {FONTNAAM[t["quote"]]} zijn opengelicentieerde
        letterfamilies (SIL Open Font License) en vrij te gebruiken in druk en online. Bij definitieve
        keuze kan een licentieletter met eigen karakter worden overwogen.</p>
    </div>
    <div style="flex:1;background:var(--acc);color:#fff;border-radius:2mm;padding:12mm 10mm;
      display:flex;flex-direction:column;justify-content:space-between">
      <div>
        <div class="lbl on-dark">Herkomst van de naam</div>
        <p class="tiny" style="margin-top:3mm;opacity:.9;line-height:1.65">
          Dirk III, graaf van West-Frisia 993–1039, in de twaalfde-eeuwse Annalen van Egmond vermeld met
          de bijnaam Hierosolymita. Burcht in Vlaardingen, vermoedelijk op de plek van de huidige Grote Kerk, tol op de
          Merwede, en op 29 juli 1018 de overwinning op keizer Hendrik II.</p>
        <p class="tiny" style="margin-top:4mm;opacity:.9;line-height:1.65">
          Bronnen: Canon van Nederland (Slag bij Vlaardingen, Broekpolder), Historische Vereniging
          Vlaardingen, Wikipedia (Dirk III, Slag bij Vlaardingen 1018, Westwijk, Broekpolder),
          gemeentelijke straatnaamherkomst Westwijk.</p>
      </div>
      <div>
        <div style="display:flex;justify-content:center;margin-bottom:8mm">{logo(t, 34, on_dark=True)}</div>
        <div class="rule" style="background:#fff;opacity:.3"></div>
        <p class="tiny" style="margin-top:4mm;opacity:.75;line-height:1.6">
          Dit conceptboek is één van drie richtingen voor dezelfde naam. Het is een voorstel ter
          bespreking; niets erin is definitief vastgesteld.</p>
      </div>
    </div>
  </div>
</div>'''
    return page(inner, num="17 / 17", label="Verantwoording")

# ---------------------------------------------------------------- bouwen

BUILDERS = [p_cover, p_naam, p_ligging, p_richting, p_logo, p_varianten, p_kleur,
            p_typografie, p_motief, p_toon, p_bouwhek, p_gevel, p_web, p_social,
            p_drukwerk, p_overzicht, p_slot]

def build(key):
    t = THEMES[key]
    pages = "".join(fn(t) for fn in BUILDERS)
    html = ("<!doctype html><html lang=\"nl\"><head><meta charset=\"utf-8\">"
            "<title>Hiero — huisstijlvoorstel %s</title><style>%s%s%s</style></head><body>%s</body></html>"
            % (t["titel"], FONT_CSS, theme_css(t), BASE_CSS, pages))
    hp = os.path.join(OUT, "hiero-%s-%s.html" % (t["nr"], key))
    open(hp, "w").write(html)
    return hp, t

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def to_pdf(hp, pdf):
    cmd = [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
           "--run-all-compositor-stages-before-draw", "--virtual-time-budget=12000",
           "--print-to-pdf=" + pdf, "file://" + hp]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    if not os.path.exists(pdf):
        sys.stderr.write(r.stdout + r.stderr)
        raise SystemExit("print mislukt voor " + hp)

if __name__ == "__main__":
    for key in ("1018", "bord", "erf"):
        hp, t = build(key)
        naam = "Hiero - huisstijl %s - %s.pdf" % (t["nr"], t["titel"])
        pdf = os.path.join(OUT, naam)
        to_pdf(hp, pdf)
        print("%-28s %8.0f kB" % (naam, os.path.getsize(pdf) / 1024))
