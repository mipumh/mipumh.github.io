#!/usr/bin/env python3
"""Genera _data/ponentes.csv para la sección «Nos visitan».

Fuentes:
- _mejora_avap/ponentes_invitados_MIP_2021-2026.csv (listado administrativo + carteles)
- ../blog/_conferencias/*.md (fichas de 2020/21 y otoño de 2021)

Normaliza nombres y asignaturas y marca con publicar=no lo que el director debe
confirmar antes de publicarse. Ejecutar desde la raíz del repo:

    python3 _tools/build_ponentes.py
"""
import csv
import glob
import os
import re
import unicodedata

ROOT = os.path.join(os.path.dirname(__file__), "..")
FUENTE = os.path.join(ROOT, "_mejora_avap", "ponentes_invitados_MIP_2021-2026.csv")
CONFERENCIAS = os.path.join(ROOT, "..", "blog", "_conferencias", "*.md")
SALIDA = os.path.join(ROOT, "_data", "ponentes.csv")
# Ponentes de ediciones anteriores sin fecha, añadidos a mano por la dirección
EXTRA = os.path.join(os.path.dirname(__file__), "ponentes_extra.csv")
# Listado curado de «Nos visitan»: sus cargos completan las sesiones que no lo tienen
NOS_VISITAN = os.path.join(ROOT, "_data", "nos_visitan.yml")

NOMBRES = {
    "José A. Navas": "José A. Navas",
    "José Antonio Navas": "José A. Navas",
    "José Navas": "José A. Navas",
    "Jose A. Navas": "José A. Navas",
    "Pablo Caño": "Pablo Caño Sterck",
    "Pablo Caño Stark": "Pablo Caño Sterck",
    "Lucia González": "Lucía González",
    "Martín Gonzalez": "Martín González",
    "Mirian Hernanz": "Miriam Hernanz",
    "Bea Lara": "Beatriz Lara",
    "Fermin Elizari": "Fermín Elizari",
    "Efrén Ortiz Lemus": "Efrén Lemus",
    "Pablo Fernández Delkader": "Pablo Fernández",
    "Àlex Badia": "Alex Badía",
    "Cristian R. Marín": "Cristian Ramón Marín Sanchiz",
    "Demófilo": "Demófilo Peláez",
    "Rubén Mínguez (Nogor Digital)": "Rubén Mínguez",
    "Eva Belmonte (Civio)": "Eva Belmonte",
    "Ana López Jiménez": "Ana López",
}

# Grafía o identidad sin confirmar: no se publican hasta que lo confirme el director
NOMBRES_PENDIENTES = {"Loraine Morales", "Mar Marique", "Alejandra Llorente"}
NO_PUBLICAR = {"Irene Gómez Peña", "Reporteros Sin Fronteras (sesión con varios ponentes)"}
# Cargo (y en su caso título) copiados de otro cartel: se publica solo el nombre
SIN_CARGO = {("José A. Navas", "2025/26"), ("Alejandra Llorente", None), ("Germán Frassa", None),
             ("Quique Ribera", None), ("Roberto Prada", None)}
SIN_TITULO = {"Germán Frassa"}
ORGANIZACIONES = {"Act2ality"}
# Profesorado del máster: sus sesiones no son de ponentes invitados
CLAUSTRO = {"José María Valero Pastor", "Cristian Ramón Marín Sanchiz"}

ASIGNATURAS = {
    "la audiencia en el proceso periodistico": ("La audiencia en el proceso periodístico", "audiencia"),
    "el periodismo como contenido, producto y servicio": ("El periodismo como contenido, producto y servicio", "contenido-producto-servicio"),
    "nuevos modelos de negocio": ("Nuevos modelos de negocio", "modelos-de-negocio"),
    "el impacto de la tecnologia en el periodismo": ("El impacto de la tecnología en el periodismo", "impacto-tecnologia"),
    "diseno y planificacion de proyectos periodisticos": ("Diseño y planificación de proyectos periodísticos", "diseno-planificacion-proyectos"),
    "desarrollo y lanzamiento de proyectos periodisticos": ("Desarrollo y lanzamiento de proyectos periodísticos", "desarrollo-lanzamiento-proyectos"),
    "nuevas narrativas multimedia y periodismo de datos": ("Nuevas narrativas multimedia y periodismo de datos", "narrativas-periodismo-datos"),
    "el periodismo en las redes sociales": ("El periodismo en las redes sociales", "redes-sociales"),
    "diseno web avanzado e introduccion a la programacion": ("Diseño web avanzado e introducción a la programación", "diseno-web-programacion"),
}

