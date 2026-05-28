---
name: add-club
description: Integra un nuevo club al scraper. Recibe clubId, clubName y eventsUrl, inspecciona el JSON del endpoint, crea el archivo de club, genera el mapper de categorías y actualiza main.py.
---

El usuario quiere agregar un nuevo club al scraper. Los parámetros son: $ARGUMENTS

Formato esperado: `clubId clubName eventsUrl`
Ejemplo: `2 Jaeger https://api.jaeger.no/events`

Sigue estos pasos en orden:

## 1. Parsear parámetros

Separa los argumentos:
- `clubId`: primer token (número entero)
- `clubName`: segundo token (string)
- `eventsUrl`: todo lo que sigue (la URL completa)
- `clubName_lower`: clubName en minúsculas y espacios reemplazados por `_`

## 2. Inspeccionar el endpoint

Usa WebFetch para hacer GET a `eventsUrl` y analiza el JSON.

Identifica el path exacto de cada campo:
- **external_id** — ID único e inmutable del evento (ej: `item["id"]`, `item["objectId"]`). Si no existe, detente y avisa al usuario que el endpoint no expone un ID único por evento y no se puede integrar.
- **nombre del evento** (string)
- **fecha** — anota el formato original (ISO, timestamp, etc.)
- **descripción** (string o null)
- **imagen** (url, puede estar anidada o null)
- **ticket_url** (url o null)
- **tags** — lista de strings. Si el campo se llama distinto (ej: `genres`, `categories`) anótalo. Si no hay tags, usa lista vacía.

## 3. Extraer todos los tags únicos

Del JSON completo (todos los eventos), recopila todos los valores únicos del campo de tags en minúsculas. Muéstralos en consola.

## 4. Crear `src/mappers/{clubName_lower}.py`

Clasifica cada tag en una de estas categorías del sistema Festiva. Si un tag no encaja en ninguna, simplemente no lo incluyas.

```
1  Party
2  Latin
3  Afrobeat
4  Techno / House
5  Student
6  Themed
7  LGBTQ+ / Drag
8  Indie / Rock
9  Hip-Hop / R&B
10 Live Music
11 Jazz & Blues
12 Disco / Funk
13 Folk / Americana
14 Games & Quiz
15 Pop
16 Comedy & Shows
17 Karaoke
18 Halloween
19 Christmas
20 New Year's Eve
21 Electronic / Experimental
22 Culture & Experiences
23 Metal
24 Reggae & Ska
25 Hits / Commercial
```

Crea el archivo con este formato (usa `src/mappers/salt.py` como referencia de estilo):

```python
TAG_MAP: dict[str, int] = {
    # Party (1)
    "tag1": 1,
    "tag2": 1,

    # Techno / House (4)
    "tag3": 4,
    ...
}
```

Reglas:
- Todas las keys en minúsculas
- Agrupa por categoría con comentario
- Si un tag encaja en varias categorías, elige la más específica
- Omite tags que no encajan en ninguna categoría

## 5. Crear `src/clubs/club_{clubName_lower}.py`

Usa `src/clubs/club_salt.py` como referencia exacta de estilo.

```python
import requests
from src.models import Event
from src.mappers.{clubName_lower} import TAG_MAP

CLUB_ID = {clubId}
CLUB_NAME = "{clubName}"
EVENTS_URL = "{eventsUrl}"


def get_events() -> list[Event]:
    response = requests.get(EVENTS_URL, timeout=15)
    response.raise_for_status()
    data = response.json()

    events = []
    for item in data.get("...", []):   # ajusta la clave raíz al JSON real
        start_time = item.get("...")   # campo de fecha original
        if not start_time:
            continue

        tags = item.get("tags") or []

        events.append(
            Event(
                club_id=CLUB_ID,
                club_name=CLUB_NAME,
                external_id=item.get("..."),   # campo id único
                title=item.get("..."),
                date=start_time[:10],          # normaliza a yyyy-MM-dd
                description=item.get("..."),
                image_url=...,
                ticket_url=...,
                tags=tags,
                categories=list({TAG_MAP[t.lower()] for t in tags if t.lower() in TAG_MAP}),
            )
        )

    return events
```

Reglas:
- Normaliza la fecha a `yyyy-MM-dd` (usa `datetime` si el formato no es ISO)
- Si un campo opcional no existe, usa `None`
- No agregues manejo de errores más allá del estilo de `club_salt.py`
- No agregues comentarios salvo que el parseo de fecha sea no obvio

## 6. Actualizar `main.py`

Lee `main.py` y:
1. Agrega el import del nuevo club junto a los existentes
2. Agrega `all_events += club_{clubName_lower}.get_events()` junto a los otros `+=`

Si el club estaba comentado (porque existía antes), descoméntalo en vez de duplicar.

## 7. Confirmar

Reporta:
- Campos mapeados (nombre → campo JSON)
- Total de tags únicos encontrados y cuántos quedaron sin categoría
- Archivos creados/modificados
