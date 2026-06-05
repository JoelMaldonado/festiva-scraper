import requests
from src.models import Event
from src.mappers.folkstorgata import TAG_MAP

CLUB_ID = 32
CLUB_NAME = "FolkStorgata"
EVENTS_URL = "https://data.accentapi.com/feed/81585.json?nocache=1780672356809"


def get_events() -> list[Event]:
    response = requests.get(EVENTS_URL, timeout=15)
    response.raise_for_status()
    data = response.json()

    events = []
    for item in data.get("events", []):
        date = item.get("start_date_raw")
        if not date:
            continue

        events.append(
            Event(
                club_id=CLUB_ID,
                club_name=CLUB_NAME,
                external_id=item.get("event_id"),
                title=item.get("name"),
                date=date,
                description=item.get("description"),
                image_url=item.get("thumbnail_url") or None,
                ticket_url=item.get("ticket_uri") or None,
                tags=[],
                categories=[],
            )
        )

    return events
