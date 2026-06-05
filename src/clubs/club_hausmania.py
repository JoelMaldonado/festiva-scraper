import requests
from src.models import Event
from src.mappers.hausmania import TAG_MAP

CLUB_ID = 13
CLUB_NAME = "Hausmania"
EVENTS_URL = "https://demo.broadcastapp.no/api/layoutWidgetCors?limit=99&venue=w4MaTLQUry&recommended=false&hostname=www.hausmania.org&city=Oslo"


def get_events() -> list[Event]:
    response = requests.get(EVENTS_URL, timeout=15)
    response.raise_for_status()
    data = response.json()

    events = []
    for item in data.get("results", []):
        start_time = item.get("start_time")
        if not start_time:
            continue

        tags = item.get("tags") or []

        events.append(
            Event(
                club_id=CLUB_ID,
                club_name=CLUB_NAME,
                external_id=item.get("objectId"),
                title=item.get("name"),
                date=start_time[:10],
                description=item.get("details"),
                image_url=(item.get("imagekitRef") or {}).get("url"),
                ticket_url=(item.get("custom_fields") or {}).get("ticketUrl") or None,
                tags=tags,
                categories=list({TAG_MAP[t.lower()] for t in tags if t.lower() in TAG_MAP}),
            )
        )

    return events
