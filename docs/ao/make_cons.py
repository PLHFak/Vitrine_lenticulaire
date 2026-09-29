# Dossier de consultation LV-VL-CONS-01 — châssis de l'écran (lot 2b) — FR et EN
import datetime, zoneinfo
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ACC = HexColor("#5a7d8c"); MUTE = HexColor("#7a7a7a"); LINE = HexColor("#d9d2c3"); INK = HexColor("#2b2b2b"); BG = HexColor("#f3f0e8")
IMG = "/home/claude/plhfak/Vitrine_lenticulaire/img/"
NOW = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Brussels")).strftime("%d-%m-%Y · %H:%M")

T = {
 "FR": dict(
  lang="FR", num="LV-VL-CONS-01", rev="v01", statut="CONSULTATION",
  doc="Châssis de l'écran — consultation", objet="Châssis tube inox 316L, deux montants scellés",
  proj="PROJET", art="ARTISTE · MAÎTRE D'ŒUVRE", asst="ASSISTANT ÉLECTROMÉCANIQUE", docl="DOCUMENT", objl="OBJET",
  numl="N° DOCUMENT", revl="RÉVISION", datel="DATE · HEURE", statl="STATUT", pagel="PAGE",
  legal="© Eva L'Hoest 2026 — Confidentiel. Reproduction, diffusion ou usage hors de cette consultation interdits sans accord écrit de l'artiste. Cotes non contractuelles.",
  title="Les Veilleurs — Châssis de l'écran lenticulaire",
  sub="Dossier de consultation v01 · septembre 2026 · métallerie inox — demande d'avis constructif et d'offre de prix",
  s1="1. De quoi s'agit-il",
  p1="Une œuvre d'art permanente sur la côte belge (Beaufort 27, mer du Nord), garantie dix ans en milieu marin. Sur un socle monobloc en pierre claire se dresse un écran de 1,8 × 1,2 m : un panneau lenticulaire pris entre deux verres feuilletés, qui joue avec l'horizon. Nous cherchons un atelier pour fabriquer le châssis qui porte cet écran : un cadre rectangulaire en tube inox 316L, dont les deux montants sont prolongés et scellés dans le socle. C'est une pièce unique, simple à souder, faite pour durer dehors. Le vitrage n'est pas dans cette consultation. Les cotes ci-dessous sont notre proposition : votre avis sur ce qui est plus simple, plus sûr ou moins cher à fabriquer nous intéresse autant que votre prix.",
  s2="2. Cotes principales",
  th=("Élément", "Cote / valeur", "Remarque"),
  rows=[
   ("Profil", "tube rectangulaire 80 × 40 × 3 mm, inox 316L", "grand côté (80) dans le sens du vent ; 4 mm acceptable si vous le jugez préférable, à indiquer"),
   ("Largeur hors tout", "1 890 mm", "entre montants : 1 810"),
   ("Montants", "2 × 1 728 mm", "1 200 visibles + 528 scellés dans le socle"),
   ("Traverse basse", "1 810 mm, soudée", "son dessus affleure le dessus du socle"),
   ("Traverse haute", "1 810 mm, rapportée", "boulonnée après insertion du vitrage ; assemblage à proposer"),
   ("Ouverture libre", "1 810 × 1 120 mm", "reçoit un sandwich verre / lenticulaire / verre d'environ 30 mm"),
   ("Réception du vitrage", "à l'extérieur du tube, côté mer", "proposition : parclose plat 40 × 6 vissée, bandes souples 2 mm, aucun contact verre / métal — voir § 3.3"),
   ("Scellement", "2 réservations ≈ 50 × 90 × 528 dans la pierre", "résine ou mortier de scellement ; taillées par l'atelier de pierre sur vos cotes finales"),
   ("Masse", "≈ 37 kg (7,1 m de tube)", "manutention à deux, sans engin"),
   ("Finition", "brossée, bouts de tube fermés", "à échantillonner ; cordons visibles meulés et brossés"),
  ],
  s3="3. Description pièce par pièce",
  d=[("3.1 Montants et traverse basse", "Trois tubes 80 × 40 × 3 en 316L, assemblés en U par deux soudures d'angle (onglet ou coupe droite, à votre choix), cordons continus, pénétration complète en pied de montant. Les montants sont fermés en tête et en pied par une plaque soudée de 3 mm ; aucune eau ne doit pouvoir entrer dans les tubes. La partie scellée (528 mm) peut rester brute ; deux goujons ou tiges soudés en travers améliorent l'ancrage dans la résine."),
     ("3.2 Traverse haute rapportée", "Tube identique, fixé en tête des montants par un assemblage démontable (platines et boulons inox A4, ou embouts glissants goupillés). Il n'a pas besoin d'être rigide : une fois le vitrage serré, le sandwich triangule le cadre. L'assemblage doit rester discret vu de face : proposez-nous le vôtre."),
     ("3.3 Réception du vitrage (proposition)", "Le sandwich verre / lenticulaire / verre (≈ 1 800 × 1 200 × 30 mm, ≈ 60 kg, fourni par le lot vitrage) vient s'appliquer contre la face extérieure du cadre, côté mer, sur une bande souple autocollante de 2 mm. Il est retenu par un cadre de parcloses en plat inox 40 × 6 vissé dans le tube (vis fraisées Torx A4, pas ≈ 200), avec une seconde bande souple entre la parclose et le verre. Aucune vis ne traverse le verre ; le vitrage reste démontable sur place. Si vous connaissez une solution plus simple ou plus élégante (cornière, profil de battée, feuillard), elle est la bienvenue."),
     ("3.4 Tenue au vent et scellement", "Front de mer : le châssis est tenu par l'encastrement des montants, pas par les angles du cadre. Le socle en pierre (≈ 6,7 t) reçoit deux réservations verticales de 528 mm ; le scellement se fait à la résine ou au mortier après réglage d'aplomb. Le prédimensionnement au vent a été fait par nos soins et sera confirmé par le bureau d'ossature ; si vous préférez une épaisseur de 4 mm, dites-le et chiffrez les deux."),
     ("3.5 Ce que nous vous demandons", "Une offre en € HT pour la fourniture du châssis : tubes, traverse haute démontable, parcloses et bandes souples (ou votre alternative), certificat matière 3.1, finition. En option : transport et pose des montants dans le socle à Westende (scellement compris). Merci d'indiquer votre délai à partir de la commande, vos hypothèses et tout point du dossier qui vous paraît discutable."),
  ],
  s4="4. Points ouverts",
  open_=["Épaisseur du tube (3 ou 4 mm) : à votre appréciation, offre pour les deux bienvenue.",
         "Assemblage de la traverse haute : platines boulonnées ou embouts glissants.",
         "Détail de réception du vitrage : notre parclose 40 × 6 est une proposition ; votre solution habituelle nous intéresse.",
         "Le sandwich vitré fera 29 ou 32 mm selon le verre retenu (55.2 ou 66.2) : la parclose doit s'en accommoder.",
         "Le socle est en cours d'étude ; les cotes de réservation seront figées avec le plan de socle V01."],
  note="Les plans de ce dossier ont été établis avec l'aide de l'intelligence artificielle, sous le contrôle de l'équipe. Nous sommes ouverts à vous confier le plan de réalisation, ou à travailler avec le bureau d'études que vous nous suggérez.",
  s5="5. Figures",
  figs=[("rendu_260924.jpeg", "Fig. 1 — Rendu d'ensemble : socle, écran et niche des cristaux (les figures en bronze ne sont pas représentées)."),
        ("plan_ensemble.png", "Fig. 2 — Implantation de l'écran sur le socle."),
        ("/home/claude/out/ch02.png", "Fig. 3 — Châssis v02 : élévation, vue latérale, section du montant, nomenclature (LV-VL-CH-02)."),
        ("step_v00_vues.png", "Fig. 4 — Maquette 3D de J. Miceli (STEP ecran v00) : même géométrie, profil ramené de 100 × 40 à 80 × 40 × 3."),
        ("fig3_sandwich.png", "Fig. 5 — Le sandwich verre / lenticulaire / verre reçu par le châssis (pour information, lot vitrage)."),
  ],
  s6="6. Documents et liens",
  links=["Dossier Drive (présentation, plans, CAO) : https://drive.google.com/drive/folders/1gwChq_mJxhfM1suTWyyN8btA9JSbgtrG",
         "Site technique de la vitrine : https://vitrine-lenticulaire.vercel.app/?code=EVA",
         "Maquette 3D interactive de l'ensemble : https://base-les-veilleurs.vercel.app/monobloc.html?code=EVA",
         "Contact : Production Office — Eva L'Hoest / EHLAB SRL — eva.production.bx@gmail.com ; questions techniques : Gioacchino Miceli."],
 ),
 "EN": dict(
  lang="EN", num="LV-VL-CONS-01", rev="v01", statut="CONSULTATION",
  doc="Screen frame — request for quotation", objet="316L stainless tube frame, two uprights set in stone",
  proj="PROJECT", art="ARTIST · PROJECT LEAD", asst="ELECTROMECHANICAL ASSISTANT", docl="DOCUMENT", objl="SUBJECT",
  numl="DOCUMENT No.", revl="REVISION", datel="DATE · TIME", statl="STATUS", pagel="PAGE",
  legal="© Eva L'Hoest 2026 — Confidential. Reproduction, distribution or use outside this consultation is prohibited without the artist's written consent. Dimensions not contractual.",
  title="Les Veilleurs — Frame of the lenticular screen",
  sub="Consultation file v01 · September 2026 · stainless steel fabrication — request for constructive advice and quotation",
  s1="1. What it is",
  p1="A permanent artwork on the Belgian coast (Beaufort 27, North Sea), guaranteed for ten years in a marine environment. On a monolithic light-stone base stands a 1.8 × 1.2 m screen: a lenticular panel held between two laminated glass panes, playing with the horizon. We are looking for a workshop to make the frame that carries this screen: a rectangular frame in 316L stainless steel tube, whose two uprights extend down and are set into the stone base. It is a one-off piece, simple to weld, built to last outdoors. The glazing is not part of this consultation. The dimensions below are our proposal: your view on what is simpler, safer or cheaper to make interests us as much as your price.",
  s2="2. Main dimensions",
  th=("Item", "Dimension / value", "Remark"),
  rows=[
   ("Section", "rectangular tube 80 × 40 × 3 mm, 316L stainless", "80 mm side facing the wind; 4 mm acceptable if you consider it preferable — please say so"),
   ("Overall width", "1,890 mm", "between uprights: 1,810"),
   ("Uprights", "2 × 1,728 mm", "1,200 visible + 528 set into the base"),
   ("Bottom rail", "1,810 mm, welded", "its top face is flush with the top of the base"),
   ("Top rail", "1,810 mm, removable", "bolted after the glazing is inserted; connection to be proposed"),
   ("Clear opening", "1,810 × 1,120 mm", "receives a glass / lenticular / glass sandwich of about 30 mm"),
   ("Glazing support", "outside the tube, sea side", "proposal: 40 × 6 flat-bar bead screwed on, 2 mm soft strips, no glass-to-metal contact — see § 3.3"),
   ("Anchoring", "2 pockets ≈ 50 × 90 × 528 in the stone", "resin or grout; cut by the stone workshop to your final dimensions"),
   ("Mass", "≈ 37 kg (7.1 m of tube)", "two-person handling, no lifting gear"),
   ("Finish", "brushed, tube ends closed", "sample to be agreed; visible welds ground and brushed"),
  ],
  s3="3. Part-by-part description",
  d=[("3.1 Uprights and bottom rail", "Three 80 × 40 × 3 tubes in 316L, assembled as a U with two corner welds (mitred or square cut, your choice), continuous seams, full penetration at the foot of the uprights. Uprights are closed top and bottom by a welded 3 mm plate; no water may enter the tubes. The embedded part (528 mm) may stay as-welded; two studs or cross bars welded on improve the anchorage in the resin."),
     ("3.2 Removable top rail", "Same tube, fixed to the heads of the uprights by a demountable connection (stainless A4 plates and bolts, or sliding pinned inserts). It does not need to be rigid: once the glazing is clamped, the sandwich braces the frame. The connection should stay discreet when seen from the front: propose yours."),
     ("3.3 Glazing support (proposal)", "The glass / lenticular / glass sandwich (≈ 1,800 × 1,200 × 30 mm, ≈ 60 kg, supplied by the glazing lot) bears against the outer face of the frame, sea side, on a 2 mm self-adhesive soft strip. It is retained by a bead frame of 40 × 6 stainless flat bar screwed into the tube (countersunk Torx A4 screws, pitch ≈ 200), with a second soft strip between bead and glass. No screw passes through the glass; the glazing stays removable on site. If you know a simpler or more elegant solution (angle, rebate profile, strip), it is welcome."),
     ("3.4 Wind and anchoring", "Seafront: the frame is held by the embedment of the uprights, not by the frame corners. The stone base (≈ 6.7 t) receives two vertical pockets 528 mm deep; anchoring is done with resin or grout after plumbing. We have pre-sized the frame for wind and the structural engineer will confirm it; if you would rather use 4 mm wall, say so and price both."),
     ("3.5 What we ask of you", "A quotation (excl. VAT) for the supply of the frame: tubes, removable top rail, beads and soft strips (or your alternative), 3.1 material certificate, finish. As an option: transport and setting of the uprights into the base at Westende (grouting included). Please state your lead time from order, your assumptions and any point of the file you find questionable."),
  ],
  s4="4. Open points",
  open_=["Tube wall (3 or 4 mm): your call; a quotation for both is welcome.",
         "Top-rail connection: bolted plates or sliding inserts.",
         "Glazing support detail: our 40 × 6 bead is a proposal; your usual solution interests us.",
         "The glazed sandwich will be 29 or 32 mm depending on the glass chosen (55.2 or 66.2): the bead must accommodate this.",
         "The base is still being studied; pocket dimensions will be frozen with base drawing V01."],
  note="The drawings in this file were prepared with the help of artificial intelligence, under the team's control. We are open to entrusting you with the shop drawings, or to working with the engineering office you suggest.",
  s5="5. Figures",
  figs=[("rendu_260924.jpeg", "Fig. 1 — Overall rendering: base, screen and crystal niche (bronze figures not shown)."),
        ("plan_ensemble.png", "Fig. 2 — Position of the screen on the base."),
        ("/home/claude/out/ch02.png", "Fig. 3 — Frame v02: elevation, side view, upright section, parts list (LV-VL-CH-02; drawing labelled in French)."),
        ("step_v00_vues.png", "Fig. 4 — 3D model by J. Miceli (STEP ecran v00): same geometry, section reduced from 100 × 40 to 80 × 40 × 3."),
        ("fig3_sandwich.png", "Fig. 5 — The glass / lenticular / glass sandwich received by the frame (for information, glazing lot)."),
  ],
  s6="6. Documents and links",
  links=["Drive folder (presentation, drawings, CAD): https://drive.google.com/drive/folders/1gwChq_mJxhfM1suTWyyN8btA9JSbgtrG",
         "Technical site of the screen: https://vitrine-lenticulaire.vercel.app/?code=EVA",
         "Interactive 3D model of the whole piece: https://base-les-veilleurs.vercel.app/monobloc.html?code=EVA",
         "Contact: Production Office — Eva L'Hoest / EHLAB SRL — eva.production.bx@gmail.com; technical questions: Gioacchino Miceli."],
 ),
}

