#!/usr/bin/env python3
"""Descarga la ficha oficial del título y las guías docentes desde umh.es.

Escribe _data/umh/titulo.json y _data/umh/asignaturas.json, que son la fuente
de verdad de la web para los datos oficiales. Ejecutar desde la raíz del repo:

    python3 _tools/sync_umh.py
"""
import datetime
import html
import json
import os
import re
import urllib.request

BASE = "https://www.umh.es"
API = BASE + "/get_dataJson.py?item=:{item}&frm=DEFAULT&lang=ES"
TITULO = "tit_m_182"
CODIGOS = range(3018, 3029)
OUT = os.path.join(os.path.dirname(__file__), "..", "_data", "umh")
FOTOS = os.path.join(os.path.dirname(__file__), "..", "images", "profesorado")

# Nombres en minúscula y slugs estables para las URL de /asignaturas/
ASIGNATURAS = {
    3018: ("La audiencia en el proceso periodístico", "audiencia"),
    3019: ("El periodismo como contenido, producto y servicio", "contenido-producto-servicio"),
    3020: ("Nuevos modelos de negocio", "modelos-de-negocio"),
    3021: ("El impacto de la tecnología en el periodismo", "impacto-tecnologia"),
    3022: ("Diseño y planificación de proyectos periodísticos", "diseno-planificacion-proyectos"),
    3023: ("Desarrollo y lanzamiento de proyectos periodísticos", "desarrollo-lanzamiento-proyectos"),
    3024: ("Nuevas narrativas multimedia y periodismo de datos", "narrativas-periodismo-datos"),
    3025: ("El periodismo en las redes sociales", "redes-sociales"),
    3026: ("Diseño web avanzado e introducción a la programación", "diseno-web-programacion"),
    3027: ("Prácticas externas", "practicas-externas"),
    3028: ("Trabajo fin de máster", "trabajo-fin-de-master"),
}

DOCUMENTOS = {
    "memoria.pdf": "Memoria verificada del título",
    "memoria_aneca.pdf": "Informe de verificación (ANECA)",
    "informe_avap.pdf": "Informe de evaluación (AVAP)",
    "informe_mod_1.pdf": "Informe de modificación 1",
    "informe_seguimiento_1.pdf": "Informe de seguimiento (AVAP)",
    "informe_renovacion.pdf": "Informe de renovación de la acreditación (AVAP)",
    "resultados_titulo.pdf": "Resultados del título (último informe)",
    "dipticos_publicitarios.pdf": "Díptico informativo",
}


def fetch(item):
    with urllib.request.urlopen(API.format(item=item), timeout=60) as r:
        raw = r.read().decode("utf-8")
    data = json.loads(raw[raw.index("=") + 1:].rstrip().rstrip(";"))
    if data.get("sujetoNoDisponible") != "N":
        raise SystemExit("umh.es no devuelve datos para " + item)
    return data


def first(data, key):
    v = data.get(key) or [None]
    v = v[0] if isinstance(v, list) else v
    if isinstance(v, str):
        v = re.sub(r"^~[$>fy]", "", v)
    return v


def number(data, key):
    v = first(data, key)
    if not v:
        return None
    n = float(v.replace(",", "."))
    return int(n) if n.is_integer() else n


def clean_html(v):
    """Limpia el HTML de umh.es: quita comentarios, <br> sobrantes y pasa a https."""
    if not v:
        return ""
    v = re.sub(r"^~\$", "", v)
    v = re.sub(r"<!--.*?-->", "", v, flags=re.S)
    v = html.unescape(v)
    v = re.sub(r"\s*<br\s*/?>\s*(?=</?(ul|li)\b)", "", v)
    v = re.sub(r"(</?(ul|li)>)\s*<br\s*/?>", r"\1", v)
    v = re.sub(r"(<br\s*/?>\s*){2,}", "</p><p>", v)
    v = v.replace("http://", "https://")
    v = re.sub(r"(?<![\"'=])(https://[^\s<]+)", r'<a href="\1">\1</a>', v)
    return ("<p>" + v.strip() + "</p>").replace("<p></p>", "")


