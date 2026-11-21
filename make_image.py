#!/usr/bin/env python3
"""Draw the 21 November 2026 world-news front page as one 1024x1024 PNG.

Original vector-style artwork only (PIL primitives): no photographs, no
logos of real outlets.  Every headline is a story reported on
21 November 2026 (Reuters, AP, AFP, The Hindu morning digest, Jiji/Kyodo).
Run:  python3 make_image.py   ->  writes entry.png beside this file.
"""
from PIL import Image, ImageDraw, ImageFont
import os, textwrap

W = H = 1024
PAPER = (247, 243, 234)
INK = (18, 28, 40)
RED = (178, 34, 44)
NAVY = (16, 42, 74)
TEAL = (0, 105, 110)
PURPLE = (86, 44, 120)
ORANGE = (196, 96, 10)
GREEN = (24, 102, 56)
GREY = (90, 96, 104)
WHITE = (255, 255, 255)

F = "/usr/share/fonts/truetype/noto/"
def font(name, size):
    return ImageFont.truetype(F + name, size)

SERIF_BLACK = "NotoSerifDisplay-Black.ttf"
SANS_BLACK = "NotoSansDisplay-Black.ttf"
SANS_XBOLD = "NotoSansDisplay-ExtraBold.ttf"
SANS_BOLD = "NotoSansDisplay-Bold.ttf"
SANS_SEMI = "NotoSansDisplay-SemiBold.ttf"
SANS_MED = "NotoSansDisplay-Medium.ttf"

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=fnt) <= width:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    return lines

def text_block(x, y, text, fnt, fill, width, leading=1.12, align="left"):
    for line in wrap(text, fnt, width):
        if align == "center":
            d.text((x + (width - d.textlength(line, font=fnt)) / 2, y), line, font=fnt, fill=fill)
        else:
            d.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 10], fill=RED)
d.rectangle([0, 16, W, 20], fill=INK)
title = "THE GLOBAL FRONT PAGE"
msize = 74
while d.textlength(title, font=font(SERIF_BLACK, msize)) > W - 56:
    msize -= 2
mast = font(SERIF_BLACK, msize)
d.text(((W - d.textlength(title, font=mast)) / 2, 30), title, font=mast, fill=INK)
sub = font(SANS_SEMI, 24)
s = "ONE IMAGE  •  THE WORLD'S NEWS OF THE DAY  •  ORIGINAL ARTWORK"
d.text(((W - d.textlength(s, font=sub)) / 2, 112), s, font=sub, fill=GREY)
d.rectangle([28, 146, W - 28, 150], fill=INK)

# ---------------------------------------------------------------- date bar
d.rectangle([28, 158, W - 28, 208], fill=RED)
date_f = font(SANS_BLACK, 38)
s = "SATURDAY  •  21 NOVEMBER 2026"
d.text(((W - d.textlength(s, font=date_f)) / 2, 164), s, font=date_f, fill=WHITE)

# ---------------------------------------------------------------- lead story
LX, LY, LW, LH = 28, 220, 968, 238
d.rectangle([LX, LY, LX + LW, LY + LH], fill=NAVY)
# simple globe, right side
cx, cy, r = LX + LW - 118, LY + 104, 78
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(140, 190, 235), width=5)
for k in (-0.55, 0.0, 0.55):
    d.ellipse([cx - r * (1 - abs(k)) * 0.62 - 6, cy - r, cx + r * (1 - abs(k)) * 0.62 + 6, cy + r],
              outline=(110, 160, 210), width=3)
d.line([cx - r, cy, cx + r, cy], fill=(110, 160, 210), width=3)
# three summit dots under the globe: US blue, China red, Russia white
for i, col in enumerate([(70, 110, 200), (222, 41, 16), (235, 235, 235)]):
    x0 = cx - 66 + i * 48
    d.ellipse([x0, LY + 192, x0 + 30, LY + 222], fill=col, outline=WHITE, width=3)
