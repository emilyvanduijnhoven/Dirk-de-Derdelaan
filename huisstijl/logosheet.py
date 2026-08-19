#!/usr/bin/env python3
"""Bouwt de logo-uitwerking voor HIERO: een PDF van 11 liggende pagina's plus
losse SVG-bestanden met de letters als outlines (geen letterlicentie nodig)."""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import logo as G

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
LOGODIR = os.path.join(HERE, "logo")
os.makedirs(LOGODIR, exist_ok=True)

L = G.Letters("Outfit-800.ttf")
PAL = G.PALETTEN["schemer"]
SCHETS = {"ink": "#2E6B4F", "sun": "#F2E27A", "water": "#A8C4E5", "bg": "#FFFFFF"}

def face(fam, w, st, fn):
    return ("@font-face{font-family:'%s';font-weight:%s;font-style:%s;"
            "src:url('file://%s/%s') format('truetype');font-display:block}" % (fam, w, st, FONTS, fn))

FONT_CSS = "".join([face("Inter", w, "normal", "Inter-%d.ttf" % w) for w in (400, 500, 600, 700)] +
                   [face("Outfit", 800, "normal", "Outfit-800.ttf")])

CSS = """
@page{size:280mm 210mm;margin:0}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:Inter,sans-serif;color:#1C2C46}
.page{width:280mm;height:210mm;position:relative;overflow:hidden;background:#F4F1EA;
  page-break-after:always;break-after:page}
.page:last-child{page-break-after:auto}
.pad{position:absolute;inset:13mm}
.lbl{font-weight:600;font-size:6.1pt;letter-spacing:.3em;text-transform:uppercase;opacity:.5}
.lbl.w{color:#fff;opacity:.65}
h2{margin:0;font-family:Outfit;font-weight:800;font-size:22pt;line-height:1.04;letter-spacing:-.01em}
.body{font-size:8.6pt;line-height:1.55}
.small{font-size:7.4pt;line-height:1.5;opacity:.75}
.tiny{font-size:6.3pt;line-height:1.45;opacity:.62}
.card{background:#FBF9F4;border-radius:1.6mm;padding:6mm}
.pnum{position:absolute;right:13mm;bottom:11mm;font-size:6.4pt;letter-spacing:.22em;opacity:.45}
.foot{position:absolute;left:13mm;bottom:11mm;font-size:6.4pt;letter-spacing:.28em;
  text-transform:uppercase;opacity:.45}
table{border-collapse:collapse;width:100%}
td{font-size:7.5pt;padding:2mm 0;vertical-align:top}
tr+tr td{border-top:1px solid rgba(0,0,0,.09)}
.kruis{position:relative}
.kruis:after{content:"";position:absolute;left:8%;right:8%;top:50%;height:1.1px;background:#C0392B;
  transform:rotate(-9deg)}
"""

def page(inner, num=None, label=None, bg=None):
    st = ' style="background:%s"' % bg if bg else ""
    lb = '<div class="lbl%s" style="position:absolute;left:13mm;top:12mm">%s</div>' % (
        " w" if bg else "", label) if label else ""
    ft = ""
    if num:
        c = "#fff" if bg else "#1C2C46"
        ft = ('<div class="foot" style="color:%s">Hiero · logo-uitwerking</div>'
              '<div class="pnum" style="color:%s">%s</div>' % (c, c, num))
    return '<section class="page"%s>%s%s%s</section>' % (st, lb, inner, ft)

def lk(pal=None, w=120, **kw):
    pal = pal or PAL
    b, vb = G.lockup(L, pal, **kw)
    return G.inline(b, vb, w)

def mk(pal=None, w=20, **kw):
    pal = pal or PAL
    b, vb = G.merk(L, pal, **kw)
    return G.inline(b, vb, w)

# ---------------------------------------------------------------- 1 omslag

def p1():
    inner = '''
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">%s</div>
<div class="pad">
  <div class="lbl">Logo-uitwerking — Hiero</div>
  <div style="position:absolute;left:0;bottom:0">
    <div style="font-weight:600;font-size:9.4pt">Dakcontour en de O als zonsondergang</div>
    <div class="tiny" style="margin-top:1.6mm">Dirk de Derdelaan 167–319, Vlaardingen · augustus 2026</div>
  </div>
  <div style="position:absolute;right:0;bottom:0;text-align:right" class="tiny">
    Vier varianten van de O · drie boogvormen · vier paletten</div>
</div>''' % lk(w=176)
    return page(inner)

# ---------------------------------------------------------------- 2 wat er strakker is

