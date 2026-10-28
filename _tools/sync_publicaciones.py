#!/usr/bin/env python3
"""Últimos artículos científicos del claustro desde el Portal de Investigación de la UMH.

Lee `portal_id` del front matter de _profesorado/*.md y escribe
_data/publicaciones.json. El portal bloquea las peticiones simples, así que
las páginas se descargan con Chrome sin interfaz. Ejecutar desde la raíz:

    python3 _tools/sync_publicaciones.py
"""
import glob
import html
import json
import os
import re
import subprocess

ROOT = os.path.join(os.path.dirname(__file__), "..")
PORTAL = "https://portalinvestigacion.umh.es"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SALIDA = os.path.join(ROOT, "_data", "publicaciones.json")
MAX_ARTICULOS = 4

# Publicaciones que no son artículos en revistas científicas
EXCLUIR = ("Revista de Innovación en Periodismo", "Festa d'Elx", "UMH Sapiens", "Monografías")


def descargar(url):
    out = subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=12000", "--dump-dom", url],
        capture_output=True, text=True, timeout=120)
    return out.stdout


def limpiar(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def articulos(portal_id):
    s = descargar("%s/investigadores/%s/publicaciones?size=150" % (PORTAL, portal_id))
    lista = []
    for anyo, bloque in re.findall(
            r'<h3 class="grupo-docs__grupo-titulo">(\d{4})</h3>(.*?)</ol>', s, re.S):
        for href, titulo, loc in re.findall(
                r'<a href="(/documentos/[^"]+)">\s*<span class="c-doc__titulo"[^>]*>(.*?)</span>.*?'
                r'<p class="c-doc__localizacion">(.*?)</p>', bloque, re.S):
            loc = limpiar(loc)
            # Artículo de revista: la localización cita volumen o número
            titulo = limpiar(titulo)
            if any(x in loc for x in EXCLUIR) or titulo.startswith("Capítulo") or not re.search(r"\b(Vol\.|Núm\.)", loc):
                continue
            revista = re.split(r",\s*(Vol\.|Núm\.)", loc)[0]
            lista.append({"titulo": titulo, "revista": revista,
                          "anyo": int(anyo), "url": PORTAL + href})
    lista.sort(key=lambda a: a["anyo"], reverse=True)
    return lista[:MAX_ARTICULOS]


def main():
    datos = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "_profesorado", "*.md"))):
        fm = open(path, encoding="utf-8").read().split("---")[1]
        m = re.search(r"^portal_id:\s*(\d+)", fm, re.M)
        if not m:
            continue
        slug = os.path.basename(path)[:-3]
        datos[slug] = {
            "perfil": "%s/investigadores/%s/detalle" % (PORTAL, m.group(1)),
            "publicaciones": "%s/investigadores/%s/publicaciones" % (PORTAL, m.group(1)),
            "articulos": articulos(m.group(1)),
        }
        print(slug, len(datos[slug]["articulos"]))
    with open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
