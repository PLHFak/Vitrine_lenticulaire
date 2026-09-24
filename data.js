// Données du dossier « Vitrine lenticulaire — Les Veilleurs ».
// Ce fichier est le seul à modifier pour mettre le site à jour :
// chaque commit sur GitHub redéploie automatiquement sur Vercel.

window.DATA = {
  version: "0.1",
  date: "25 septembre 2026",

  // ---- Contexte : les trois vues -----------------------------------------
  contexte: {
    intro: "L'écran lenticulaire est l'un des cinq éléments de l'œuvre : un panneau de 1 800 × 1 200 mm dressé face à la mer sur le socle monobloc, qui crée un effet d'invisibilité contre l'horizon. Les trois figures en bronze ne sont pas représentées sur ces vues.",
    vues: [
      { titre: "Rendu de l'ensemble", legende: "Socle, cadre de l'écran et niche des cristaux — maquette 3D J. Miceli, 24-09-26", img: "img/rendu_260924.jpeg" },
      { titre: "Ensemble base + écran + cristaux", legende: "Planche v01 du 22-09-26 — écran 1 800 × 1 200, 1 730 hors sol", img: "img/plan_ensemble.png", pdf: "docs/base_cplt_260922.pdf" },
      { titre: "Base monobloc V00", legende: "Comblanchien 6 720 kg — réservations 50 × 110 pour les montants", img: "img/plan_base.png", pdf: "docs/base_mono_bloc_V00.pdf" }
    ]
  },

  // ---- Fiche technique -----------------------------------------------------
  fiche: {
    "Dimensions": "1 800 × 1 200 mm hors socle, montants prolongés ≈ 500 mm",
    "Vitrage": "2 × verre feuilleté de sécurité 55.2, antireflet, PVB filtrant UV",
    "Lenticulaire": "PETG 6 mm, 20 LPI, libre — non collé",
    "Lame d'air": "≈ 7 mm, air sec ; sandwich ≈ 29 mm",
    "Étanchéité": "joint tubulaire Ø ≈ 10 vulcanisé en cadre fermé + cadre de positionnement",
    "Châssis": "U inox 316L 80 × 40 × 5 soudé laser (prédimensionné vent 220 km/h) — 100 × 40 × 3 dans la maquette V00 de Jacky",
    "Serrage": "entretoises à deux poussoirs taraudés, tige à pas contraires",
    "Protection": "balayage air sec par 2 tubes Ø4 à travers le joint, poche d'équilibrage + dessiccant"
  },

  // ---- Principe (sections) -------------------------------------------------
  principe: [
    {
      id: "sandwich", titre: "Le sandwich", img: "img/fig3_sandwich.png",
      texte: "Le film lenticulaire ne peut être laissé nu en front de mer. Il est pincé, sans collage, entre deux verres feuilletés 55.2 qui apportent la rigidité, la sécurité du public, l'étanchéité et le filtrage UV. Le PETG et le verre ne se dilatent pas de la même façon : un collage finirait par grisailler par décollements partiels, la plaque reste donc libre. Un joint tubulaire vulcanisé en cadre fermé rend la lame d'air étanche ; un cadre de positionnement, collé sur un verre, le tient en place et sert de butée d'écrasement.",
      pourquoi: "Un vitrier ne peut pas insérer une plaque lenticulaire dans un double vitrage scellé à coût raisonnable. On fabrique donc un double vitrage par construction, démontable."
    },
    {
      id: "air", titre: "La lame d'air : condensation et prolifération", img: "img/fig4_air_sec.png",
      texte: "Deux tubes Ø4 traversent le joint périphérique, en bas et en haut, dans la zone masquée par le châssis — aucun perçage du verre. En atelier, une pompe fait circuler quelques heures de l'air passé sur dessiccant jusqu'à remplacer l'air ambiant humide ; on peut y ajouter un agent antibactérien et fongicide, ou de l'azote sec. Sur site, le réseau reste relié à une poche souple contenant une réserve de dessiccant remplaçable.",
      pourquoi: "La poche équilibre en permanence la pression intérieure et extérieure : le joint périphérique n'est jamais sollicité, ni en pression ni en dépression."
    },
    {
      id: "chassis", titre: "Le châssis et le serrage", img: "img/fig2_coupe_montant.png",
      texte: "Cadre en U inox 316L, traverse basse soudée, traverse haute rapportée après insertion du sandwich. Dans le U, côté opposé au vitrage, des entretoises de pression : deux poussoirs taraudés (filet droit, filet gauche) écartés par une tige à pas contraires — un tour de tige écarte les deux poussoirs ensemble, principe du ridoir. Leur serrage plaque le sandwich contre l'aile opposée et comprime le joint jusqu'à la butée du cadre intérieur. Des rubans souples minces calent le verre et le laissent glisser (dilatation différentielle verre / inox). Un cache clipsé ferme le U.",
      pourquoi: "Les montants sont scellés ≈ 500 mm dans le socle de 6,7 t : la tenue au vent vient de l'encastrement, pas des angles du cadre. La triangulation par les verres suffit à rendre l'ensemble stable.",
      croquis: "img/croquis_260924.jpeg"
    },
    {
      id: "elevation", titre: "Élévation", img: "img/fig1_elevation.png",
      texte: "Cotes en mm. Le profil 80 × 40 est le schéma de principe ; il peut être porté à 100 × 40 si le calcul au vent l'exige, mais l'artiste préfère rester dans des dimensions discrètes."
    }
  ],

  // ---- Montage -------------------------------------------------------------
  montage: {
    img: "img/fig5_montage.png",
    etapes: [
      "En atelier, à plat sur table : premier verre, cadre de positionnement collé, joint tubulaire dans son logement, plaque lenticulaire déposée libre, second verre.",
      "Le sandwich est glissé dans les U des montants et de la traverse basse ; la traverse haute est fixée pour fermer le cadre.",
      "Serrage progressif des entretoises, en croix, jusqu'à la butée du cadre intérieur — pression homogène sur tout le périmètre.",
      "Balayage à l'air sec, raccordement de la poche d'équilibrage, contrôle d'étanchéité, pose des caches.",
      "Transport vertical, scellement des montants dans les réservations 50 × 110 du socle."
    ],
    unique: "Il ne s'agit pas d'un produit à industrialiser mais d'une pièce unique, qui peut rester artisanale. La mise en œuvre est fastidieuse, mais ce n'est pas un handicap pour un exemplaire. En contrepartie : démontable sur place, intérieur accessible en cas de défaut, lenticulaire remplaçable à moindre frais, maintenance préventive sans démontage (dessiccant, ré-injection d'air sec ou de biocide)."
  },

  // ---- Fournitures repérées ------------------------------------------------
  fournitures: [
    {
      groupe: "Profil U inox",
      items: [
        { nom: "Pliage sur mesure 316L 3 mm", detail: "La voie recommandée : un simple U 80 × 40 (ou 100 × 40) plié chez le tôlier qui fera le châssis. Permet de choisir librement la hauteur d'âme.", statut: "recommandé" },
        { nom: "Voss Inox — U plié 40×80×40×3, 1.4301, 6 m, 3,55 kg/m", detail: "Sur stock, mais en 304 : à réserver à un prototype d'atelier, pas à la pièce définitive.", url: "https://www.voss-edelstahl.com/online/fr/Acier-Inox/Profil-s-U/pli/", ref: "V0011309 (3 mm) · V0011310 (4 mm)" },
        { nom: "Atinox (Nazareth, BE) — profils U inox de stock, 316L sur demande", detail: "Fournisseur belge à consulter en premier pour une barre 316L.", url: "https://www.atinox.fr/rvs-produits/profil-u-inox-lamine-atinox-sa-304l-316l-sur-demander/" },
        { nom: "Montanstahl — UPN inox 304 / 316L, dimensions non standard sur demande", detail: "Profils soudés laser ; solution si l'on veut un profil épais, plus coûteuse.", url: "https://www.montanstahl.com/fr/produits/profils-marchands-et-barres-polies-en-acier-inoxydable/profils-u-en-acier-inoxydable/" }
      ]
    },
    {
      groupe: "Écarteurs à pas contraires (accastillage garde-corps câbles, inox 316)",
      items: [
        { nom: "Goujon double filet droite/gauche M6, 65 mm, inox 316", detail: "La tige de l'entretoise telle que dessinée : à monter entre deux poussoirs taraudés (un droit, un gauche), avec un méplat ou six pans usiné au centre. Un tour = 2 mm d'écartement.", url: "https://www.inoxdesign.fr/goujon-filete-m6-droite-gauche-pour-tendeur-cable-inox.html", statut: "recommandé" },
        { nom: "Tige filetée double pas M6 / M8, 65 mm, inox A4", detail: "Équivalent, en M8 pour plus de raideur.", url: "https://www.esse.fr/tiges-filetees/4034-tige-filetee-inox-double-pas-droite-gauche-m6-ou-m8.html" },
        { nom: "Tiges filetées 50 mm, pas droit ou pas gauche, M6 / M8, inox A4", detail: "Variante : deux tiges vissées à demeure dans les poussoirs et un écrou central tournant.", url: "https://esse.fr/visserie-inox/4132-tige-filetee-inox-316-a4-pas-droit-ou-gauche-m6-m8.html" },
        { nom: "Corps de tendeur à filetages intérieurs G/D — M6 92 mm Ø10, M8 112 mm Ø13,5", detail: "La variante « tige avec trou » ; trop long pour l'espace libre du U (≈ 45 mm) sans recoupe.", url: "https://www.rollingcenter-france.fr/cables-et-filets-inox/1252-tendeur-inox316-tar-drt-gch-m6x30-r5940006.html" }
      ]
    }
  ],

  // ---- Profil et vent --------------------------------------------------------
  vent: {
    intro: "Prédimensionnement du 25-09-26 pour un vent de 220 km/h (61 m/s, q = 2,3 kPa, cf = 1,8 panneau isolé) : effort sur l'écran 9,6 kN à 0,66 m, soit 6,4 kNm, 3,2 kNm par montant. Flèche en tête 7 mm avec le U de 5 mm. À confirmer par le bureau d'ossature.",
    profils: [
      { profil: "U 80×40×4 plié 316L", w: "14,7", kg: "4,8", sigma: "216 MPa (limite)", dispo: "pliage sur mesure" },
      { profil: "U 80×40×5 soudé laser 316L", w: "17,7", kg: "5,9", sigma: "180 MPa (OK, 20 % de marge)", dispo: "sur mesure — retenu" },
      { profil: "UPN 80 inox (80×45×6/8)", w: "26,5", kg: "8,6", sigma: "120 MPa", dispo: "catalogue, plus lourd" },
      { profil: "Tube 100×40×3 (maquette V00)", w: "—", kg: "—", sigma: "162 MPa", dispo: "référence Jacky" }
    ],
    conclusions: [
      "Encastrement 500 mm : pression sur la pierre ≈ 1,7 MPa, négligeable pour du Comblanchien.",
      "Bloc de 6,7 t : renversement 12,5 kNm contre 62 kNm stabilisant (sécurité 5) ; glissement 33 kN contre 14 kN. Le socle tient par sa masse.",
      "Verre : un 55.2 recuit est à la limite (≈ 23 MPa) — prévoir un feuilleté trempé, 66.2 trempé ≈ 16 MPa.",
      "Châssis v01 : hors tout 1 820 × 1 220, montants 1 720 dont 500 encastrés, réservation borgne 50 × 110 × 500, entraxe 1 780 (le plan V00 du socle, à 1 720, est à mettre à jour)."
    ],
    imgs: ["img/chassis_v01_U80x40.png", "img/step_v00_vues.png"]
  },

  // ---- Points ouverts ------------------------------------------------------
  ouverts: [
    "Section du profil : U 80 × 40 × 5 retenu en prédimensionnement, à confirmer par le bureau d'ossature.",
    "Verre : passer du 55.2 recuit à un feuilleté trempé (66.2) selon la note vent — à valider avec le vitrier et l'artiste (antireflet sur verre trempé).",
    "Hauteur du cadre de positionnement à caler sur l'épaisseur réelle du lenticulaire et sur la compression du joint (≈ 30 % pour Ø10).",
    "Matériau du cadre de positionnement et colle compatible PVB / PETG.",
    "Passage étanche des deux tubes à travers le joint (traversée vulcanisée ou collée).",
    "Choix du fluide de balayage (air sec, azote) et de l'agent biocide compatible PETG.",
    "Emplacement de la poche d'équilibrage (montant creux ou réservation dans le socle) et accès pour l'entretien.",
    "Poussoirs en inox 316 ou en polymère (POM / PE) pour éviter tout couple galvanique dans le U ; taraudage M6 pas à gauche à préciser à l'atelier.",
    "Validation sur prototype grandeur réelle avant toute commande."
  ],

  // ---- Téléchargements -----------------------------------------------------
  docs: [
    { titre: "Note de principe — vitrine lenticulaire v01 (PDF, 7 p.)", fichier: "docs/note_vitrine_lenticulaire_v01.pdf" },
    { titre: "Ensemble base + écran + cristaux (v01 260922)", fichier: "docs/base_cplt_260922.pdf" },
    { titre: "Base mono bloc V00 — plan coté (J. Miceli, 22-09-26)", fichier: "docs/base_mono_bloc_V00.pdf" },
    { titre: "STEP — ecran v00 100x40x3 (J. Miceli, Inventor, 24-09-26)", fichier: "docs/cao/ecran_v00_100x40x3.stp" },
    { titre: "STL — châssis v01 U 80×40×5 (25-09-26)", fichier: "docs/cao/ecran_v01_U80x40.stl" }
  ],

  // ---- Prompt CAO ------------------------------------------------------------
  prompt: `Contexte. Œuvre d'art permanente en front de mer (Westende, Belgique). Modéliser l'assemblage d'une vitrine lenticulaire : un sandwich verre / lenticulaire / verre de 1800 × 1200 mm maintenu par un châssis inox en U, encastré 500 mm dans un socle en pierre. Livrable 1 : planche PDF A3 (élévation, vue latérale, coupe horizontale dans un montant échelle 1:1, coupe verticale dans la traverse basse, éclaté d'assemblage, nomenclature). Livrable 2 : assemblage STEP AP214 paramétrique, une pièce par composant, cotes en mm.

Composants et cotes.
1. Verre feuilleté 55.2 (5 + 0,76 + 5 = 10,76 mm), 1800 × 1200, × 2, antireflet, sans perçage.
2. Plaque lenticulaire PETG 6 mm, 1710 × 1110, libre, centrée entre les verres.
3. Joint tubulaire souple Ø10, cadre fermé rectangulaire, axe à 45 mm du bord du verre, comprimé à 7 mm ; deux tubes Ø4 le traversent (un en bas à droite, un en haut à gauche).
4. Cadre de positionnement, section 6 × 7 mm, cadre fermé juste à l'intérieur du joint, collé sur le verre côté socle.
5. Profil U inox 316L 80 × 40 × 3 (paramètre : hauteur d'âme 80 ou 100), ouverture du U vers le centre du panneau ; deux montants de 1200 + 500 mm, traverse basse de 1800 mm soudée, traverse haute de 1800 mm rapportée (boulonnée, coupe droite).
6. Ruban souple 1,5 mm entre le verre et l'aile du U, et entre le verre et l'entretoise.
7. Entretoises de pression : deux poussoirs de 12 mm d'épaisseur sur toute la profondeur libre du U, chacun taraudé (M6 filet droit dans l'un, M6 filet gauche dans l'autre), écartés par un goujon double filet M6 × 65 avec six pans central (type ridoir) ; une entretoise tous les 300 mm sur le périmètre ; le poussoir inférieur est collé sur l'aile du U.
8. Cache de finition clipsé de 2 mm fermant l'ouverture du U sur la hauteur des entretoises.
9. Circuit d'air : deux tubes Ø4 partant des traversées du joint, cheminant dans le U, jusqu'à une poche souple (volume de 1 L) et une cartouche de dessiccant logées dans le montant droit sous le niveau du socle.
10. Socle : représenter seulement une portion du monobloc (2750 × 527 × 400 mm) avec deux réservations 50 × 110 × 500 mm pour les montants, entraxe 1760 mm.

Règles. Le sandwich est plaqué contre l'aile du U côté extérieur, les entretoises côté intérieur. Aucun collage entre lenticulaire et verre, aucun perçage du verre. Cotes fonctionnelles à faire apparaître : 1800, 1200, 500, 80 (ou 100), 40, épaisseur sandwich ≈ 29. Nommer les pièces en français. Produire d'abord la planche PDF pour validation, puis le STEP.`,

  // ---- Journal -------------------------------------------------------------
  journal: [
    { date: "24-09-26", texte: "Principe constructif dicté par P. L'Hoest ; croquis de la coupe dans le montant ; note v01 produite." },
    { date: "24-09-26", texte: "Corrections : tubes d'air à travers le joint (plus de perçage du verre), lenticulaire 6 mm, poussoirs taraudés à pas contraires." },
    { date: "25-09-26", texte: "Recherche fournitures : U inox plié 80×40×3, écarteurs double filet inox 316." },
    { date: "25-09-26", texte: "STEP de Jacky (ecran v00 100x40x3) reçu et analysé ; châssis v01 U 80×40×5 et note vent 220 km/h ; mise en ligne du site, v0.1." }
  ]
};