def items(v):
    return re.findall(r"<li>\s*(.*?)\s*(?:</li>|<br|$)", v or "")


def people(data, key):
    return [
        {"id": p["href"].lstrip(":"), "nombre_umh": p["label"]}
        for p in (data.get(key) or [])
        if p
    ]


def labels(data, key):
    return [p["label"] for p in (data.get(key) or []) if p]


def titulo():
    d = fetch(TITULO)
    plazas = re.search(r"\d+", first(d, "_x_numero_plazas_nuevo_ingreso") or "")
    docs = first(d, "expand_expPintaDocumOficial") or {}
    documentos, resultados = [], []
    for ref in docs.get("_x_documentacion_oficial", []):
        anyo = re.search(r"<!--(\d{4})-->", ref)
        path = re.sub(r"^(<!--\d+-->)?~>", "", ref)
        url = BASE + path
        nombre = os.path.basename(path)
        anual = re.search(r"/(\d{4})/\d+_resultados_titulo\.pdf$", path)
        if anual:
            resultados.append({"curso": anual.group(1), "url": url})
        else:
            documentos.append({
                "nombre": DOCUMENTOS.get(nombre, nombre),
                "anyo": anyo.group(1) if anyo else None,
                "url": url,
            })
    resp = (d.get("_x_responsable_titulacion") or [{}])[0]
    salidas_html = first(d, "_x_salidas_profesionales")
    return {
        "nombre": d["label"],
        "curso_academico": first(d, "_x_curso_academico"),
        "modalidad": first(d, "_x_modalidad_estudio"),
        "plazas": int(plazas.group()) if plazas else None,
        "creditos": {
            "total": number(d, "_x_creditos_ECTS"),
            "obligatorios": number(d, "_x_creditos_ECTS_Obligatorias"),
            "optativos": number(d, "_x_creditos_ECTS_optativas"),
            "practicas": number(d, "_x_creditos_ECTS_practicas"),
            "tfm": number(d, "_x_creditos_ECTS_trabajo_fin_master"),
        },
        "duracion": first(d, "_x_duracion_estudio"),
        "orientacion": first(d, "_x_orientacion_master"),
        "plan": first(d, "_x_plan_anyo"),
        "profesion_regulada": first(d, "_x_profesion_regulada"),
        "centro": labels(d, "_x_centro_docente")[0],
        "campus": labels(d, "_x_campus_realizacion")[0].capitalize(),
        "rama": labels(d, "_x_tiene_rama_conocimiento")[0].capitalize(),
        "ambito": labels(d, "_x_tiene_ambito_conocimiento")[0],
        "responsable": {
            "nombre_umh": resp.get("label"),
            "email": first(resp, "_x_email"),
        },
        "ruct": {
            "codigo": "4313467",
            "url": first(docs, "_x_enlace_RUCT"),
        },
        "ficha_url": BASE + "/contenido/Estudios/:" + TITULO + "/datos_es.html",
        "descripcion_html": clean_html(first(d, "_x_descripcion")),
        "salidas": items(salidas_html),
        "salidas_html": clean_html(salidas_html),
        "planificacion_html": clean_html(first(d, "_x_master_tiene_planificacion")),
        "tfm_html": [clean_html(v) for v in d.get("_x_tiene_trabajo_fin_estudios") or [] if v],
        "acceso_html": clean_html(first(d, "_x_acceso_estudios")),
        "admision_html": clean_html(first(d, "_x_admision_estudios")),
        "perfil_ingreso_html": clean_html(first(d, "_x_tiene_perfil_ingreso")),
        # La URL del calendario se enlaza aparte en la web
        "horario_html": clean_html(re.sub(r"https://calendar\.google\.com\S+", "", first(d, "_x_horario") or "")),
        "competencias_generales": labels(d, "_x_titulacion_tiene_competencias_generales"),
        "competencias_especificas": labels(d, "_x_titulacion_tiene_competencias_especificas"),
        "documentos": documentos,
        "resultados_anuales": sorted(resultados, key=lambda r: r["curso"], reverse=True),
    }


