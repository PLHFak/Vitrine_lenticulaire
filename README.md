# La vitrine lenticulaire — Les Veilleurs

Note de principe et dossier de fabrication du double vitrage démontable de l'écran lenticulaire (site statique).

- `data.js` — tout le contenu : contexte, fiche, principe, montage, profil & vent, fournitures, points ouverts, documents, prompt CAO, journal
- `img/` — figures de principe, croquis, châssis v01, vues du STEP v00
- `docs/` — note v01 (PDF), note vent (MD), PDF cartouchés des schémas (`docs/pdf/`), CAO (`docs/cao/` : STEP v00 de J. Miceli, STL châssis v01), plans du socle
- `vercel.json` — déploiement Vercel (preset Other), noindex

Site : https://vitrine-lenticulaire.vercel.app (à importer sur Vercel depuis ce dépôt). Lien direct : https://vitrine-lenticulaire.vercel.app/?code=EVA

## Charte commune aux trois dossiers

Les trois sites (`Base_les_veilleurs`, `Vitrine_lenticulaire`, `Aquarium-K9`) partagent le même gabarit :

- `lv.css` et `lv.js` — styles, barre de titre (liens vers les trois dossiers, onglets de langue), cartouche technique, cartes « Documents ». **Ces deux fichiers doivent rester identiques dans les trois dépôts** : toute modification se recopie dans les deux autres.
- `data.js` — le seul fichier de contenu. Chaque texte est donné dans les quatre langues avec `L("fr","en","nl","de")` ; les schémas et plans restent légendés en français.
- `index.html` — gabarit et rendu des sections propres au dossier (ne porte pas de contenu).
- `build.py` — génère les vignettes (`docs/thumbs/`), les PDF avec cartouche des schémas (`docs/pdf/`), les PNG des plans (`docs/png/`) et `docs/sizes.js`. S'appuie sur `lv_build.py` (commun, identique dans les trois dépôts ; Pillow, reportlab, pdftoppm).

Langue : onglets FR / EN / NL / DE en haut de page, ou `?lang=en` dans le lien ; le choix est mémorisé dans le navigateur.

Accès : code `EVA` (côté client, `lv.js`), ou `?code=EVA` dans le lien. Pages en `noindex`.


## Mesure d'audience (chapitre « Fréquentation »)

- `api/hit.js` — reçoit les mesures du navigateur sur le même domaine que le site (rien vers un tiers ; échec silencieux). Pas d'IP ni de cookie : site, langue, page, document téléchargé, pays/ville (en-têtes Vercel), appareil, durée.
- `api/stats.js` — statistiques ; le code administrateur est vérifié dans la base (fonction `lv_stats`), jamais côté client.
- `api/_cfg.js` — URL et clé *anon* Supabase (variables Vercel `SUPABASE_URL` / `SUPABASE_ANON_KEY` prioritaires).
- `docs/lv_analytics.sql` — à exécuter une fois dans Supabase (tables `lv_hits`, `lv_config` avec le code administrateur, fonction `lv_stats`). Commun aux trois sites.
- Le chapitre apparaît en bas de page quand le site est ouvert avec le code administrateur (saisi au clavier ; il n'est jamais mis dans un lien). Les visites administrateur ne sont pas comptées.
