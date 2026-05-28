from datetime import date
from src.models import Event
from src.database import get_connection
from src.repository import load_scraped_ids, load_production_ids, load_production_title_dates, insert_event


def _filter_by_date(events: list[Event]) -> tuple[list[Event], int]:
    today = date.today()
    valid = []
    discarded = 0

    for event in events:
        try:
            event_date = date.fromisoformat(event.date)
        except (ValueError, TypeError):
            discarded += 1
            continue

        if event_date < today:
            discarded += 1
            continue

        valid.append(event)

    return valid, discarded


def _print_status(msg: str) -> None:
    print(f"\r{msg}", end="", flush=True)


def process_events(all_events: list[Event]) -> None:
    _print_status("Conectando a BD...")
    conn = get_connection()

    clubs: dict[str, list[Event]] = {}
    for event in all_events:
        clubs.setdefault(event.club_name, []).append(event)

    stats: dict[str, dict] = {}

    for club_name, events in clubs.items():
        _print_status(f"[{club_name}] Filtrando eventos...          ")
        valid, discarded_date = _filter_by_date(events)

        seen = set()
        deduped = []
        for event in valid:
            key = event.external_id
            if key not in seen:
                seen.add(key)
                deduped.append(event)
        discarded_date += len(valid) - len(deduped)

        _print_status(f"[{club_name}] Verificando duplicados en BD...")
        club_id = deduped[0].club_id if deduped else None
        scraped_ids = load_scraped_ids(conn, club_id) if club_id else set()
        production_ids = load_production_ids(conn, club_id) if club_id else set()
        production_title_dates = load_production_title_dates(conn, club_id) if club_id else set()

        new_events = []
        duplicates_count = 0
        in_production_count = 0
        for event in deduped:
            if event.external_id in production_ids or (event.title, event.date) in production_title_dates:
                in_production_count += 1
            elif event.external_id in scraped_ids:
                duplicates_count += 1
            else:
                new_events.append(event)

        stats[club_name] = {
            "found": len(events),
            "discarded_date": discarded_date,
            "in_production": in_production_count,
            "duplicates": duplicates_count,
            "to_insert": new_events,
        }

    print("\r" + " " * 60 + "\r", end="")

    total_inserted = 0
    for club_name, s in stats.items():
        inserted_count = 0
        for event in s["to_insert"]:
            insert_event(conn, event)
            inserted_count += 1

        total_inserted += inserted_count

        print(f"\n[{club_name}]")
        print(f"  Encontrados:           {s['found']}")
        print(f"  Descartados por fecha: {s['discarded_date']}")
        print(f"  Ya en producción:      {s['in_production']}")
        print(f"  Duplicados:            {s['duplicates']}")
        print(f"  Insertados:            {inserted_count}")

    print(f"\n{'=' * 40}")
    print(f"TOTAL insertados: {total_inserted}")

    conn.close()