def p2():
    schets = lk(pal=SCHETS, w=112, variant="B", rise=0.40, uid="sk")
    nieuw = lk(w=112, uid="nw")
    punten = [
        ("De boog is nu een echte cirkelboog",
         "In de schets loopt de lijn taps toe en zijn de uiteinden ongelijk. Nu is het een segment van "
         "één cirkel met constante lijndikte, dus hij blijft kloppen op elk formaat."),
        ("De O is op het letterraster gezet",
         "Diameter is 1,03 × de kapitaalhoogte, met overschot boven en onder zoals elke ronde letter. "
         "De ring is 0,60 × de letterstam: lichter dan de letters, waardoor de O een venster wordt."),
        ("De zon en het water liggen op één ritme",
         "Horizon, zon en reflectie zijn allemaal afgeleid van de binnenradius. Geen losse maten meer."),
        ("De onderkant sluit op de basislijn",
         "In de schets zakken de waterbalken onder de letters. Nu eindigt de compositie exact op de "
         "basislijn, of binnen het overschot van de ronding."),
        ("De boog staat dichter op het woord",
         "Overstek terug van ruim een tiende naar 0,06 × de kapitaalhoogte, rijzing van 0,40 naar 0,30. "
         "Daardoor leest het als één merk in plaats van twee losse elementen."),
        ("De O leest weer als letter",
         "Met de ring erom staat er HIERO. Zonder ring staat er HIER met een zonsondergang ernaast — "
         "dat is variant B op pagina 4, als je die kant op wil."),
    ]
    lijst = "".join(
        '<div style="margin-top:4.5mm"><div style="font-weight:600;font-size:8pt">%s</div>'
        '<div class="tiny" style="margin-top:1.2mm;max-width:112mm">%s</div></div>' % (a, b)
        for a, b in punten)
    inner = '''
<div class="pad">
  <div style="display:flex;gap:11mm;height:100%%">
    <div style="width:120mm;padding-top:11mm">
      <h2>Wat er strakker is</h2>
      <p class="small" style="margin-top:3mm;max-width:112mm">Het idee blijft ongewijzigd: een
        dakcontour boven het woord en de O als zon die in het water zakt. Alleen de uitvoering is
        opnieuw opgezet, met maten die uit elkaar volgen.</p>
      %s
    </div>
    <div style="flex:1;display:flex;flex-direction:column;gap:5mm;padding-top:11mm">
      <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center;
        background:#fff">
        <div class="lbl">Uitgangspunt — nagebouwd</div>
        <div style="margin-top:6mm">%s</div>
        <div class="tiny" style="margin-top:6mm">Benadering van je schets, opnieuw getekend om te
          kunnen vergelijken. Niet je originele bestand.</div>
      </div>
      <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center">
        <div class="lbl">Uitwerking</div>
        <div style="margin-top:6mm">%s</div>
        <div class="tiny" style="margin-top:6mm">Variant A in het palet Avondlicht. Alle maten staan
          op de volgende pagina.</div>
      </div>
    </div>
  </div>
</div>''' % (lijst, schets, nieuw)
    return page(inner, num="02 / 11", label="Vergelijking")

# ---------------------------------------------------------------- 3 constructie