def build(L, out):
    W, H = A4; m = 18 * mm; cart_h = 31 * mm
    st = dict(
        h1=ParagraphStyle("h1", fontName="Times-Bold", fontSize=17, leading=21, textColor=INK, spaceAfter=3),
        sub=ParagraphStyle("sub", fontName="Times-Italic", fontSize=9.5, leading=12, textColor=MUTE, spaceAfter=10),
        h2=ParagraphStyle("h2", fontName="Times-Bold", fontSize=12.5, leading=16, textColor=ACC, spaceBefore=9, spaceAfter=4),
        p=ParagraphStyle("p", fontName="Times-Roman", fontSize=10, leading=13.5, textColor=INK, spaceAfter=5),
        pd=ParagraphStyle("pd", fontName="Times-Roman", fontSize=10, leading=13.5, textColor=INK, spaceAfter=6),
        tb=ParagraphStyle("tb", fontName="Times-Roman", fontSize=8.8, leading=11, textColor=INK),
        tbh=ParagraphStyle("tbh", fontName="Times-Bold", fontSize=8.8, leading=11, textColor=white),
        cap=ParagraphStyle("cap", fontName="Times-Italic", fontSize=8.5, leading=11, textColor=MUTE, spaceAfter=8),
        bul=ParagraphStyle("bul", fontName="Times-Roman", fontSize=10, leading=13.5, textColor=INK, leftIndent=10, bulletIndent=0, spaceAfter=2),
        note=ParagraphStyle("note", fontName="Times-Italic", fontSize=9.5, leading=12.5, textColor=INK, backColor=BG, borderPadding=6, spaceBefore=6, spaceAfter=8),
    )
    def footer(c, doc):
        c.saveState(); aw = W - 2 * m; y0 = m - 4 * mm
        cols = [0.37, 0.37, 0.26]; xs = [m]
        for f in cols: xs.append(xs[-1] + aw * f)
        c.setStrokeColor(black); c.setLineWidth(0.7); c.rect(m, y0, aw, cart_h)
        for xx in xs[1:-1]: c.line(xx, y0, xx, y0 + cart_h)
        def k(x, y, s): c.setFillColor(MUTE); c.setFont("Helvetica", 5.3); c.drawString(x, y, s)
        def v(x, y, s, b=False, sz=7.2): c.setFillColor(INK); c.setFont("Helvetica-Bold" if b else "Helvetica", sz); c.drawString(x, y, s)
        p = 6; yt = y0 + cart_h - 11
        x1 = xs[0] + p
        k(x1, yt + 3, L["proj"]); v(x1, yt - 6, "LES VEILLEURS — Beaufort 27", True, 8.5)
        k(x1, yt - 17, L["art"]); v(x1, yt - 26, "Eva L'Hoest · +32 495 57 92 12 · eva.lhoest@gmail.com", sz=6.3)
        k(x1, yt - 37, L["asst"]); v(x1, yt - 46, "Gioacchino Miceli · +32 497 84 45 10", sz=6.8); v(x1, yt - 54, "gioacchino.miceli@thefaktory.com", sz=6.8)
        k(x1, yt - 65, "Production Office"); v(x1, yt - 73, "Eva L'Hoest / EHLAB SRL · eva.production.bx@gmail.com", sz=6.1)
        x2 = xs[1] + p
        k(x2, yt + 3, L["docl"]); v(x2, yt - 6, L["doc"], True, 8)
        k(x2, yt - 17, L["objl"]); v(x2, yt - 26, L["objet"], sz=6.8)
        k(x2, yt - 37, L["numl"]); v(x2, yt - 46, L["num"], True, 7.5)
        k(x2 + 80, yt - 37, L["revl"]); v(x2 + 80, yt - 46, L["rev"], sz=7.2)
        k(x2 + 118, yt - 37, L["datel"]); v(x2 + 118, yt - 46, NOW, sz=6.6)
        x3 = xs[2] + p
        k(x3, yt + 3, L["statl"]); c.setStrokeColor(ACC); c.setFillColor(ACC); c.setFont("Helvetica-Bold", 7.5)
        sw = c.stringWidth(L["statut"], "Helvetica-Bold", 7.5) + 10; c.rect(x3, yt - 10, sw, 12); c.drawString(x3 + 5, yt - 7, L["statut"])
        k(x3 + sw + 14, yt + 3, L["pagel"]); v(x3 + sw + 14, yt - 7, f"{doc.page} / {doc.total}" if hasattr(doc, "total") else str(doc.page), True, 8)
        c.setFillColor(MUTE); c.setFont("Helvetica", 5.4)
        words = L["legal"].split(); lines = []; cur = ""
        for w in words:
            t = (cur + " " + w).strip()
            if c.stringWidth(t, "Helvetica", 5.4) <= xs[3] - x3 - p: cur = t
            else: lines.append(cur); cur = w
        lines.append(cur)
        for i, ln in enumerate(lines): c.drawString(x3, yt - 24 - i * 6.8, ln)
        c.restoreState()

    class Doc(SimpleDocTemplate):
        pass
    def make(total=None):
        doc = Doc(out, pagesize=A4, leftMargin=m, rightMargin=m, topMargin=m, bottomMargin=m + cart_h + 2 * mm,
                  title=L["title"], author="Eva L'Hoest", subject=L["objet"])
        if total: doc.total = total
        S = []
        S.append(Paragraph(L["title"], st["h1"])); S.append(Paragraph(L["sub"], st["sub"]))
        S.append(Paragraph(L["s1"], st["h2"])); S.append(Paragraph(L["p1"], st["p"]))
        S.append(Paragraph(L["s2"], st["h2"]))
        data = [[Paragraph(h, st["tbh"]) for h in L["th"]]] + [[Paragraph(c, st["tb"]) for c in r] for r in L["rows"]]
        aw = W - 2 * m
        t = Table(data, colWidths=[aw * 0.24, aw * 0.33, aw * 0.43], repeatRows=1)
        t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), ACC), ("GRID", (0, 0), (-1, -1), 0.4, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, BG])]))
        S.append(t)
        S.append(Paragraph(L["s3"], st["h2"]))
        for h, p in L["d"]: S.append(Paragraph(f"<b>{h}</b> — {p}", st["pd"]))
        S.append(Paragraph(L["s4"], st["h2"]))
        for o in L["open_"]: S.append(Paragraph(o, st["bul"], bulletText="–"))
        S.append(Paragraph(L["note"], st["note"]))
        S.append(Paragraph(L["s5"], st["h2"]))
        from PIL import Image as PI
        for f, cap in L["figs"]:
            path = f if f.startswith("/") else IMG + f
            im = PI.open(path); r = im.height / im.width
            w = aw if r < 0.5 else aw * 0.9
            h = w * r
            if h > 118 * mm: h = 118 * mm; w = h / r
            S.append(KeepTogether([Image(path, w, h), Paragraph(cap, st["cap"])]))
        S.append(Paragraph(L["s6"], st["h2"]))
        for l in L["links"]: S.append(Paragraph(l, st["bul"], bulletText="–"))
        doc.build(S, onFirstPage=footer, onLaterPages=footer)
        return doc.page
    n = make(); make(n)

build(T["FR"], "/home/claude/out/LV-VL-CONS-01_chassis_ecran_v01_FR.pdf")
build(T["EN"], "/home/claude/out/LV-VL-CONS-01_chassis_ecran_v01_EN.pdf")
print("ok")
