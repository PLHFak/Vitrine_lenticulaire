# Dessin LV-VL-CH-02 : châssis v02 tube 80x40x3 316L — élévation, vue latérale, section, encastrement
import sys, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
sys.path.insert(0, "/home/claude/plhfak/Vitrine_lenticulaire")
from lv_build import stamp_pdf

INK = "#2b2b2b"; ACC = "#5a7d8c"; STONE = "#d9d2c3"; GLASS = "#cfe0ea"; MUTE = "#7a7a7a"
plt.rcParams.update({"font.family": "serif", "font.size": 12, "text.color": INK})
fig = plt.figure(figsize=(16, 10.5), dpi=100, facecolor="white")

def dim(ax, x0, y0, x1, y1, text, off=0, side="h", fs=11):
    if side == "h":
        y = y0 + off
        ax.annotate("", (x0, y), (x1, y), arrowprops=dict(arrowstyle="<->", lw=0.7, color=INK))
        ax.plot([x0, x0], [y0, y], lw=0.4, color=MUTE); ax.plot([x1, x1], [y1, y], lw=0.4, color=MUTE)
        ax.text((x0 + x1) / 2, y + 12, text, ha="center", va="bottom", fontsize=fs)
    else:
        x = x0 + off
        ax.annotate("", (x, y0), (x, y1), arrowprops=dict(arrowstyle="<->", lw=0.7, color=INK))
        ax.plot([x0, x], [y0, y0], lw=0.4, color=MUTE); ax.plot([x1, x], [y1, y1], lw=0.4, color=MUTE)
        ax.text(x + 12, (y0 + y1) / 2, text, ha="left", va="center", fontsize=fs, rotation=90)

# ---------- Élévation ----------
ax = fig.add_axes([0.02, 0.10, 0.46, 0.84]); ax.set_aspect("equal"); ax.axis("off")
W, Hv, Emb, T = 1890, 1200, 528, 40           # hors tout, hauteur visible, encastrement, largeur de tube vue de face
socle_top = 0
# socle
ax.add_patch(Rectangle((-400, -Emb - 60), W + 800, Emb + 60, fc=STONE, ec=MUTE, lw=0.6, hatch=""))
# réservations
for x in (0, W - T):
    ax.add_patch(Rectangle((x - 5, -Emb), T + 10, Emb, fc="white", ec=MUTE, lw=0.5, ls="--"))
# vitrage (derrière le cadre, ouverture 1810 x 1120)
ax.add_patch(Rectangle((T, T), W - 2 * T, Hv - 2 * T, fc=GLASS, ec="none"))
# montants et traverses (tube 40 vu de face)
for x in (0, W - T):
    ax.add_patch(Rectangle((x, -Emb), T, Emb + Hv, fc="white", ec=INK, lw=1.2))
ax.add_patch(Rectangle((T, 0), W - 2 * T, T, fc="white", ec=INK, lw=1.2))                # traverse basse (au niveau du dessus du socle)
ax.add_patch(Rectangle((T, Hv - T), W - 2 * T, T, fc="white", ec=INK, lw=1.2))           # traverse haute (rapportée)
ax.text(W / 2, Hv - T - 60, "traverse haute rapportée (boulonnée), posée après insertion du vitrage", ha="center", va="center", fontsize=10, color=MUTE)
ax.text(W / 2, T + 60, "traverse basse soudée, dessus affleurant le socle", ha="center", va="center", fontsize=10, color=MUTE)
ax.text(W / 2, Hv / 2, "sandwich verre / lenticulaire / verre\nouverture libre 1 810 × 1 120\n(vitrage hors fourniture)", ha="center", va="center", fontsize=11, color=ACC)
ax.text(T / 2, -Emb / 2, "scellé", ha="center", va="center", fontsize=10, rotation=90, color=MUTE)
dim(ax, 0, Hv, W, Hv, "1 890 hors tout", off=200)
dim(ax, T, Hv, W - T, Hv, "1 810 entre montants", off=90, fs=10)
dim(ax, W, -Emb, W, Hv, "1 728 montant", off=140, side="v")
dim(ax, W, 0, W, Hv, "1 200 visible", off=60, side="v")
dim(ax, W, -Emb, W, 0, "528 encastré", off=60, side="v")
dim(ax, 0, -Emb - 60, T, -Emb - 60, "40", off=-40, fs=10)
ax.set_xlim(-450, W + 520); ax.set_ylim(-Emb - 180, Hv + 330)
ax.set_title("Élévation (face mer) — cotes en mm", fontsize=13, color=MUTE, loc="left")

