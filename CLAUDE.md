# mip.umh.es · Memoria del proyecto

Web del **Máster Universitario en Innovación en Periodismo (UMH)**. Jekyll en GitHub Pages (gema `github-pages` 223, Jekyll 3.9), Bootstrap 5.3 por CDN y una hoja propia en `css/main.scss`. La revista vive en otro repo (`../blog`, publicada en `https://mip.umh.es/blog/`) y comparte el menú.

Rama de trabajo del rediseño: `rediseno-avap`. `rediseno-escaparate` es una variante descartada (estilo primary.studio) que se conserva como referencia. `master` es la web publicada antigua.

## Compilar y comprobar

```sh
LC_ALL=en_US.UTF-8 bundle exec jekyll serve --port 4011      # sin LC_ALL falla el Sass por las tildes
LC_ALL=en_US.UTF-8 bundle exec jekyll build
LC_ALL=en_US.UTF-8 htmlproofer ./_site --disable-external --allow-hash-href --empty-alt-ignore --url-ignore "/\/blog\//"
```

- Liquid 4 de GitHub Pages: `where_exp` no admite `or`; un campo vacío de un CSV llega como `nil` (comprobar con `.size > 0`).
- Un valor de front matter con `: ` sin comillas hace que Jekyll publique la página **sin plantilla** (solo avisa). Entrecomillar siempre `description` y `lead`.

## De dónde salen los datos

| Datos | Fichero | Cómo se actualiza |
|---|---|---|
| Ficha oficial, guías docentes, PDI y precio por crédito (umh.es) | `_data/umh/*.json`, `images/profesorado/` | `python3 _tools/sync_umh.py` (JSON público `get_dataJson.py?item=:tit_m_182`). Correcciones de la dirección en `RESPONSABLES` del script (p. ej. 3023 → Marín) |
| Últimos 4 artículos científicos del claustro | `_data/publicaciones.json` | `python3 _tools/sync_publicaciones.py` (Portal de Investigación UMH con Chrome sin interfaz; `portal_id` en `_profesorado/*.md`) |
| Ponentes invitados (Nos visitan, asignaturas) | `_data/ponentes.csv` | `python3 _tools/build_ponentes.py` (lee `_mejora_avap/`, `../blog/_conferencias` y `_tools/ponentes_extra.csv`) |
| Fotos de ponentes | `images/ponentes/<slug>.jpg`, `_data/fotos_ponentes.yml` | A mano, 240×240 px |
| Carteles de clases del curso | `images/carteles/`, `_data/carteles.yml` | PNG original en `carteles_escaparate/` (fuera de git) → JPG 640 px |
| Premio Vicente Verdú | `images/premios/`, `_data/premio_verdu.yml` | Originales en `CARTELES PREMIADOS/` (fuera de git) → JPG 600 px |
| Entidades de prácticas / instituciones colaboradoras | `_data/entidades.yml`, `_data/colaboradores.yml`, `images/colaboradores/` | A mano |
| Egresados por promoción | `_data/egresados.yml` | Listados de TFM de la Facultad: **solo nombre y título**, nunca NIF ni notas |
| Admisión, FAQ, hitos (RUCT), avisos, menú | `_data/admision.yml`, `faq.yml`, `hitos.yml`, `avisos.yml`, `navigation.yml` | A mano. `navigation.yml` se copia también a `../blog/_data/` |
| Profesorado (fichas, CV AVAP) | `_profesorado/*.md` | A mano: bloque `cv:`; asignaturas salen de `_data/umh` |

## Reglas

- **No inventar datos.** Lo oficial (plazas, créditos, modalidad, horario, responsables) sale de `_data/umh`. Lo pendiente de confirmar no se publica.
- **Datos personales:** nada de NIF, calificaciones ni datos de pago. Egresados está **oculto** (`published: false`, fuera del menú y de la portada) hasta revisar permisos.
- **Estilo:** fondo blanco, negro `#0b0b0b` y menta `#3df0c4`. El menta solo como fondo o subrayado, nunca como color de texto. Titulares en Inter Tight, texto en Inter. Porcentajes **sin espacio** («60%»).
- **Imágenes:** retratos 240 px, carteles 640 px, sin EXIF, con `width`/`height`, `loading="lazy"` y `decoding="async"`. Iconos con `{% include icon.html n="…" %}` (SVG en línea, sin Font Awesome).
- **SEO:** meta descripción por página (las colecciones la generan en `_includes/head.html`), JSON-LD en `_includes/jsonld.html`, intertítulos como `<h2 class="intertitulo">`, imagen social `images/og-mip.jpg`.
- Escribir en castellano, tono informativo; commits pequeños con mensaje descriptivo.

## Pendiente

- Analytics desactivado: el ID `UA-32796571-1` (web) y `UA-38906933-1` (revista) no recogen datos desde 2023. Falta un ID `G-` de GA4 (`site.inc.analytics.google` en `_config.yml`).
- Permisos de egresados; LinkedIn del máster; «IBerperia» en instituciones; erratas de numeración en los carteles del premio Verdú.
- Detalle en `docs/rediseno-avap-2026.md` y en `_mejora_avap/pendientes.md` (local, fuera de git).
