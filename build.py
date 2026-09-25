# Génère vignettes (docs/thumbs), PDF avec cartouche des schémas (docs/pdf), PNG des plans du socle (docs/png) et docs/sizes.js. Lancer depuis la racine du dépôt.
# lv_build.py est commun aux trois dépôts (identique).
from lv_build import thumb, stamp_pdf, pdf_to_png, sizes, now_be
URL = "https://vitrine-lenticulaire.vercel.app"
OBJ = "Double vitrage démontable, lenticulaire libre, châssis U inox"
thumb("docs/note_vitrine_lenticulaire_v01.pdf", "docs/thumbs/note_v01.jpg")
DRAW = [
 ("img/fig1_elevation.png","fig1_elevation","LV-VL-FIG-01","1","24-09-26","ESQUISSE","Élévation, cotes en mm","elevation"),
 ("img/fig2_coupe_montant.png","fig2_coupe_montant","LV-VL-FIG-02","1","24-09-26","ESQUISSE","Coupe horizontale dans un montant","coupe_montant"),
 ("img/fig3_sandwich.png","fig3_sandwich","LV-VL-FIG-03","1","24-09-26","ESQUISSE","Le sandwich verre / lenticulaire / verre","sandwich"),
 ("img/fig4_air_sec.png","fig4_air_sec","LV-VL-FIG-04","1","24-09-26","ESQUISSE","Circuit d'air sec, poche d'équilibrage et dessiccant","air_sec"),
 ("img/fig5_montage.png","fig5_montage","LV-VL-FIG-05","1","24-09-26","ESQUISSE","Séquence de montage","montage"),
 ("img/croquis_260924.jpeg","croquis","LV-VL-CRQ-01","1","24-09-26","ESQUISSE","Croquis de principe d'origine — coupe dans le montant","croquis"),
 ("img/chassis_v01_U80x40.png","chassis_v01","LV-VL-CH-01","1","25-09-26","ÉTUDE","Châssis v01 U 80×40×5 316L — trois vues","chassis_v01"),
 ("img/step_v00_vues.png","step_v00","LV-VL-CAO-00","0","24-09-26","ÉTUDE","STEP « ecran v00 100x40x3 » (J. Miceli) — trois vues","step_v00_vues"),
]
for src, th, num, rev, date, statut, titre, suf in DRAW:
    thumb(src, f"docs/thumbs/{th}.jpg")
    stamp_pdf(src, f"docs/pdf/{num}_{suf}.pdf", dict(titre="La vitrine lenticulaire — "+titre, num=num, rev=rev, date=date, statut=statut, objet=OBJ, url=URL))
for pdf, out in [("docs/base_mono_bloc_V00.pdf","base_mono_bloc_V00"),("docs/base_cplt_260922.pdf","base_cplt_260922")]:
    pdf_to_png(pdf, f"docs/png/{out}.png")
    thumb(pdf, f"docs/thumbs/{'base_V00' if 'V00' in out else 'base_cplt'}.jpg")
S = sizes(".")
print(len(S), "fichiers mesurés ·", now_be())
