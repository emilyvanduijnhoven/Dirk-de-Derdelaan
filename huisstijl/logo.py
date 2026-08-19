#!/usr/bin/env python3
"""Uitwerking van het logo-idee voor HIERO: dakcontour + de O als zonsondergang.

De letters HIER komen als echte outlines uit de letterfamilie (geen natekening),
de O is mathematisch geconstrueerd op hetzelfde raster: diameter = kapitaalhoogte,
ringdikte = stamdikte van de letters. Daardoor klopt het optisch op elk formaat.
"""
import os, subprocess, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
LOGODIR = os.path.join(HERE, "logo")
os.makedirs(LOGODIR, exist_ok=True)
CAP = 300.0                      # kapitaalhoogte in tekeneenheden
RING = 0.60                      # ringdikte van de O, als deel van de letterstam

# ---------------------------------------------------------------- paletten

PALETTEN = {
    "schemer": {
        "naam": "Schemer",
        "ink": "#16302F", "sun": "#D9A273", "water": "#4F6F6B",
        "bg": "#EFEAE0", "inknaam": "Diep petrol", "sunnaam": "Zandzon",
        "waternaam": "Gedempt groenblauw", "bgnaam": "Bot",
        "waarom": "Water en letters komen uit dezelfde familie, dus er is maar één warme noot. "
                  "Geen complementair conflict, en de zon is zand in plaats van geel.",
    },
    "tonaal": {
        "naam": "Tonaal",
        "ink": "#1F2A33", "sun": "#8093A0", "water": "#B6C2C8",
        "bg": "#ECEAE5", "inknaam": "Inkt", "sunnaam": "Middentoon",
        "waternaam": "Lichte toon", "bgnaam": "Kalk",
        "waarom": "Eén kleurfamilie in drie sterktes, geen tweede kleur. De zonsondergang wordt "
                  "licht in plaats van kleur. Het meest terughoudend en het moeilijkst fout te doen.",
    },
    "avondrood": {
        "naam": "Avondrood",
        "ink": "#2A2325", "sun": "#A84A3C", "water": "#7E8A8B",
        "bg": "#EDE6DB", "inknaam": "Bijna zwart", "sunnaam": "Avondrood",
        "waternaam": "Grijsgroen", "bgnaam": "Steen",
        "waarom": "Een zon die de horizon raakt is rood, niet geel. Dat is meteen minder "
                  "voorspelbaar, en het grijsgroene water houdt het koel zonder blauw te worden.",
    },
    "klei": {
        "naam": "Inkt en klei",
        "ink": "#22201D", "sun": "#B06A45", "water": "#D3A98F",
        "bg": "#EDE8DF", "inknaam": "Roetzwart", "sunnaam": "Klei",
        "waternaam": "Lichte klei", "bgnaam": "Room",
        "waarom": "Tweekleurig: het water is een lichtere tint van de zon. Twee tinten in het hele "
                  "merk, dus het kan nauwelijks rommelig worden. Warm en aards.",
    },
}

# ---------------------------------------------------------------- letters

class Letters:
    def __init__(self, fontfile):
        self.ft = TTFont(os.path.join(FONTS, fontfile))
        self.gs = self.ft.getGlyphSet()
        self.cm = self.ft.getBestCmap()
        self.cap = self._bb("H")[3] - self._bb("H")[1]
        i = self._bb("I")
        self.stem = i[2] - i[0]
        self.s = CAP / self.cap

    def _bb(self, ch):
        p = BoundsPen(self.gs)
        self.gs[self.cm[ord(ch)]].draw(p)
        return p.bounds

    def d(self, ch):
        pen = SVGPathPen(self.gs)
        self.gs[self.cm[ord(ch)]].draw(pen)
        return pen.getCommands()

    def adv(self, ch):
        return self.gs[self.cm[ord(ch)]].width * self.s

    def lsb(self, ch):
        return self._bb(ch)[0] * self.s

    def rsb(self, ch):
        g = self.gs[self.cm[ord(ch)]]
        return (g.width - self._bb(ch)[2]) * self.s

    def word(self, text, x, track=0.0, fill="#000"):
        """Letters als outlines, y-as omgeklapt; baseline op y=CAP."""
        out, cur = [], x
        for ch in text:
            out.append('<g transform="translate(%.2f %.2f) scale(%.5f %.5f)" fill="%s">'
                       '<path d="%s"/></g>' % (cur, CAP, self.s, -self.s, fill, self.d(ch)))
            cur += self.adv(ch) + track
        return "".join(out), cur - track