def p3():
    g = G.geometrie(L)
    ink, hulp = PAL["ink"], "#C0392B"
    b, _ = G.lockup(L, PAL, uid="cst")
    gl = []
    def lijn(x1, y1, x2, y2, dash="3 3", kl=None, w=1.1):
        gl.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="%s" stroke-width="%.2f"'
                  ' stroke-dasharray="%s" opacity=".75"/>' % (x1, y1, x2, y2, kl or hulp, w, dash))
    def txt(x, y, s, anchor="start", kl=None, fs=18):
        gl.append('<text x="%.2f" y="%.2f" text-anchor="%s" font-family="Inter" font-weight="600"'
                  ' font-size="%d" fill="%s">%s</text>' % (x, y, anchor, fs, kl or hulp, s))
    x0, x1 = -g["oh"] - 168, g["breedte"] + g["oh"] + 24
    lijn(x0, 0, x1, 0); lijn(x0, G.CAP, x1, G.CAP)                  # kapitaal en basislijn
    lijn(x0, g["y0"], x1, g["y0"], "5 4")                            # koorde van de boog
    lijn(x0, g["y0"] - g["rise"], x1, g["y0"] - g["rise"], "5 4")    # top van de boog
    lijn(g["cx"], -60, g["cx"], G.CAP + 60, "2 4")                   # hart van de O
    gl.append('<rect x="%.2f" y="0" width="%.2f" height="%.2f" fill="none" stroke="%s"'
              ' stroke-width="1.1" opacity=".6"/>' % (g["olinks"], G.CAP, G.CAP, hulp))
    gl.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="none" stroke="%s" stroke-width="1.1"'
              ' opacity=".6"/>' % (g["cx"], g["cy"], g["D"] / 2, hulp))
    txt(x0 + 4, g["y0"] - g["rise"] - 10, "TOP VAN DE BOOG")
    txt(x0 + 4, g["y0"] - 10, "KOORDE")
    txt(x1 - 4, -10, "KAPITAALLIJN", "end")
    txt(x0 + 4, G.CAP + 26, "BASISLIJN")
    txt(g["cx"], G.CAP + 52, "Ø 1,03 × KAPITAALHOOGTE", "middle")
    vb = "%.2f %.2f %.2f %.2f" % (x0 - 8, g["y0"] - g["rise"] - 44,
                                  (x1 + 8) - (x0 - 8), G.CAP + 96 + g["rise"] + 44)
    tek = G.inline('<g opacity=".92">%s</g>%s' % (b, "".join(gl)), vb, 130)
    # detail van de O
    D, t = g["D"], g["t"]
    R, ri = D / 2.0, D / 2.0 - g["t"]
    ocx, ocy = 0.0, 0.0
    yh, th, rs = ocy + ri * 0.15, ri * 0.16, ri * 0.67
    dl = [G.zon_o(0.0, 0.0, D, t, PAL["ink"], PAL["sun"], PAL["water"], PAL["bg"], "A", True, "od")]
    dl.append('<circle cx="0" cy="0" r="%.2f" fill="none" stroke="%s" stroke-width="1.4"'
              ' stroke-dasharray="4 4" opacity=".85"/>' % (ri, hulp))
    dl.append('<line x1="%.2f" y1="0" x2="%.2f" y2="0" stroke="%s" stroke-width="1.2"'
              ' stroke-dasharray="2 4" opacity=".8"/>' % (-R - 40, R + 40, hulp))
    dl.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="%s" stroke-width="1.2"'
              ' stroke-dasharray="4 3" opacity=".85"/>' % (-R - 40, yh, R + 40, yh, hulp))
    dl.append('<line x1="0" y1="%.2f" x2="0" y2="%.2f" stroke="%s" stroke-width="1.2"'
              ' stroke-dasharray="2 4" opacity=".6"/>' % (-R - 26, R + 26, hulp))
    for ty, lab in ((-R - 30, "BUITENDIAMETER  1,03"), (yh - 8, "HORIZON  0,15 \u00d7 BINNENRADIUS"),
                    (R + 44, "ZON  0,67 \u00d7 BINNENRADIUS"), (-ri - 10, "RING  0,60 \u00d7 STAM")):
        dl.append('<text x="%.2f" y="%.2f" text-anchor="end" font-family="Inter" font-weight="600"'
                  ' font-size="17" fill="%s">%s</text>' % (-R - 18, ty, hulp, lab))
    dvb = "%.2f %.2f %.2f %.2f" % (-R - 300, -R - 54, (R + 46) - (-R - 300), 2 * R + 112)
    detail = G.inline("".join(dl), dvb, 120)

    maten = [
        ("Kapitaalhoogte", "1,00 — alle maten zijn hiervan afgeleid"),
        ("Diameter van de O", "1,03 × kapitaalhoogte, met overschot boven en onder"),
        ("Ringdikte van de O", "0,60 × de letterstam"),
        ("Horizon in de O", "0,15 × binnenradius onder het hart"),
        ("Zonsradius", "0,67 × binnenradius"),
        ("Afstand R naar O", "0,062 × kapitaalhoogte"),
        ("Rijzing van de boog", "0,30 × kapitaalhoogte"),
        ("Koorde van de boog", "0,13 × kapitaalhoogte boven de kapitaallijn"),
        ("Lijndikte van de boog", "0,34 × de letterstam"),
        ("Overstek van de boog", "0,06 × kapitaalhoogte aan weerszijden"),
    ]
    rows = "".join('<tr><td style="width:40mm;opacity:.6">%s</td><td>%s</td></tr>' % (a, b)
                   for a, b in maten)
    inner = '''
<div class="pad">
  <div style="padding-top:11mm"><h2>Constructie</h2>
    <p class="small" style="margin-top:3mm;max-width:150mm">Eén maat bepaalt alles: de
      kapitaalhoogte. Wie het logo namaakt of aanpast, kan met deze verhoudingen exact hetzelfde
      resultaat tekenen.</p></div>
  <div style="display:flex;gap:11mm;margin-top:9mm;align-items:flex-start">
    <div style="width:132mm;flex:none">%s
      <div style="margin-top:5mm">%s</div></div>
    <div style="flex:1;min-width:0"><div class="lbl">Verhoudingen</div><table style="margin-top:3mm">%s</table></div>
  </div>
</div>''' % (tek, detail, rows)
    return page(inner, num="03 / 11", label="Constructie")

# ---------------------------------------------------------------- 4 de O

def p4():
    opties = [
        ("A", "Ring om de zonsondergang", True,
         "Leest onmiskenbaar als HIERO. De ring is lichter dan de letters, waardoor de O een venster "
         "wordt en de zon niet met de letters concurreert. Werkt het best klein."),
        ("B", "Zonder ring", False,
         "Dichtst bij je schets en het meest sfeervol. Nadeel: er staat HIER met een zonsondergang "
         "ernaast, niet HIERO. Kan werken als de naam er altijd bij staat, maar niet als los merk."),
        ("C", "Onderste helft als gevelritme", False,
         "De waterbalken lopen buiten de cirkel door en verwijzen naar de galerijen van het gebouw. "
         "Rijk, maar het silhouet wordt onrustig en valt onder 15 mm uit elkaar."),
        ("D", "Zon achter de horizon", False,
         "De zon zakt half weg achter de waterlijn. Sterk beeld, maar het geheel gaat richting een "
         "aan-uitknop en de zon verliest zijn vorm."),
    ]
    cards = ""
    for k, titel, aanbev, tekst in opties:
        rand = "2px solid %s" % PAL["ink"] if aanbev else "1px solid rgba(0,0,0,.12)"
        merkje = ('<div style="display:inline-block;background:%s;color:#fff;font-size:6pt;'
                  'font-weight:600;letter-spacing:.2em;padding:1mm 2.6mm;border-radius:9mm">'
                  'AANBEVOLEN</div>' % PAL["ink"]) if aanbev else ""
        cards += '''<div style="flex:1;background:#FBF9F4;border:%s;border-radius:1.6mm;padding:6mm;
          display:flex;flex-direction:column">
          <div style="display:flex;justify-content:space-between;align-items:flex-start">
            <div class="lbl">Variant %s</div>%s</div>
          <div style="margin:7mm 0;display:flex;align-items:center;justify-content:center;flex:1">%s</div>
          <div style="font-weight:600;font-size:7.6pt">%s</div>
          <div class="tiny" style="margin-top:1.4mm">%s</div>
        </div>''' % (rand, k, merkje, lk(w=52, variant=k, uid="o" + k), titel, tekst)
    inner = '''
<div class="pad">
  <div style="padding-top:11mm"><h2>De O</h2>
    <p class="small" style="margin-top:3mm;max-width:150mm">Vier manieren om de zonsondergang in de
      letter te zetten. De vraag is elke keer dezelfde: leest er nog HIERO, en houdt het stand op
      een favicon van 16 pixels?</p></div>
  <div style="display:flex;gap:4mm;margin-top:8mm;height:118mm">%s</div>
</div>''' % cards
    return page(inner, num="04 / 11", label="De O")

