# Hiero — drie huisstijlvoorstellen

Drie richtingen voor dezelfde projectnaam, voor de transformatie van Dirk de Derdelaan
167–319 in Vlaardingen-Westwijk (146 woningen, verkoopstart H2 2028).

| Document | Richting | Kern |
|---|---|---|
| `Hiero - huisstijl 01 - Anno 1018.pdf` | Anno 1018 — het zegel | Het adres krijgt zijn geschiedenis terug: Dirk III, bijgenaamd Hierosolymita, en de slag van 1018. |
| `Hiero - huisstijl 02 - Het bord.pdf` | Het bord — straatnaambord | Als het adres het probleem is, zet het adres dan op de gevel. Wit op blauw, geen opsmuk. |
| `Hiero - huisstijl 03 - Het erf.pdf` | Het erf — de boog | Antwoord op de grootste angst van de doelgroep: wie zijn mijn buren, en wie zorgt hiervoor? |

Elk document is 17 liggende pagina's (280 × 210 mm) en volgt dezelfde opbouw:
omslag, de naam, de ligging, de richting, primair logo, logovarianten, kleur,
typografie, grafisch element, toon en kernboodschap, en dan de toepassingen
(bouwhek, gevelbanner, projectpagina, social, drukwerk), overzicht en verantwoording.

## Logo-uitwerking

`Hiero - logo-uitwerking.pdf` werkt het logo-idee uit: een dakcontour boven het woord en de
O als zon die in het water zakt. Elf pagina's met constructie, vier varianten van de O, drie
boogvormen, drie letterkeuzes, vier paletten, varianten en maten, fout gebruik en toepassing.

De losse bestanden staan in `logo/`. In alle SVG's zijn de letters omgezet naar contouren,
dus wie het logo plaatst heeft geen letterlicentie nodig.

## Opnieuw genereren

```
python3 build.py       # de drie huisstijlrichtingen
python3 logosheet.py   # de logo-uitwerking en de SVG-bestanden in logo/
```

Vereist Chromium (pad staat in de scripts), de letters in `fonts/` en `fonttools` voor de
letteromtrekken. De scripts schrijven eerst HTML en printen die naar PDF.

`logo.py` bevat de meetkunde van het logo: één maat, de kapitaalhoogte, bepaalt alles.
Ringdikte, horizon, zonsradius, boogrijzing en overstek zijn daarvan afgeleid, dus een
wijziging in `PALETTEN` of `RING` werkt overal door.

## Uitgangspunten

- **Beeld.** Alle illustraties zijn vector en zelf getekend. Er is nog geen
  projectfotografie; nulfotografie en dronebeeld staan in fase 0 van het
  marketingplan. Bewust geen stockbeeld gebruikt.
- **Letters.** Fraunces, Inter, Archivo, Bricolage Grotesque en Newsreader vallen
  onder de SIL Open Font License en zijn vrij te gebruiken in druk en online.
- **Status.** De naam Hiero is een voorstel. Prijzen, woningaantallen per type en
  renovatiediepte staan nog niet vast.
