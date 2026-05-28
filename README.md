# festiva-scraper

Scraper de eventos para la plataforma Festiva. Consume las APIs públicas de clubs de Oslo, normaliza los eventos, los clasifica por categoría y los persiste en base de datos para su revisión antes de pasar a producción.

## Flujo

1. `python main.py` — scrapea todos los clubs activos, filtra eventos pasados y duplicados, e inserta los nuevos en `scraped_events` con sus categorías mapeadas.
2. `python promote.py` — toma los eventos pendientes en `scraped_events` y los promueve a las tablas de producción (`event`, `event_schedule`, `event_category`, `event_detail`).

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # completar con credenciales de BD
python -m src.migrate
```

## Estructura

```
src/
  clubs/          # un archivo por club (get_events)
  mappers/        # TAG_MAP por club (tags → category_id)
  models.py       # dataclass Event
  processor.py    # filtrado, dedup y persistencia en scraped_events
  repository.py   # queries a BD
  database.py     # conexión MySQL
  migrate.py      # crea la tabla scraped_events
main.py           # entry point del scraper
promote.py        # promueve scraped_events a producción
inspect_tags.py   # utilidad: lista tags únicos de un endpoint
```

## Agregar un nuevo club

```
/add-club <clubId> <clubName> <eventsUrl>
```

El skill inspecciona el endpoint, valida que tenga ID único por evento, genera el mapper de categorías y crea el archivo de club automáticamente.