# ---------------------------------------------------------------- 5 de boog

def p5():
    opties = [
        ("Rijzing 0,30 — aanbevolen", "rond", 0.30, True,
         "Genoeg boog om als dak te lezen, laag genoeg om één geheel te vormen met het woord."),
        ("Rijzing 0,20 — strakker", "rond", 0.20, False,
         "Bijna een horizon. Rustiger en moderner, maar de dakassociatie verdwijnt grotendeels."),
        ("Platte contour", "plat", 0.26, False,
         "Letterlijker: het silhouet van een plat dak. Past bij het gebouw, maar kan als tent lezen."),
    ]
    cards = ""
    for titel, vorm, rise, aanbev, tekst in opties:
        rand = "2px solid %s" % PAL["ink"] if aanbev else "1px solid rgba(0,0,0,.12)"
        cards += '''<div style="flex:1;background:#FBF9F4;border:%s;border-radius:1.6mm;padding:6mm;
          display:flex;flex-direction:column">
          <div class="lbl">%s</div>
          <div style="margin:8mm 0;flex:1;display:flex;align-items:center">%s</div>
          <div class="tiny">%s</div></div>''' % (
            rand, titel, lk(w=68, vorm=vorm, rise=rise, uid="b%s%d" % (vorm, rise * 100)), tekst)
    inner = '''
<div class="pad">
  <div style="padding-top:11mm"><h2>De boog</h2>
    <p class="small" style="margin-top:3mm;max-width:150mm">De boog is het dak en de horizon in één.
      Hij hoort bij het logo, maar mag er ook af: op smalle dragers en in kleine maten is de
      compacte versie zonder boog de juiste keuze.</p></div>
  <div style="display:flex;gap:4mm;margin-top:8mm;height:78mm">%s</div>
  <div style="display:flex;gap:4mm;margin-top:4mm;height:44mm">
    <div style="flex:2;background:#FBF9F4;border:1px solid rgba(0,0,0,.12);border-radius:1.6mm;
      padding:6mm;display:flex;align-items:center;gap:8mm">
      <div>%s</div>
      <div><div style="font-weight:600;font-size:7.6pt">Compact, zonder boog</div>
        <div class="tiny" style="margin-top:1.4mm;max-width:70mm">Voor briefpapier, e-mailondertekening,
          smalle banners en alles onder 20 mm breed.</div></div>
    </div>
    <div style="flex:1;background:%s;border-radius:1.6mm;padding:6mm;display:flex;
      align-items:center;justify-content:center">%s</div>
  </div>
</div>''' % (cards, lk(w=54, boog=False, uid="cmp"), PAL["ink"], lk(w=54, dark=True, uid="drk"))
    return page(inner, num="05 / 11", label="De boog")

# ---------------------------------------------------------------- 6 letterkeuze

def p6():
    kand = [
        ("Outfit 800", "Outfit-800.ttf", True,
         "Geometrisch, gesloten vormen, vlakke afsluitingen. De ronde O sluit exact aan op de cirkel "
         "van de zon, dus het logo voelt uit één stuk."),
        ("Archivo 700", "Archivo-700.ttf", False,
         "Smaller en meer grotesk. Zakelijker en iets Nederlandser van toon, maar de R en de O staan "
         "minder rustig naast elkaar."),
        ("Space Grotesk 700", "SpaceGrotesk-700.ttf", False,
         "Meer eigenzinnig, met karakter in de R. Lichter van gewicht, waardoor de zon zwaarder weegt "
         "dan de naam."),
    ]
    cards = ""
    for titel, fn, aanbev, tekst in kand:
        Lx = G.Letters(fn)
        b, vb = G.lockup(Lx, PAL, uid="f" + fn[:4])
        rand = "2px solid %s" % PAL["ink"] if aanbev else "1px solid rgba(0,0,0,.12)"
        merkje = ('<span style="background:%s;color:#fff;font-size:5.6pt;font-weight:600;'
                  'letter-spacing:.18em;padding:.8mm 2.2mm;border-radius:9mm;margin-left:3mm">'
                  'AANBEVOLEN</span>' % PAL["ink"]) if aanbev else ""
        cards += '''<div style="background:#FBF9F4;border:%s;border-radius:1.6mm;padding:6mm 7mm;
          display:flex;align-items:center;gap:10mm">
          <div style="width:96mm">%s</div>
          <div style="flex:1"><div style="font-weight:600;font-size:8pt">%s%s</div>
          <div class="tiny" style="margin-top:1.6mm">%s</div>
          <div class="tiny" style="margin-top:1.6mm;opacity:.5">Stam %.3f × kapitaalhoogte</div></div>
        </div>''' % (rand, G.inline(b, vb, 96), titel, merkje, tekst, Lx.stem / Lx.cap)
    inner = '''
<div class="pad">
  <div style="padding-top:11mm"><h2>Letterkeuze</h2>
    <p class="small" style="margin-top:3mm;max-width:150mm">Alle drie zijn opengelicentieerd, dus vrij
      te gebruiken in druk en online. In de geleverde bestanden zijn de letters omgezet naar contouren;
      wie het logo plaatst heeft de letter dus niet nodig.</p></div>
  <div style="display:flex;flex-direction:column;gap:4mm;margin-top:8mm">%s</div>
</div>''' % cards
    return page(inner, num="06 / 11", label="Letterkeuze")

