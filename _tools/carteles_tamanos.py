#!/usr/bin/env python3
"""Genera las versiones de 320 y 480 px de los carteles (images/carteles/<slug>.jpg, 640 px).

La portada las sirve con srcset: en móvil el cartel se ve a unos 250-280 px y no hace falta
descargar el de 640. Ejecutar desde la raíz del repo tras añadir o cambiar un cartel:

    python3 _tools/carteles_tamanos.py
"""
import glob
import os
import re

from PIL import Image

DIR = os.path.join(os.path.dirname(__file__), "..", "images", "carteles")
ANCHOS = (320, 480)

for ruta in sorted(glob.glob(os.path.join(DIR, "*.jpg"))):
    if re.search(r"-\d+\.jpg$", ruta):
        continue
    im = Image.open(ruta).convert("RGB")
    for ancho in ANCHOS:
        destino = ruta[:-4] + "-%d.jpg" % ancho
        if os.path.exists(destino) and os.path.getmtime(destino) >= os.path.getmtime(ruta):
            continue
        alto = round(im.height * ancho / im.width)
        im.resize((ancho, alto), Image.LANCZOS).save(destino, quality=80, optimize=True, progressive=True)
        print("%s (%dx%d, %d KB)" % (os.path.basename(destino), ancho, alto, os.path.getsize(destino) // 1024))