MESES = {m: i + 1 for i, m in enumerate(
    "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split())}

# Las notas internas («pendiente») no se escriben: el repo es público. Ver _mejora_avap/pendientes.md
CAMPOS = ["curso", "fecha", "fecha_iso", "ponente", "slug_ponente", "cargo", "titulo",
          "asignatura", "slug_asignatura", "vinculo", "tipo", "publicar"]


def ascii_lower(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s.lower()).strip()


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", ascii_lower(s)).strip("-")


def asignatura(nombre):
    key = ascii_lower(nombre)
    if key == "diseno y planificacion de proyectos periodistico":
        key += "s"
    return ASIGNATURAS.get(key, ("", ""))


def curso_de(fecha_iso):
    y, m = int(fecha_iso[:4]), int(fecha_iso[5:7])
    return "%d/%02d" % (y, (y + 1) % 100) if m >= 9 else "%d/%02d" % (y - 1, y % 100)


def fila(curso, fecha_iso, ponente, cargo, titulo, asig, vinculo, pendiente=""):
    ponente = NOMBRES.get(ponente.strip(), ponente.strip())
    nombre_asig, slug_asig = asignatura(asig)
    publicar = "si"
    if ponente in NO_PUBLICAR or ponente in NOMBRES_PENDIENTES or curso >= "2026/27":
        publicar = "no"
    if (ponente, curso) in SIN_CARGO or (ponente, None) in SIN_CARGO:
        cargo = ""
    if ponente in SIN_TITULO:
        titulo = ""
    fecha = ""
    if fecha_iso:
        fecha = "%s/%s/%s" % (fecha_iso[8:10], fecha_iso[5:7], fecha_iso[:4])
    return {
        "curso": curso, "fecha": fecha, "fecha_iso": fecha_iso, "ponente": ponente,
        "slug_ponente": slugify(ponente), "cargo": cargo.strip(), "titulo": titulo.strip(),
        "asignatura": nombre_asig, "slug_asignatura": slug_asig, "vinculo": vinculo,
        "tipo": "organizacion" if ponente in ORGANIZACIONES else "persona",
        "publicar": publicar, "pendiente": pendiente,
    }


def desde_csv():
    filas = []
    with open(FUENTE, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            fecha_iso = ""
            if r["fecha"]:
                d, m, y = r["fecha"].split("/")
                fecha_iso = "%s-%s-%s" % (y, m, d)
            filas.append(fila(r["curso"], fecha_iso, r["ponente"], r["cargo_segun_cartel"],
                              r["titulo"], r["asignatura"], r["vinculo"], r["aviso"]))
    return filas


def desde_conferencias():
    filas = []
    for path in sorted(glob.glob(CONFERENCIAS)):
        fm = open(path, encoding="utf-8").read().split("---")[1]
        g = lambda k: (re.search(r"^" + k + r":\s*(.*)$", fm, re.M) or [None, ""])[1].strip().strip('"')
        nombre = NOMBRES.get(g("name"), g("name"))
        if nombre in CLAUSTRO:
            continue
        archivo = os.path.basename(path)[:10]
        fecha_iso, pendiente = "", ""
        m = re.match(r"(\d+) de (\w+) de (\d{4})", g("fecha"))
        if m and MESES.get(m.group(2)):
            iso = "%s-%02d-%02d" % (m.group(3), MESES[m.group(2)], int(m.group(1)))
            if iso[:7] == archivo[:7] and int(m.group(1)) <= 31 and not (MESES[m.group(2)] == 11 and int(m.group(1)) > 30):
                fecha_iso = iso
        if not fecha_iso:
            pendiente = "fecha de la ficha (%s) no coincide con la publicación (%s)" % (g("fecha"), archivo)
        filas.append(fila(curso_de(archivo), fecha_iso, nombre, g("position"), g("titulo"),
                          g("asignatura"), "Externo", pendiente))
    return filas


def desde_extra():
    with open(EXTRA, encoding="utf-8") as f:
        return [fila("", "", r["ponente"], r["cargo"], "", r["asignatura"], "Externo")
                for r in csv.DictReader(f)]


def cargos_curados():
    import yaml
    cargos = {}
    for bloque in yaml.safe_load(open(NOS_VISITAN, encoding="utf-8")):
        for p in bloque["ponentes"]:
            if p.get("cargo"):
                cargos.setdefault(p["slug"], p["cargo"])
    return cargos


def main():
    filas = desde_conferencias() + desde_csv() + desde_extra()
    cargos = cargos_curados()
    for f in filas:
        if not f["cargo"] and f["tipo"] == "persona":
            f["cargo"] = cargos.get(f["slug_ponente"], "")
    vistas = set()
    unicas = []
    for f in filas:
        clave = (f["slug_ponente"], f["fecha_iso"] or f["curso"], f["slug_asignatura"])
        if clave in vistas:
            continue
        vistas.add(clave)
        unicas.append(f)
    unicas.sort(key=lambda f: (f["curso"], f["fecha_iso"] or "0"), reverse=True)
    with open(SALIDA, "w", encoding="utf-8", newline="") as out:
        w = csv.DictWriter(out, fieldnames=CAMPOS, extrasaction="ignore")
        w.writeheader()
        w.writerows(unicas)
    pub = [f for f in unicas if f["publicar"] == "si"]
    print("%d sesiones (%d publicables, %d personas)" % (
        len(unicas), len(pub), len({f["slug_ponente"] for f in pub})))


if __name__ == "__main__":
    main()
