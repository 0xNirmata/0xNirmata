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

# ── palettes ──────────────────────────────────────────────────────────────
THEMES = {
    # phosphore vert sur noir adouci
    "phosphor": dict(bg="#0d1210", bar="#131a16", border="#22302a",
                     dim="#3f7355", key="#4fbf7a", fg="#a8e6b8",
                     accent="#5eff8a", eye="#4dff88", glow=True, scanlines=True,
                     dots=["#2f6b46","#3d8a58","#5eff8a"]),
    # variante plus douce, moins néon
    "phosphor_soft": dict(bg="#101613", bar="#161d19", border="#24312b",
                     dim="#4a7a60", key="#5fa87d", fg="#bcd9c6",
                     accent="#8fe6a8", eye="#79d99a", glow=True, scanlines=True,
                     dots=["#345c46","#456f55","#8fe6a8"]),
    # monochrome vrai : tout est vert, seule la brillance varie (CRT authentique)
    "phosphor_mono": dict(bg="#0d1210", bar="#131a16", border="#22302a",
                     dim="#2c6b45", key="#3aa864", fg="#6ee094",
                     accent="#9dffbe", eye="#3fd472", glow=True, scanlines=True,
                     dots=["#2c6b45","#3aa864","#9dffbe"]),
    # l'ancienne, gardée sous la main
    "tokyo":    dict(bg="#16161e", bar="#1a1b26", border="#2a2f45",
                     dim="#565f89", key="#7aa2f7", fg="#c0caf5",
                     accent="#bb9af7", eye="#7aa2f7", glow=False, scanlines=False,
                     dots=["#f7768e","#e0af68","#9ece6a"]),
}

FONT = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'DejaVu Sans Mono',monospace"
W, H = 720, 350
TX, VX, FIRST, LH = 300, 400, 104, 22

def build(name):
    t = THEMES[name]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" font-family="{FONT}">']
    s.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" '
             f'fill="{t["bg"]}" stroke="{t["border"]}"/>')

    if t["scanlines"]:
        s.append('<g fill="#ffffff" opacity="0.022">')
        for y in range(36, H-2, 4):
            s.append(f'<rect x="1" y="{y}" width="{W-2}" height="2"/>')
        s.append('</g>')

    s.append(f'<path d="M0.5 10.5a10 10 0 0 1 10-10h{W-21}a10 10 0 0 1 10 10V34H0.5z" '
             f'fill="{t["bar"]}" stroke="{t["border"]}"/>')
    for i,c in enumerate(t["dots"]):
        s.append(f'<circle cx="{22+i*20}" cy="17.5" r="5.5" fill="{c}"/>')
    s.append(f'<text x="{W/2}" y="22" font-size="12" fill="{t["dim"]}" '
             f'text-anchor="middle">0xEr3b0s@localhost: ~</text>')
    s.append(f'<text x="28" y="66" font-size="14"><tspan fill="{t["accent"]}">$</tspan>'
             f'<tspan fill="{t["fg"]}"> neofetch</tspan></text>')

    # l'oeil d'Horus : chaque point braille devenu un cercle
    pts = dots()
    maxr = max(r for _,r in pts)
    top = FIRST + (len(ROWS)+1)*LH/2 - (maxr+1)*5.2/2 - 8
    if t["glow"]:   # halo de phosphore, sans filtre SVG (compatibilite GitHub)
        s.append(f'<g fill="{t["eye"]}" opacity="0.18">')
        for c,r in pts:
            s.append(f'<circle cx="{40+c*5.2:.1f}" cy="{top+r*5.2:.1f}" r="4"/>')
        s.append('</g>')
    s.append(f'<g fill="{t["eye"]}">')
    for c,r in pts:
        s.append(f'<circle cx="{40+c*5.2:.1f}" cy="{top+r*5.2:.1f}" r="2"/>')
    s.append('</g>')

    y = FIRST
    s.append(f'<text x="{TX}" y="{y}" font-size="14" font-weight="bold">'
             f'<tspan fill="{t["accent"]}">0xEr3b0s</tspan><tspan fill="{t["dim"]}">@</tspan>'
             f'<tspan fill="{t["accent"]}">localhost</tspan></text>')
    y += LH
    s.append(f'<text x="{TX}" y="{y}" font-size="14" fill="{t["dim"]}">'
             f'──────────────────────────────</text>')
    for k,v in ROWS:
        y += LH
        s.append(f'<text x="{TX}" y="{y}" font-size="14" fill="{t["key"]}">{k}</text>')
        s.append(f'<text x="{VX}" y="{y}" font-size="14" fill="{t["fg"]}">{v}</text>')

    s.append(f'<text x="28" y="{H-26}" font-size="14" fill="{t["accent"]}">$</text>')
    s.append(f'<rect x="42" y="{H-38}" width="9" height="15" fill="{t["accent"]}">'
             f'<animate attributeName="opacity" values="1;1;0;0" dur="1.1s" '
             f'repeatCount="indefinite"/></rect>')
    s.append('</svg>')
    open(f"terminal_{name}.svg","w").write("\n".join(s))

for n in THEMES: build(n)
print("faits :", ", ".join(THEMES))