# ---------------------------------------------------------------- 7 kleur

def p7():
    kaarten = []
    for key in ("schemer", "tonaal", "avondrood", "klei"):
        p = G.PALETTEN[key]
        aanbev = key == "schemer"
        rand = "2px solid %s" % PAL["ink"] if aanbev else "1px solid rgba(0,0,0,.12)"
        stalen = "".join(
            '<div style="flex:1"><div style="height:9mm;background:%s;border-radius:.8mm;'
            'box-shadow:inset 0 0 0 1px rgba(0,0,0,.14)"></div>'
            '<div class="tiny" style="margin-top:1.2mm;font-weight:600;opacity:.9">%s</div>'
            '<div class="tiny" style="opacity:.55">%s</div></div>'
            % (h, n, h.upper()) for h, n in
            ((p["ink"], p["inknaam"]), (p["sun"], p["sunnaam"]),
             (p["water"], p["waternaam"]), (p["bg"], p["bgnaam"])))
        merkje = ('<span style="background:%s;color:#fff;font-size:5.4pt;font-weight:600;'
                  'letter-spacing:.18em;padding:.7mm 2mm;border-radius:9mm;margin-left:3mm">'
                  'AANBEVOLEN</span>' % PAL["ink"]) if aanbev else ""
        b, vb = G.lockup(L, p, uid="p" + key)
        kaarten.append(
            '<div style="flex:1;background:%s;border:%s;border-radius:1.6mm;padding:5mm;'
            'display:flex;flex-direction:column;overflow:hidden">'
            '<div style="display:flex;align-items:center"><div class="lbl">%s</div>%s</div>'
            '<div style="margin:5mm 0 4mm;flex:1;display:flex;align-items:center">%s</div>'
            '<div style="display:flex;gap:2mm">%s</div>'
            '<div class="tiny" style="margin-top:2.5mm">%s</div></div>'
            % (p["bg"], rand, p["naam"], merkje, G.inline(b, vb, 66), stalen, p["waarom"]))
    inner = '''
<div class="pad">
  <div style="padding-top:9mm"><h2>Kleur</h2>
    <p class="small" style="margin-top:3mm;max-width:150mm">Drie kleuren en een basis: de ink voor
      letters en boog, de zon, en het water. Meer heeft het logo niet nodig, en de zon is de enige
      die warm mag zijn.</p></div>
  <div style="display:flex;gap:4mm;margin-top:6mm;height:68mm">%s%s</div>
  <div style="display:flex;gap:4mm;margin-top:4mm;height:68mm">%s%s</div>
</div>''' % tuple(kaarten)
    return page(inner, num="07 / 11", label="Kleur")

# ---------------------------------------------------------------- 8 varianten