# ---------------------------------------------------------------- de O

def zon_o(cx, cy, D, t, ink, sun, water, bg, variant="A", bars=True, uid="o"):
    """De O als zonsondergang. D = buitendiameter, t = ringdikte."""
    R = D / 2.0
    ri = R - t
    clip = ('<clipPath id="%s-in"><circle cx="%.2f" cy="%.2f" r="%.2f"/></clipPath>'
            % (uid, cx, cy, ri))
    ring = ('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="none" stroke="%s" stroke-width="%.2f"/>'
            % (cx, cy, R - t / 2.0, ink, t))
    # binnenindeling, alles afgeleid van de binnenradius
    yh = cy + ri * 0.15          # horizon net onder het midden
    th = ri * 0.16               # dikte van horizon en reflectie
    rs = ri * 0.67               # zonsradius
    halve_zon = ('<path d="M%.2f %.2f A%.2f %.2f 0 0 1 %.2f %.2f Z" fill="%s"/>'
                 % (cx - rs, yh, rs, rs, cx + rs, yh, sun))
    horizon = ('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s"/>'
               % (cx - R, yh, D, th, water))
    refl = ""
    if bars:
        refl = ('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s"/>'
                % (cx - rs * 0.72, yh + th * 2.10, 2 * rs * 0.72, th * 0.88, water))

    if variant == "A":
        return ('<g>%s<g clip-path="url(#%s-in)">%s%s%s</g>%s</g>'
                % (clip, uid, horizon, halve_zon, refl, ring))

    if variant == "B":
        # zonder ring: vierkant veld, onderste balk sluit exact op de basislijn
        top, bas = cy - CAP / 2.0, cy + CAP / 2.0
        H = bas - top
        rs2 = R * 0.94
        yh2 = top + H * 0.612
        st = [(0.612, 0.088, 1.00), (0.777, 0.078, 0.80), (0.930, 0.070, 0.52)]
        zon = ('<path d="M%.2f %.2f A%.2f %.2f 0 0 1 %.2f %.2f Z" fill="%s"/>'
               % (cx - rs2, yh2, rs2, rs2, cx + rs2, yh2, sun))
        bal = "".join(
            '<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s"/>'
            % (cx - rs2 * br, top + H * fy, 2 * rs2 * br, H * fh, water)
            for fy, fh, br in st)
        return "<g>%s%s</g>" % (zon, bal)

    if variant == "C":
        # bovenste helft ring, onderste helft als gevelritme
        boog = ('<path d="M%.2f %.2f A%.2f %.2f 0 0 1 %.2f %.2f" fill="none" stroke="%s"'
                ' stroke-width="%.2f" stroke-linecap="butt"/>'
                % (cx - (R - t / 2), yh, R - t / 2, R - t / 2, cx + (R - t / 2), yh, ink, t))
        seg = "".join(
            '<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s"/>'
            % (cx - (R * br), yh + th * fy, 2 * R * br, th * 0.86, water)
            for fy, br in ((0.0, 1.00), (1.85, 0.78), (3.70, 0.50)))
        return ('<g>%s<g clip-path="url(#%s-in)">%s</g>%s%s</g>'
                % (clip, uid, halve_zon, seg, boog))

    # D: volle zon die achter de horizon wegzakt
    volle = ('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="%s"/>'
             % (cx, cy - ri * 0.06, ri * 0.66, sun))
    snee = ('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s"/>'
            % (cx - R, yh, D, th * 0.55, bg))
    hor = ('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s"/>'
           % (cx - R, yh + th * 0.55, D, th, water))
    return ('<g>%s<g clip-path="url(#%s-in)">%s%s%s</g>%s</g>'
            % (clip, uid, volle, snee, hor, ring))


# ---------------------------------------------------------------- boog

def boog_pad(x0, x1, ybasis, rise, sw, kleur, vorm="rond"):
    """Dakcontour boven het woordmerk. Constante lijndikte, exacte cirkelboog."""
    W = x1 - x0
    if vorm == "plat":
        inzet = W * 0.14
        d = ("M%.2f %.2f L%.2f %.2f H%.2f L%.2f %.2f"
             % (x0, ybasis, x0 + inzet, ybasis - rise, x1 - inzet, x1, ybasis))
        return ('<path d="%s" fill="none" stroke="%s" stroke-width="%.2f"'
                ' stroke-linejoin="miter"/>' % (d, kleur, sw))
    R = (W * W / 4.0 + rise * rise) / (2.0 * rise)
    return ('<path d="M%.2f %.2f A%.2f %.2f 0 0 1 %.2f %.2f" fill="none" stroke="%s"'
            ' stroke-width="%.2f" stroke-linecap="butt"/>'
            % (x0, ybasis, R, R, x1, ybasis, kleur, sw))