def asignatura(codigo):
    d = fetch("asi_m_%d" % codigo)
    nombre, slug = ASIGNATURAS[codigo]
    profesorado = {}
    for key in ("_x_asignatura_tiene_profesor_teoria", "_x_asignatura_tiene_profesor_practica"):
        for p in people(d, key):
            profesorado[p["id"]] = p
    return {
        "codigo": codigo,
        "slug": slug,
        "nombre": nombre,
        "ects": number(d, "_x_creditos_totales_asignatura"),
        "semestre": first(d, "_x_semestre"),
        "caracter": first(d, "_x_tipo_asignatura"),
        "materia": (labels(d, "_x_asignatura_pertenece_materia") or [None])[0],
        "curso_academico": first(d, "_x_curso_academico"),
        "validada": first(d, "_x_validada"),
        "horas": number(d, "_x_horas_asignatura"),
        "descripcion_html": clean_html(first(d, "_x_descripcion_asignatura")),
        "interes_profesional": re.sub(r"<[^>]+>", " ", clean_html(first(d, "_x_interes_profesional"))).strip(),
        "objetivos": labels(d, "_x_asignatura_tiene_objetivos"),
        "unidades": labels(d, "_x_asignatura_tienen_unidades_didacticas"),
        "evaluacion_html": clean_html(first(d, "_x_evaluacion_asignatura")),
        "responsables": people(d, "_x_asignatura_tiene_responsable"),
        "profesorado": sorted(profesorado.values(), key=lambda p: p["nombre_umh"]),
        "guia_url": BASE + "/contenido/Estudios/:asi_m_%d/datos_es.html" % codigo,
    }


def persona(pid):
    """Datos públicos del PDI en umh.es. Descarga la foto a images/profesorado/."""
    d = fetch(pid)
    foto = first(d, "_x_foto_persona")
    foto_local = None
    if foto:
        destino = os.path.join(FOTOS, pid + ".jpg")
        with urllib.request.urlopen(BASE + foto, timeout=60) as r:
            contenido = r.read()
        if len(contenido) > 4000:  # sin foto, umh.es devuelve su logotipo (~3 KB)
            with open(destino, "wb") as f:
                f.write(contenido)
            foto_local = pid + ".jpg"
    return {
        "id": pid,
        "nombre_umh": d["label"],
        "categoria": first(d, "_x_pdi_tiene_categorias_pdi"),
        "area": (labels(d, "_x_tiene_area_conocimiento") or [None])[0],
        "departamento": (labels(d, "_x_pdi_pertenece_a_uor") or [None])[0],
        "grupos": labels(d, "_x_inv_grupo_investigacion_miembros"),
        "titulaciones": [re.sub(r"^~\$(<!--\d+-->)?", "", v) for v in d.get("_x_titulacion_persona") or [] if v],
        "email": first(d, "_x_email"),
        "web": first(d, "_x_web_url"),
        "foto": foto_local,
        "umh_url": BASE + "/contenido/PDI/:" + pid + "/datos_es.html",
    }


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(FOTOS, exist_ok=True)
    hoy = datetime.date.today().isoformat()
    t = titulo()
    t["descargado"] = hoy
    asigs = [asignatura(c) for c in CODIGOS]
    asigs.sort(key=lambda a: (a["semestre"], a["caracter"] != "Obligatoria", a["codigo"]))
    ids = sorted({p["id"] for a in asigs for p in a["profesorado"] + a["responsables"]})
    pdi = {pid: persona(pid) for pid in ids}
    for name, data in (("titulo", t), ("asignaturas", asigs), ("pdi", pdi)):
        with open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    print("Ficha %s y %d asignaturas (%s)" % (t["curso_academico"], len(asigs), hoy))


if __name__ == "__main__":
    main()