def p8():
    def cel(inhoud, label, bg="#FBF9F4", flex=1, kleur=None):
        c = ' style="color:%s"' % kleur if kleur else ""
        return ('<div style="flex:%s;background:%s;border-radius:1.6mm;padding:5mm;display:flex;'
                'flex-direction:column;align-items:center;justify-content:center;gap:5mm">'
                '%s<div class="lbl"%s>%s</div></div>' % (flex, bg, inhoud, c, label))
    inner = '''
<div class="pad">
  <div style="padding-top:11mm"><h2>Varianten en maten</h2>
    <p class="small" style="margin-top:3mm;max-width:150mm">Het primaire logo is de standaard. Onder
      20 mm breed vervalt de reflectiebalk in de O, onder 12 mm vervalt de boog. Monochroom is
      verplicht op foto en op het hek van de aannemer.</p></div>
  <div style="display:flex;gap:4mm;margin-top:7mm;height:52mm">
    %s%s%s
  </div>
  <div style="display:flex;gap:4mm;margin-top:4mm;height:52mm">
    %s%s%s%s
  </div>
  <div style="display:flex;gap:4mm;margin-top:4mm;height:30mm">
    <div style="flex:2;background:#FBF9F4;border-radius:1.6mm;padding:5mm 6mm;display:flex;
      align-items:center;gap:7mm">
      <div style="border:1px dashed %s;padding:3.4mm">%s</div>
      <div><div style="font-weight:600;font-size:7.4pt">Vrije ruimte</div>
      <div class="tiny" style="margin-top:1.2mm;max-width:66mm">Rondom minimaal de hoogte van de
        letter H. Binnen dat kader komt niets anders te staan.</div></div>
    </div>
    <div style="flex:1;background:#FBF9F4;border-radius:1.6mm;padding:5mm 6mm;display:flex;
      align-items:center;gap:6mm">
      <div>%s</div>
      <div class="tiny">Beeldmerk<br>vanaf 8 mm</div>
    </div>
  </div>
</div>''' % (
        cel(lk(w=68), "Primair", flex=2),
        cel(lk(w=68, dark=True, uid="v2"), "Op ink", bg=PAL["ink"], flex=2, kleur="#fff"),
        cel(mk(w=22, uid="v3"), "Beeldmerk"),
        cel(lk(w=48, mono=PAL["ink"], uid="v4"), "Monochroom ink"),
        cel(lk(w=48, mono="#FFFFFF", uid="v5"), "Monochroom wit", bg="#20242A", kleur="#fff"),
        cel(lk(w=40, bars=False, uid="v6"), "Klein formaat"),
        cel(lk(w=34, boog=False, bars=False, uid="v7"), "Zeer klein"),
        PAL["ink"], lk(w=40, uid="v8"), mk(w=13, uid="v9", bars=False))
    return page(inner, num="08 / 11", label="Varianten")

# ---------------------------------------------------------------- 9 fout gebruik

def p9():
    def fout(inhoud, tekst, extra=""):
        return ('<div style="flex:1;background:#FBF9F4;border-radius:1.6mm;padding:5mm;display:flex;'
                'flex-direction:column">'
                '<div class="kruis" style="flex:1;display:flex;align-items:center;justify-content:center;'
                'overflow:hidden;%s">%s</div>'
                '<div class="tiny" style="margin-top:3mm">%s</div></div>' % (extra, inhoud, tekst))
    streep = ("background-image:repeating-linear-gradient(45deg,#cfc9bb 0 4px,#F4F1EA 4px 9px)")
    rij1 = "".join([
        fout('<div style="transform:scaleX(1.28)">%s</div>' % lk(w=44, uid="f1"),
             "Niet uitrekken of samendrukken. Verhoudingen staan vast."),
        fout('<div style="transform:rotate(-7deg)">%s</div>' % lk(w=44, uid="f2"),
             "Niet kantelen. De horizon in de O moet horizontaal blijven."),
        fout('<div style="filter:drop-shadow(2mm 2mm 0 rgba(0,0,0,.3))">%s</div>' % lk(w=44, uid="f3"),
             "Geen schaduw, gloed of verloop. Het logo is vlak."),
    ])
    afwijk = dict(PAL); afwijk.update({"sun": "#D6338F", "water": "#7ED957"})
    rij2 = "".join([
        fout(lk(pal=afwijk, w=44, uid="f4"),
             "Geen eigen kleuren invullen. Alleen de vier vastgestelde paletten."),
        fout('<div style="display:flex;flex-direction:column;gap:7mm;align-items:center">'
             '%s%s</div>' % (
                 G.inline(G.boog_pad(0, 300, 0, 90, 12, PAL["ink"]), "-8 -104 316 116", 44),
                 lk(w=44, boog=False, uid="f5")),
             "De boog niet losmaken van het woord. Hij hoort op vaste afstand."),
        fout(lk(w=44, uid="f6"), "Niet op een onrustige of contrastarme ondergrond plaatsen.", streep),
    ])
    inner = '''
<div class="pad">
  <div style="padding-top:11mm"><h2>Fout gebruik</h2>
    <p class="small" style="margin-top:3mm;max-width:150mm">Zes dingen die het logo kapotmaken. Deze
      pagina hoort mee naar iedere leverancier, aannemer en makelaar die het logo plaatst.</p></div>
  <div style="display:flex;gap:4mm;margin-top:7mm;height:62mm">%s</div>
  <div style="display:flex;gap:4mm;margin-top:4mm;height:62mm">%s</div>
</div>''' % (rij1, rij2)
    return page(inner, num="09 / 11", label="Fout gebruik")

# ---------------------------------------------------------------- 10 toepassing