# ---------------------------------------------------------------- opbouw

def geometrie(L, rise=0.30):
    """Alle maten van de lockup op één plek, zodat de constructietekening klopt."""
    track = -CAP * 0.010
    _, eind = L.word("HIER", 0.0, track)
    inkrechts = eind - L.rsb("R")
    D = CAP * 1.03
    olinks = inkrechts + CAP * 0.062
    return dict(track=track, eind=eind, inkrechts=inkrechts, D=D, olinks=olinks,
                cx=olinks + D / 2.0, cy=CAP / 2.0, t=L.stem * L.s * RING,
                breedte=olinks + D, sw=L.stem * L.s * 0.34, y0=-CAP * 0.13,
                oh=CAP * 0.06, rise=CAP * rise, stem=L.stem * L.s, cap=CAP)

def lockup(L, pal, variant="A", vorm="rond", rise=0.30, bars=True,
           dark=False, boog=True, uid="l", mono=None):
    ink = mono or (pal["bg"] if dark else pal["ink"])
    sun = mono or pal["sun"]
    water = mono or pal["water"]
    bg = pal["ink"] if dark else pal["bg"]
    if mono:
        sun = mono
        water = mono

    track = -CAP * 0.010
    woord, eind = L.word("HIER", 0.0, track, ink)
    inkrechts = eind - L.rsb("R")
    D = CAP * 1.03
    olinks = inkrechts + CAP * 0.062
    cx, cy = olinks + D / 2.0, CAP / 2.0
    t = L.stem * L.s * RING
    o = zon_o(cx, cy, D, t, ink, sun, water, bg, variant, bars, uid)

    breedte = olinks + D
    sw = L.stem * L.s * 0.34
    b = ""
    y0 = -CAP * 0.13
    if boog:
        oh = CAP * 0.06
        b = boog_pad(-oh, breedte + oh, y0, CAP * rise, sw, ink, vorm)
        top = y0 - CAP * rise - sw / 2.0
        links = -oh - (sw / 2.0 if vorm == "plat" else 0)
        rechts = breedte + oh + (sw / 2.0 if vorm == "plat" else 0)
    else:
        top = -6.0
        links, rechts = -4.0, breedte + 4.0
    onder = cy + D / 2.0
    vb = "%.2f %.2f %.2f %.2f" % (links - 3, top - 3, rechts - links + 6, onder - top + 6)
    return "%s%s%s" % (b, woord, o), vb


def merk(L, pal, dark=False, uid="m", mono=None, bars=False, boog=True):
    """Beeldmerk: alleen de zon-O met de boog erboven."""
    ink = mono or (pal["bg"] if dark else pal["ink"])
    sun = mono or pal["sun"]
    water = mono or pal["water"]
    bg = pal["ink"] if dark else pal["bg"]
    D = CAP * 1.03
    t = L.stem * L.s * RING
    cx, cy = D / 2.0, CAP / 2.0
    sw = L.stem * L.s * 0.34
    oh = D * 0.06
    y0 = -CAP * 0.15
    b = boog_pad(-oh, D + oh, y0, CAP * 0.30, sw, ink) if boog else ""
    o = zon_o(cx, cy, D, t, ink, sun, water, bg, "A", bars, uid)
    top = (y0 - CAP * 0.30 - sw / 2.0) if boog else (cy - D / 2 - 4)
    vb = "%.2f %.2f %.2f %.2f" % (-oh - 3, top - 3, D + 2 * oh + 6, cy + D / 2 - top + 6)
    return b + o, vb


def svg(body, vb, w=None, h=None, extra=""):
    maat = ""
    if w:
        maat = ' width="%s"' % w
    if h:
        maat += ' height="%s"' % h
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s"%s%s>%s</svg>'
            % (vb, maat, extra, body))


def inline(body, vb, breedte_mm, blok=True):
    return ('<svg viewBox="%s" preserveAspectRatio="xMidYMid meet" style="width:%smm;'
            'height:auto;%s">%s</svg>' % (vb, breedte_mm, "display:block" if blok else "", body))
