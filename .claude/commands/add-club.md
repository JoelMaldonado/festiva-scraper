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

Descarga el JSON completo a un archivo local con `curl` (NO uses WebFetch para esto: WebFetch resume/reescribe el contenido con un modelo y puede alterar, dividir o perder strings exactos como los tags).

```
curl -s "{eventsUrl}" -o ./_tmp_events.json
```

Luego inspecciona la estructura con `node` (parsea el JSON real, no un resumen):

```
node -e "const d=require('./_tmp_events.json'); console.log(JSON.stringify(d[0], null, 2))"
```

Identifica el path exacto de cada campo:
- **external_id** — ID único e inmutable del evento (ej: `item["id"]`, `item["objectId"]`). Si no existe, detente y avisa al usuario que el endpoint no expone un ID único por evento y no se puede integrar.
- **nombre del evento** (string)
- **fecha** — anota el formato original (ISO, timestamp, etc.)
- **descripción** (string o null)
- **imagen** (url, puede estar anidada o null)
- **ticket_url** (url o null)
- **tags** — lista de strings. Si el campo se llama distinto (ej: `genres`, `categories`) anótalo. Si no hay tags, usa lista vacía.

## 3. Extraer todos los tags únicos

CRÍTICO: este paso debe ser 100% programático (con `node`), nunca a ojo ni resumido por WebFetch/un modelo. Cualquier transformación manual del texto del tag (dividir palabras, agregar/quitar espacios, normalizar guiones, etc.) está prohibida.

Recorre con un script TODOS los eventos del array (sin tomar una muestra ni solo los primeros) y por cada evento recolecta TODOS los valores del campo de tags/categorías, aplicando únicamente `.toLowerCase()` — ningún otro cambio. El string debe quedar carácter por carácter idéntico al de la fuente, solo en minúsculas (ej: si el JSON tiene `"FolkRock"`, el resultado debe ser `"folkrock"`, NUNCA `"folk rock"`).

Ejemplo de script:

```
node -e "
const d=require('./_tmp_events.json');
const tags = new Set();
for (const item of d) {
  for (const t of (item.tags || [])) tags.add(t.toLowerCase());
}
console.log('total eventos:', d.length);
console.log('tags únicos:', [...tags].sort());
"
```

Verifica que el conteo de eventos procesados coincida con el total real del JSON (revisa si la API pagina con `limit`/`skip`/`total` y ajusta si hace falta para cubrir TODOS los eventos). Muestra la lista completa de tags únicos en consola antes de continuar — no la abrevies ni omitas ninguno.

Borra el archivo temporal (`./_tmp_events.json`) al finalizar.

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
TAG_MAP: dict[str, int | list[int]] = {
    # Party (1)
    "tag1": 1,
    "tag2": 1,

    # Pop (15) + Electronic / Experimental (21)
    "tag3": [15, 21],

    # Techno / House (4)
    "tag4": 4,
    ...
}
```

Reglas:
- Todas las keys en minúsculas
- Cada key debe ser una copia textual exacta del tag obtenido en el paso 3 (mismos caracteres, espacios, guiones, símbolos). No reescribas ni "corrijas" el texto del tag.
- Revisa el tag de TODOS los tags únicos del paso 3 y clasifícalo; ninguno debe quedar sin revisar
- Agrupa por categoría con comentario
- El valor normal es un `int` (una sola categoría). Si el tag describe géneros/temáticas que encajan claramente en más de una categoría (ej: "elektronisk pop" es tanto Pop (15) como Electronic / Experimental (21)), usa una lista `[a, b]`. Esto es la excepción, no la regla — no fuerces múltiples categorías si una sola ya describe bien el tag
- Omite tags que no encajan en ninguna categoría — esto incluye metadatos que no describen un género/temática, como tags de idioma (ej: "english"), o tags que repiten el nombre del propio club/venue

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

        categories = set()
        for t in tags:
            mapped = TAG_MAP.get(t.lower())
            if isinstance(mapped, list):
                categories.update(mapped)
            elif mapped is not None:
                categories.add(mapped)

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
                categories=list(categories),
            )
        )

    return events
```

Reglas:
- Normaliza la fecha a `yyyy-MM-dd` (usa `datetime` si el formato no es ISO)
- Si un campo opcional no existe, usa `None`
- No agregues manejo de errores más allá del estilo de `club_salt.py`
- No agregues comentarios salvo que el parseo de fecha sea no obvio
- El bloque que calcula `categories` (manejando tags mapeados a un `int` o a `list[int]`) se usa siempre, incluso si en este club ningún tag usa lista — mantiene el código consistente entre clubs

## 6. Actualizar `scripts/scrape.py`

Lee `scripts/scrape.py` y:
1. Agrega el import del nuevo club junto a los existentes (en el bloque `from src.clubs import ...`)
2. Agrega `all_events += club_{clubName_lower}.get_events()` junto a los otros `+=` dentro de `main()`

Si el club estaba comentado (porque existía antes), descoméntalo en vez de duplicar.

## 7. Confirmar

Reporta:
- Campos mapeados (nombre → campo JSON)
- Total de tags únicos encontrados y cuántos quedaron sin categoría
- Archivos creados/modificados