# ---------- Vue latérale ----------
ax2 = fig.add_axes([0.48, 0.10, 0.13, 0.84]); ax2.set_aspect("equal"); ax2.axis("off")
D = 80
ax2.add_patch(Rectangle((-250, -Emb - 60), 500 + D, Emb + 60, fc=STONE, ec=MUTE, lw=0.6))
ax2.add_patch(Rectangle((-5, -Emb), D + 10, Emb, fc="white", ec=MUTE, lw=0.5, ls="--"))
ax2.add_patch(Rectangle((0, -Emb), D, Emb + Hv, fc="white", ec=INK, lw=1.2))
# vitrage plaqué côté mer, parclose
ax2.add_patch(Rectangle((-30, T), 30, Hv - 2 * T, fc=GLASS, ec=INK, lw=0.6))
ax2.text(-15, Hv / 2, "sandwich ≈ 30", ha="center", va="center", fontsize=9.5, rotation=90)
dim(ax2, 0, Hv, D, Hv, "80", off=60, fs=10)
ax2.text(D + 30, Hv / 2, "tube 80 × 40 × 3\ninox 316L", ha="left", va="center", fontsize=11)
ax2.set_xlim(-300, D + 320); ax2.set_ylim(-Emb - 180, Hv + 200)
ax2.set_title("Vue latérale", fontsize=13, color=MUTE, loc="left")

# ---------- Section du montant + principe de réception du vitrage (échelle agrandie) ----------
ax3 = fig.add_axes([0.62, 0.42, 0.36, 0.52]); ax3.set_aspect("equal"); ax3.axis("off")
t = 3
ax3.add_patch(Rectangle((0, 0), 80, 40, fc="white", ec=INK, lw=1.4))
ax3.add_patch(Rectangle((t, t), 80 - 2 * t, 40 - 2 * t, fc="white", ec=INK, lw=0.8))
# sandwich à l'extérieur (côté mer = gauche), sur bande souple, retenu par un plat 40x6 vissé (proposition)
ax3.add_patch(Rectangle((-2, 0), 2, 40, fc="#e8e8e8", ec=MUTE, lw=0.4))       # bande souple 2 mm
ax3.add_patch(Rectangle((-32, 20), 30, 20, fc=GLASS, ec=INK, lw=0.8))          # vitrage (on ne dessine que la partie dans le cadre)
ax3.add_patch(Rectangle((-38, -6), 6, 46, fc="white", ec=INK, lw=1.0))         # parclose plat 40x6 (proposition)
ax3.annotate("", (-38, 10), (-52, 10), arrowprops=dict(arrowstyle="-", lw=0.5, color=MUTE))
ax3.text(-54, 10, "parclose plat inox\n40 × 6 vissé (proposition,\nà l'appréciation de l'atelier)", ha="right", va="center", fontsize=10)
ax3.text(-17, 30, "sandwich\n≈ 30", ha="center", va="center", fontsize=9.5)
ax3.text(40, 20, "80 × 40 × 3", ha="center", va="center", fontsize=11)
ax3.text(-1, 45, "bande souple 2 mm\n(pas de contact verre / métal)", ha="center", va="bottom", fontsize=9.5, color=MUTE)
dim(ax3, 0, 0, 80, 0, "80", off=-12, fs=10)
dim(ax3, 80, 0, 80, 40, "40", off=8, side="v", fs=10)
ax3.text(-60, -14, "◄ côté mer", fontsize=10, color=MUTE)
ax3.set_xlim(-140, 110); ax3.set_ylim(-30, 70)
ax3.set_title("Section du montant ≈ 1:1 — réception du vitrage", fontsize=12, color=MUTE, loc="left")

# ---------- Nomenclature ----------
ax4 = fig.add_axes([0.62, 0.06, 0.36, 0.32]); ax4.axis("off")
rows = [("Rep.", "Désignation", "Qté"),
        ("1", "Montant tube 80×40×3 316L, L = 1 728", "2"),
        ("2", "Traverse basse tube 80×40×3, L = 1 810, soudée", "1"),
        ("3", "Traverse haute tube 80×40×3, L = 1 810, boulonnée", "1"),
        ("4", "Parclose plat 40×6 316L, cadre 4 pièces (proposition)", "1"),
        ("5", "Bande souple 2 mm, pourtour (proposition)", "—"),
        ("—", "Vitrage : hors fourniture (lot vitrage)", "—")]
y = 1.0
for i, r in enumerate(rows):
    fw = "bold" if i == 0 else "normal"
    ax4.text(0.00, y, r[0], fontsize=10, va="top", fontweight=fw); ax4.text(0.10, y, r[1], fontsize=10, va="top", fontweight=fw); ax4.text(0.95, y, r[2], fontsize=10, va="top", ha="right", fontweight=fw)
    y -= 0.13
ax4.text(0, y - 0.02, "Masse châssis ≈ 5,2 kg/m × 7,1 m ≈ 37 kg.\nFinition brossée, bouts de tube fermés.\nDessin établi avec l'aide de l'IA —\nsous réserve du plan de réalisation de l'atelier.", fontsize=9.5, va="top", color=MUTE)

fig.savefig("/home/claude/out/ch02.png", dpi=110, facecolor="white")
stamp_pdf("/home/claude/out/ch02.png", "/home/claude/out/LV-VL-CH-02_chassis_v02_tube80x40x3.pdf",
          dict(titre="Vitrine lenticulaire — Châssis v02 tube 80×40×3 316L",
               num="LV-VL-CH-02", rev="2", statut="CONSULTATION", date="29-09-2026",
               objet="Châssis de l'écran : profil arrêté 80×40×3, géométrie selon STEP ecran v00 (J. Miceli)",
               url="https://vitrine-lenticulaire.vercel.app"))
print("ok")
