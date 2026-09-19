#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Segnaposto nero/arancione, da sostituire con le foto reali (stessi nomi file)."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(ROOT, "images")
os.makedirs(IMG_DIR, exist_ok=True)

INK = (10, 9, 7)
PANEL = (23, 19, 16)
ORANGE = (255, 122, 26)
PAPER = (237, 230, 216)

FILES = {
    "hero-dojo.webp": (1600, 500),
    "chi-siamo-1.webp": (900, 600), "chi-siamo-2.webp": (900, 600),
    "chi-siamo-3.webp": (900, 600), "chi-siamo-4.webp": (900, 600),
    "galleria-1.webp": (800, 600), "galleria-2.webp": (800, 600),
    "galleria-3.webp": (800, 600), "galleria-4.webp": (800, 600),
    "galleria-5.webp": (800, 600), "galleria-6.webp": (800, 600),
    "dove-1.webp": (900, 600), "locandina.webp": (700, 900),
    "hakama-gi.webp": (900, 600), "shinai.webp": (700, 700), "bokken.webp": (700, 700),
    "bogu.webp": (900, 600),
    "bambini-1.webp": (1000, 600), "bambini-2.webp": (900, 600), "bambini-3.webp": (900, 600),
    "conan-hero.webp": (900, 600), "conan-maglietta.webp": (800, 800),
    "conan-2024-risultati.webp": (900, 700), "conan-2023-gruppo.webp": (1000, 700),
}

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
except Exception:
    font = ImageFont.load_default()
    font_small = font

for name, (w, h) in FILES.items():
    img = Image.new("RGB", (w, h), PANEL)
    draw = ImageDraw.Draw(img)
    # diagonale arancione in un angolo, eco del "fendente" del sito
    draw.polygon([(0, h), (w * 0.32, h), (0, h * 0.55)], fill=ORANGE)
    draw.polygon([(0, h), (w * 0.32, h), (0, h * 0.55)], outline=INK, width=2)
    draw.rectangle([8, 8, w - 9, h - 9], outline=(255, 122, 26, 80), width=2)
    text = "PARMA KENDO KAI"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((w - tw) / 2, h / 2 - th - 4), text, fill=PAPER, font=font)
    label = name.replace(".webp", "").replace("-", " ").upper()
    bbox2 = draw.textbbox((0, 0), label, font=font_small)
    tw2, th2 = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
    draw.text(((w - tw2) / 2, h / 2 + 12), label, fill=ORANGE, font=font_small)
    img.save(os.path.join(IMG_DIR, name), quality=85)

print("Segnaposto generati:", len(FILES))
