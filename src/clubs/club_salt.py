import requests
from src.models import Event
from src.mappers.salt import TAG_MAP

CLUB_ID = 21
CLUB_NAME = "SALT"
EVENTS_URL = "https://demo.broadcastapp.no/api/layoutWidgetCors?limit=99&venue=0bDKm3RN9l&recommended=false&hostname=www.salted.no&city=Oslo&widget=listingsmodal"


def get_events() -> list[Event]:
    response = requests.get(EVENTS_URL, timeout=15)
    response.raise_for_status()
    data = response.json()

    events = []
    for item in data.get("results", []):
        start_time = item.get("start_time")
        if not start_time:
            continue

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
                tags=item.get("tags") or [],
                categories=list({TAG_MAP[t.lower()] for t in (item.get("tags") or []) if t.lower() in TAG_MAP}),
            )
        )

    return events
