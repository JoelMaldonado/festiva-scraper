import requests
from src.models import Event
from src.mappers.oconnors_irish_pub import TAG_MAP

CLUB_ID = 24
CLUB_NAME = "o'connor's irish pub"
EVENTS_URL = "https://www.broadcast.events/api/domain/events?venueId=miun0HNMGR&limit=1000&skip=0"


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
                external_id=item.get("id"),
                title=item.get("name"),
                date=start_time[:10],
                description=item.get("details"),
                image_url=(item.get("imagekit") or {}).get("url"),
                ticket_url=(item.get("custom_fields") or {}).get("ticketUrl") or None,
                tags=tags,
                categories=list(categories),
            )
        )

    return events