def p10():
    inner = '''
<div class="pad">
  <div style="padding-top:11mm"><h2>Toepassing</h2>
    <p class="small" style="margin-top:3mm;max-width:150mm">Het logo werkt op 24 meter bouwhek en op
      een favicon van 16 pixels. Dat is de hele test.</p></div>
  <div style="margin-top:7mm;background:%s;border-radius:1.4mm;height:44mm;display:flex;
    align-items:center;padding:0 12mm;gap:14mm;position:relative;overflow:hidden">
    <div>%s</div>
    <div style="color:#fff">
      <div style="font-family:Outfit;font-weight:800;font-size:15pt;line-height:1.05">
        146 woningen aan de Dirk de Derdelaan</div>
      <div style="font-size:8pt;opacity:.8;margin-top:2mm">Verkoop vanaf H2 2028 · hiero.nl</div>
    </div>
    <div style="position:absolute;right:0;top:0;bottom:0;width:22mm;background:%s;display:flex;
      align-items:center;justify-content:center">
      <div style="font-family:Outfit;font-weight:800;font-size:11pt;color:%s;
        transform:rotate(-90deg);white-space:nowrap">HIERO.NL</div></div>
  </div>
  <div style="display:flex;gap:4mm;margin-top:4mm;height:74mm">
    <div style="width:34mm;background:%s;border-radius:1.4mm;display:flex;flex-direction:column;
      align-items:center;justify-content:space-between;padding:6mm 0">
      <div style="transform:rotate(-90deg);transform-origin:center">%s</div>
      <div class="lbl w">Gevelbanner</div>
    </div>
    <div style="flex:1;background:#FBF9F4;border-radius:1.4mm;padding:5mm;display:flex;
      flex-direction:column">
      <div class="lbl">Social — vierkant</div>
      <div style="flex:1;background:%s;border-radius:1mm;margin-top:4mm;display:flex;
        flex-direction:column;justify-content:space-between;padding:5mm">
        <div>%s</div>
        <div style="color:#fff;font-family:Outfit;font-weight:800;font-size:11pt;line-height:1.1">
          Vanaf de elfde<br>zie je de mist<br>over de polder</div>
      </div>
    </div>
    <div style="flex:1;background:#FBF9F4;border-radius:1.4mm;padding:5mm;display:flex;
      flex-direction:column">
      <div class="lbl">Website — kop</div>
      <div style="background:#fff;border-radius:1mm;margin-top:4mm;flex:1;overflow:hidden;
        border:1px solid rgba(0,0,0,.1)">
        <div style="height:6mm;background:rgba(0,0,0,.05);display:flex;align-items:center;
          padding:0 3mm;gap:1.6mm">
          <div style="width:1.6mm;height:1.6mm;border-radius:9mm;background:rgba(0,0,0,.18)"></div>
          <div style="width:1.6mm;height:1.6mm;border-radius:9mm;background:rgba(0,0,0,.18)"></div>
          <div style="background:#fff;border-radius:9mm;padding:.5mm 3mm;font-size:5.4pt;opacity:.6;
            margin-left:2mm">hiero.nl</div></div>
        <div style="padding:5mm;display:flex;justify-content:space-between;align-items:center">
          <div>%s</div>
          <div style="display:flex;gap:3mm;font-size:5.6pt;opacity:.7;align-items:center">
            <div>Het gebouw</div><div>Uitzicht</div>
            <div style="background:%s;color:#fff;border-radius:9mm;padding:1mm 2.6mm">Inschrijven</div>
          </div>
        </div>
        <div style="padding:0 5mm 5mm">
          <div style="font-family:Outfit;font-weight:800;font-size:13pt;color:%s;line-height:1.05">
            146 woningen<br>op 38 meter</div></div>
      </div>
    </div>
    <div style="width:40mm;background:#FBF9F4;border-radius:1.4mm;padding:5mm;display:flex;
      flex-direction:column;justify-content:space-between">
      <div class="lbl">Favicon</div>
      <div style="display:flex;align-items:flex-end;gap:4mm;justify-content:center">
        %s%s%s
      </div>
      <div class="tiny">32, 16 en 8 mm breed. Onder 12 mm zonder boog, onder 20 mm zonder reflectie.</div>
    </div>
  </div>
</div>''' % (PAL["ink"], lk(w=44, dark=True, uid="t1"), PAL["sun"], PAL["ink"],
             PAL["ink"], lk(w=30, dark=True, uid="t2"), PAL["ink"], lk(w=26, dark=True, uid="t3"),
             lk(w=26, uid="t4"), PAL["ink"], PAL["ink"],
             mk(w=13, uid="t5"), mk(w=8, uid="t6", bars=False, boog=False),
             mk(w=5, uid="t7", bars=False, boog=False))
    return page(inner, num="10 / 11", label="Toepassing")

# ---------------------------------------------------------------- 11 bestanden

