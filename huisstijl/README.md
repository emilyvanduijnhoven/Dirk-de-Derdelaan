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

## Opnieuw genereren

```
python3 build.py
```

Vereist `pymupdf` niet — alleen Chromium (pad staat in `build.py`) en de letters in
`fonts/`. Het script schrijft eerst een HTML per richting en print die naar PDF.

## Uitgangspunten

- **Beeld.** Alle illustraties zijn vector en zelf getekend. Er is nog geen
  projectfotografie; nulfotografie en dronebeeld staan in fase 0 van het
  marketingplan. Bewust geen stockbeeld gebruikt.
- **Letters.** Fraunces, Inter, Archivo, Bricolage Grotesque en Newsreader vallen
  onder de SIL Open Font License en zijn vrij te gebruiken in druk en online.
- **Status.** De naam Hiero is een voorstel. Prijzen, woningaantallen per type en
  renovatiediepte staan nog niet vast.
