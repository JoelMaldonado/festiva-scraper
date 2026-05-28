import requests
from src.models import Event
from src.mappers.rockefeller import TAG_MAP

CLUB_ID = 3
CLUB_NAME = "Rockefeller"
EVENTS_URL = "https://www.rockefeller.no/api/eventsEdge"


def get_events() -> list[Event]:
    response = requests.get(EVENTS_URL, timeout=15)
    response.raise_for_status()
    data = response.json()

    events = []
    for item in data:
        start_time = item.get("start_time")
        if not start_time:
            continue

        tags = item.get("tags") or []

        events.append(
            Event(
                club_id=CLUB_ID,
                club_name=CLUB_NAME,
                external_id=item.get("id"),
                title=item.get("name"),
                date=start_time[:10],
                description=item.get("details"),
                image_url=(item.get("imagekit") or {}).get("url"),
                ticket_url=(item.get("custom_fields") or {}).get("ticketUrl") or None,
                tags=tags,
                categories=list({TAG_MAP[t.lower()] for t in tags if t.lower() in TAG_MAP}),
            )
        )

    return events
