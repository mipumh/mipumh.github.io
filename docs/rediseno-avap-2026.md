# Rediseño de mip.umh.es para la visita de la AVAP (octubre de 2026)

Recorrido de los cambios hechos entre el 26 y el 28 de octubre de 2026 en la rama `rediseno-avap` (35 commits sobre `master`). Contexto: el comité de la AVAP revisa la web para la renovación de la acreditación (visita el 6/11/2026; consulta la web desde el 30/10).

## 1. Base: datos oficiales y nueva estructura (26/10)

- **Fuente de verdad oficial.** La ficha del título en umh.es se pinta con JavaScript; sus datos salen de un JSON público (`get_dataJson.py`). `_tools/sync_umh.py` descarga la ficha, las 11 guías docentes 2026/27 y las fichas del PDI. Plazas, créditos, modalidad, horario, responsables y ponderaciones ya no se escriben a mano.
- Errores corregidos frente a la web antigua y el encargo: horario 18:00–19:00 (no 19:30), Prácticas en el 2.º semestre (no anual), Carvajal y González Esteban catedráticos, enlaces rotos de reconocimiento de créditos, preinscripción de másteres y SGIC.
- **Bootstrap 5.3 por CDN** en lugar del 4.4 copiado, sin jQuery ni el sidebar Lanyon. Layouts únicos (`default`, `page`, `home`, `docente`, `asignatura`).
- **Páginas nuevas:** Calidad y transparencia, Nos visitan, Prácticas, 11 asignaturas, fichas de profesorado con plantilla de CV AVAP. Plan de estudios y Admisión rehechos con textos oficiales.
- Revista (`../blog`): menú común, ISSN 3020-383X en el pie, `/conferencias/` como archivo y entrada de la audiencia abierta con la AVAP.

## 2. Diseño (27/10)

- Hero negro con ilustración animada (SVG/CSS, respeta *reduced motion*), cinta de materias, tipografía Inter Tight, logo UMH como en ComunIA.
- Se probó una variante tipo primary.studio; se descartó (rama eliminada) y se eligió la del hero negro.
- Textos recortados ~30%; ruta de navegación en todas las subpáginas; intertítulos en negrita.

## 3. Contenidos (28/10)

- **Nos visitan:** carteles de las clases del curso en portada (rejilla de 4, «Próxima clase» automática); página agrupada por asignatura con fichas de ponentes; 31 de 105 con foto (revista del máster, dirección, perfiles públicos).
- **Profesorado:** etiquetas de asignaturas (responsable/participa), profesorado externo, Valero subdirector, últimos 4 artículos científicos del Portal de Investigación UMH en cada ficha.
- **Admisión:** criterios 60/20/20 (dentro de los rangos de la memoria verificada); preguntas frecuentes desplegables.
- **Portada:** cuadro «El título en datos» con ediciones, egresados, precio por crédito y fechas del RUCT; claustro compacto; entidades colaboradoras (16) sobre menta con enlace al catálogo del Observatorio; instituciones colaboradoras con logos (Informadores de Elche, APPA, ADEPA, AMI, ANP, ComunIA); Premio Vicente Verdú con los seis trabajos premiados.
- **Contacto:** botón «¿Hablamos?» en cabecera y menú móvil, formulario en ventana (EmailJS); menú móvil con información práctica y redes.
- **Egresados:** fichas por promoción desde los listados de TFM (solo nombre y título). **Oculta** hasta revisar permisos.

## 4. Rendimiento y SEO (28/10)

- Imágenes: de 7,4 MB a <1 MB; retratos 240 px, carteles 600–640 px; `width/height`, carga diferida. Originales fuera de la web publicada (de 20 MB a 2,5 MB).
- Font Awesome sustituido por SVG en línea; EmailJS solo al usar un formulario; menos pesos tipográficos.
- Meta descripción por página, imagen social propia (1200×630), JSON-LD (programa, universidad, web, migas de pan, Person, Course), H1 y H2 correctos, sitemap con 31 URL.

- URL jerárquicas sin `.html`: `/plan-de-estudios/<asignatura>/`, `/profesorado/<docente>/`, `/admision/`… (sin redirecciones desde las antiguas); títulos con «máster online» y «título oficial»; enlaces de la revista actualizados.
- Analytics GA4 (`G-BEL40TFYNP`) con Consent Mode v2 y aviso de cookies en web y revista.

## 5. Preguntas frecuentes (28/10)

- Página `/preguntas-frecuentes/` con 36 preguntas en siete temas (el máster, clases, admisión, estudiantes de fuera de España, precio y becas, prácticas y TFM, contacto). Salen de unos 260 correos de respuesta a candidatos (2022-2026), redactadas de nuevo y contrastadas con la ficha oficial y estudios.umh.es (tasas, exenciones, formas de pago, acceso con títulos extranjeros).
- Admisión muestra solo el bloque de admisión; menú móvil, pie, formulario y vías de contacto enlazan a la página nueva.
- Sin marcado FAQPage: Google retiró ese resultado enriquecido en mayo de 2026.

## 6. Pendiente

- Permisos de egresados antes de volver a publicar la página.
- CV de los docentes (bloque `cv:` en `_profesorado/*.md`), LinkedIn del máster, «IBerperia», fotos de 74 ponentes.
- Web fusionada en `master` y publicada el 28/10/2026; falta la revista (`../blog`, rama `rediseno-avap`).
