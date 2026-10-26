# mip.umh.es

Web del [Máster Universitario en Innovación en Periodismo](https://mip.umh.es) de la Universidad Miguel Hernández. Jekyll en GitHub Pages, con Bootstrap 5.3 por CDN y una hoja propia en `css/main.scss`.

## Datos

| Fuente | Fichero | Cómo se actualiza |
|---|---|---|
| Ficha oficial del título, guías docentes y fichas del PDI (umh.es) | `_data/umh/*.json`, `images/profesorado/` | `python3 _tools/sync_umh.py` |
| Ponentes invitados (Nos visitan) | `_data/ponentes.csv` | `python3 _tools/build_ponentes.py` (lee `_mejora_avap/` y `../blog/_conferencias`) |
| Profesorado (fichas y CV) | `_profesorado/*.md` | a mano: bloque `cv:` |
| Menú común con la revista | `_data/navigation.yml` | a mano; copiar también a `blog/_data/` |
| Avisos de cabecera | `_data/avisos.yml` | a mano; se ocultan solos tras `fecha_fin` |

Los datos oficiales (plazas, créditos, modalidad, horario, responsables) no se escriben a mano en las páginas: salen de `_data/umh`.

## Compilar en local

```sh
bundle install
LC_ALL=en_US.UTF-8 bundle exec jekyll serve
```

El `Gemfile` fija la gema `github-pages`, así que la compilación local usa las mismas versiones que GitHub Pages.

Contacto: [mip@umh.es](mailto:mip@umh.es)