def p11():
    rows = "".join('<tr><td style="width:56mm;font-weight:600">%s</td><td>%s</td></tr>' % (a, b)
                   for a, b in [
        ("hiero-logo.svg", "Primair logo, palet Schemer, op lichte ondergrond"),
        ("hiero-logo-ink.svg", "Primair logo op de ink-kleur, voor donkere vlakken"),
        ("hiero-logo-compact.svg", "Zonder boog, voor smalle dragers en kleine maten"),
        ("hiero-logo-klein.svg", "Zonder reflectiebalk, vanaf 12 tot 20 mm breed"),
        ("hiero-logo-mono-ink.svg", "Eén kleur, voor stempels en eenkleurig drukwerk"),
        ("hiero-logo-mono-wit.svg", "Eén kleur wit, voor foto en donkere ondergrond"),
        ("hiero-beeldmerk.svg", "Alleen de zon-O met boog, voor social en app-icoon"),
        ("hiero-beeldmerk-zonder-boog.svg", "Alleen de zon-O, voor favicon onder 12 mm"),
        ("hiero-logo-{palet}.svg", "Dezelfde lockup in Tonaal, Avondrood en Inkt en klei"),
    ])
    inner = '''
<div class="pad">
  <div style="padding-top:12mm;display:flex;gap:11mm">
    <div style="width:126mm">
      <h2>Bestanden en verantwoording</h2>
      <div class="lbl" style="margin-top:8mm">Wat je krijgt</div>
      <table style="margin-top:3mm">%s</table>
      <div class="lbl" style="margin-top:7mm">Letters</div>
      <p class="small" style="margin-top:2.5mm;max-width:120mm">In alle SVG-bestanden zijn de letters
        omgezet naar contouren. Wie het logo plaatst heeft geen letterlicentie nodig en het kan niet
        verschuiven door een ontbrekende letter. Outfit valt onder de SIL Open Font License; voor
        koppen en broodtekst is de familie vrij te gebruiken.</p>
      <div class="lbl" style="margin-top:6mm">Nog te beslissen</div>
      <p class="small" style="margin-top:2.5mm;max-width:120mm">Variant van de O, vorm en rijzing van
        de boog, letterkeuze en palet. Zeg per onderdeel wat je wil en ik zet het vast; daarna kan het
        logo in de drie huisstijldocumenten worden doorgevoerd.</p>
    </div>
    <div style="flex:1;background:%s;border-radius:2mm;padding:11mm 10mm;display:flex;
      flex-direction:column;justify-content:space-between">
      <div>
        <div class="lbl w">Waar het idee op staat</div>
        <p class="tiny" style="margin-top:3mm;color:#fff;opacity:.9;line-height:1.7">
          De boog is het dak van een gebouw van dertien lagen en tegelijk de horizon die je vanaf
          38 meter ziet. De zon in de O zakt over het water van het Scheur. Het logo zegt daarmee
          precies wat de troef van dit project is: hoogte en uitzicht, in een adres dat mensen al
          kennen.</p>
        <p class="tiny" style="margin-top:4mm;color:#fff;opacity:.75;line-height:1.7">
          De naam Hiero komt van de bijnaam Hierosolymita van Dirk III, de graaf naar wie de straat
          is vernoemd, en is tegelijk Vlaardings voor hier.</p>
      </div>
      <div>
        <div style="display:flex;justify-content:center;margin-bottom:9mm">%s</div>
        <div style="height:1px;background:#fff;opacity:.3"></div>
        <p class="tiny" style="margin-top:4mm;color:#fff;opacity:.7">Voorstel ter bespreking.
          Niets hierin is definitief vastgesteld.</p>
      </div>
    </div>
  </div>
</div>''' % (rows, PAL["ink"], lk(w=52, dark=True, uid="e1"))
    return page(inner, num="11 / 11", label="Bestanden")

# ---------------------------------------------------------------- bouwen

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def export_svg():
    """Losse bestanden, letters als contouren, geen letterlicentie nodig."""
    uit = []
    def w(naam, body, vb):
        pad = os.path.join(LOGODIR, naam)
        open(pad, "w").write(G.svg(body, vb))
        uit.append(naam)
    b, vb = G.lockup(L, PAL, uid="a");                        w("hiero-logo.svg", b, vb)
    b, vb = G.lockup(L, PAL, dark=True, uid="b");             w("hiero-logo-ink.svg", b, vb)
    b, vb = G.lockup(L, PAL, boog=False, uid="c");            w("hiero-logo-compact.svg", b, vb)
    b, vb = G.lockup(L, PAL, bars=False, uid="d");            w("hiero-logo-klein.svg", b, vb)
    b, vb = G.lockup(L, PAL, mono=PAL["ink"], uid="e");       w("hiero-logo-mono-ink.svg", b, vb)
    b, vb = G.lockup(L, PAL, mono="#FFFFFF", uid="f");        w("hiero-logo-mono-wit.svg", b, vb)
    b, vb = G.merk(L, PAL, uid="g");                          w("hiero-beeldmerk.svg", b, vb)
    b, vb = G.merk(L, PAL, uid="g2", boog=False);             w("hiero-beeldmerk-zonder-boog.svg", b, vb)
    for k in ("tonaal", "avondrood", "klei"):
        b, vb = G.lockup(L, G.PALETTEN[k], uid="h" + k);      w("hiero-logo-%s.svg" % k, b, vb)
    return uit

def main():
    paginas = "".join(f() for f in (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11))
    html = ('<!doctype html><html lang="nl"><head><meta charset="utf-8">'
            '<title>Hiero — logo-uitwerking</title><style>%s%s</style></head><body>%s</body></html>'
            % (FONT_CSS, CSS, paginas))
    hp = os.path.join(HERE, "hiero-logo.html")
    open(hp, "w").write(html)
    pdf = os.path.join(HERE, "Hiero - logo-uitwerking.pdf")
    r = subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                        "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                        "--virtual-time-budget=15000", "--print-to-pdf=" + pdf, "file://" + hp],
                       capture_output=True, text=True, timeout=300)
    if not os.path.exists(pdf):
        sys.stderr.write(r.stdout + r.stderr)
        raise SystemExit("print mislukt")
    bestanden = export_svg()
    print("PDF  %.0f kB" % (os.path.getsize(pdf) / 1024))
    print("SVG  %d bestanden: %s" % (len(bestanden), ", ".join(bestanden)))

if __name__ == "__main__":
    main()
