# -*- coding: utf-8 -*-
ART = [
"⠀⠀⠀⢀⣀⣀⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠰⠛⠋⠉⠀⠀⠀⠀⠉⠉⠛⠶⢤⣄⣀⠀⠀⠀⠀",
"⠀⠀⠀⣠⣤⣶⣶⣶⡤⢤⣀⠀⠀⠀⠀⠉⠉⠉⠉⠀",
"⠀⢀⡴⠃⠸⣿⣿⣿⡏⠀⣨⡿⠶⠦⠤⠤⠤⠤⣤⠀",
"⠀⠉⠉⢻⣷⠾⣿⡛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⢼⣿⠀⠈⠛⢶⣄⡀⠀⠀⠀⠀⠀⠀⠢⡰⠀",
"⠀⠀⠀⠘⣿⠀⠀⠀⠀⠈⠙⠲⢤⣀⡀⠀⠀⣀⠜⠀",
"⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀",
]
# ordre des bits braille -> (colonne, ligne) dans la cellule 2x4
BITS = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(0,3),(1,3)]

def dots():
    out = []
    for li, line in enumerate(ART):
        for ci, ch in enumerate(line):
            code = ord(ch) - 0x2800
            if code < 0: continue
            for b,(dc,dr) in enumerate(BITS):
                if code >> b & 1:
                    out.append((ci*2+dc, li*4+dr))
    return out

ROWS = [
    ("focus",    "Systems &amp; Offensive Security"),
    ("stack",    "C · C++ · Rust · Python · Bash"),
    ("tools",    "GDB · Docker · CMake · K3s · Vagrant"),
    ("now",      "binary exploitation · Rust tooling"),
    ("status",   "seeking a cybersecurity internship"),
    ("role",     "red team · open to blue team"),
    ("location", "France · remote / UK"),
]

FONT = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'DejaVu Sans Mono',monospace"
BG, BAR, BORDER = "#16161e", "#1a1b26", "#2a2f45"
BLUE, FG, DIM, GREEN, MAGENTA = "#7aa2f7", "#c0caf5", "#565f89", "#9ece6a", "#bb9af7"

W, H = 720, 350
TX = 300            # colonne de gauche du texte
VX = TX + 100       # colonne des valeurs
FIRST = 104         # première ligne de base
LH = 22

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">')
s.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="{BG}" stroke="{BORDER}"/>')
s.append(f'<path d="M0.5 10.5a10 10 0 0 1 10-10h{W-21}a10 10 0 0 1 10 10V34H0.5z" fill="{BAR}" stroke="{BORDER}"/>')
for i,c in enumerate(["#f7768e","#e0af68","#9ece6a"]):
    s.append(f'<circle cx="{22+i*20}" cy="17.5" r="5.5" fill="{c}"/>')
s.append(f'<text x="{W/2}" y="22" font-size="12" fill="{DIM}" text-anchor="middle">0xEr3b0s@localhost: ~</text>')

# ligne de commande
s.append(f'<text x="28" y="66" font-size="14"><tspan fill="{GREEN}">$</tspan>'
         f'<tspan fill="{FG}"> neofetch</tspan></text>')

# l'oeil d'Horus, chaque point braille devenu un vrai cercle
pts = dots()
maxr = max(r for _,r in pts)
top = FIRST + (len(ROWS)+1)*LH/2 - (maxr+1)*5/2 - 8
s.append(f'<g fill="{BLUE}">')
for c,r in pts:
    s.append(f'<circle cx="{40+c*5.2:.1f}" cy="{top+r*5.2:.1f}" r="2"/>')
s.append('</g>')

# le bloc neofetch
y = FIRST
s.append(f'<text x="{TX}" y="{y}" font-size="14" font-weight="bold">'
         f'<tspan fill="{MAGENTA}">0xEr3b0s</tspan><tspan fill="{FG}">@</tspan>'
         f'<tspan fill="{MAGENTA}">localhost</tspan></text>')
y += LH
s.append(f'<text x="{TX}" y="{y}" font-size="14" fill="{DIM}">──────────────────────────────</text>')
for k,v in ROWS:
    y += LH
    s.append(f'<text x="{TX}" y="{y}" font-size="14" fill="{BLUE}">{k}</text>')
    s.append(f'<text x="{VX}" y="{y}" font-size="14" fill="{FG}">{v}</text>')

# invite finale avec curseur clignotant
s.append(f'<text x="28" y="{H-26}" font-size="14" fill="{GREEN}">$</text>')
s.append(f'<rect x="42" y="{H-38}" width="9" height="15" fill="{FG}">'
         f'<animate attributeName="opacity" values="1;1;0;0" dur="1.1s" repeatCount="indefinite"/></rect>')
s.append('</svg>')

open("terminal.svg","w").write("\n".join(s))
print("dots:", len(pts), "ok")