kick = font(SANS_BOLD, 25)
d.text((LX + 30, LY + 20), "SHENZHEN  •  APEC SUMMIT", font=kick, fill=(255, 205, 60))
lead_h = font(SANS_BLACK, 47)
y = text_block(LX + 30, LY + 54, "TRUMP, XI & PUTIN HOLD FIRST TRILATERAL SUMMIT",
               lead_h, WHITE, LW - 290, leading=1.06)
lead_d = font(SANS_MED, 26)
text_block(LX + 30, y + 10,
           "The “G-3” meets in Shenzhen and pledges nuclear-arms cuts, "
           "as a shifting world order takes shape.",
           lead_d, (205, 222, 242), LW - 290, leading=1.18)

# ---------------------------------------------------------------- panels
def panel(x, y, w, h, accent, kicker, headline, deck, hsize=30, compact=False):
    d.rectangle([x, y, x + w, y + h], fill=WHITE)
    d.rectangle([x, y, x + w, y + 10], fill=accent)
    d.rectangle([x, y, x + w, y + h], outline=(200, 196, 186), width=2)
    ky = y + 13 if compact else y + 20
    hy = y + 36 if compact else y + 46
    d.text((x + 20, ky), kicker, font=font(SANS_BOLD, 19), fill=accent)
    yy = text_block(x + 20, hy, headline, font(SANS_XBOLD, hsize), INK, w - 40, leading=1.05)
    if deck:
        text_block(x + 20, yy + 4, deck, font(SANS_MED, 19), (52, 60, 70), w - 40, leading=1.12)

PX, PY, PW, PH, GAP = 28, 472, 474, 180, 16
panel(PX, PY, PW, PH, RED, "EUROPE  •  WAR",
      "RUSSIAN MISSILE LANDS IN POLAND",
      "Warsaw: “a deliberate provocation.” Russia pounds Ukraine anew; "
      "Ukraine hits the Crimean Bridge again.")
panel(PX + PW + GAP, PY, PW, PH, TEAL, "THE HAGUE  •  WORLD COURT",
      "MYANMAR COMMITTED GENOCIDE — ICJ",
      "First genocide verdict against a state: reparations ordered for "
      "the Rohingya. Myanmar: “unfair.”")
panel(PX, PY + PH + GAP, PW, PH, PURPLE, "DENMARK  •  SECURITY",
      "RUSSIAN ASSASSINATION PLOT FOILED",
      "Intelligence stops a plan to kill a US–Ukrainian rapper; two Danes "
      "charged, a Russian diplomat expelled.")
panel(PX + PW + GAP, PY + PH + GAP, PW, PH, ORANGE, "MARKETS  •  AI",
      "ANTHROPIC IPO RAISES $81BN — LARGEST EVER",
      "$1.5tn valuation, yet the tech sell-off deepens. Riemann claim by a "
      "Claude researcher — unverified.")

# ---------------------------------------------------------------- wide panel
WY = PY + 2 * PH + 2 * GAP
panel(PX, WY, 968, 78, GREEN, "CLIMATE  •  COP31",
      "COP31 TALKS DEADLOCKED — SUMMIT IN OVERTIME, NO DEAL IN SIGHT",
      "", hsize=26, compact=True)

# ---------------------------------------------------------------- ticker
TY = WY + 84
d.rectangle([0, TY, W, TY + 54], fill=INK)
tick = ("ALSO TODAY:  UK & EU agree post-Brexit reset deal  •  Gupta jailed 19½ years in New York "
        "Sikh-plot case  •  Tanker hit again in the Strait of Hormuz, seafarer missing  •  "
        "Cost-of-living protests spread across Europe")
text_block(28, TY + 8, tick, font(SANS_SEMI, 20), (240, 238, 230), W - 56, leading=1.25)

foot = font(SANS_MED, 15)
s = "Every story as reported on 21 November 2026 — Reuters • AP • AFP • Jiji • Kyodo"
d.text(((W - d.textlength(s, font=foot)) / 2, TY + 58), s, font=foot, fill=GREY)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, optimize=True)
print("wrote", out, os.path.getsize(out), "bytes")
