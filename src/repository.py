import json
from src.models import Event


def load_scraped_ids(conn, club_id: int) -> set[str]:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT external_id FROM scraped_events WHERE club_id = %s",
        (club_id,),
    )
    ids = {row[0] for row in cursor.fetchall()}
    cursor.close()
    return ids


def load_production_ids(conn, club_id: int) -> set[str]:
    cursor = conn.cursor()
    # Eventos scrapeados que ya están en producción por external_id
    cursor.execute(
        "SELECT external_id FROM event WHERE club_id = %s AND external_id IS NOT NULL",
        (club_id,),
    )
    ids = {row[0] for row in cursor.fetchall()}
    cursor.close()
    return ids


def load_production_title_dates(conn, club_id: int) -> set[tuple]:
    """Fallback para eventos ingresados manualmente (sin external_id)."""
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT e.title, es.event_date
        FROM event e
        JOIN event_schedule es ON es.event_id = e.id
        WHERE e.club_id = %s AND e.external_id IS NULL
        """,
        (club_id,),
    )
    pairs = {(row[0], str(row[1])) for row in cursor.fetchall()}
    cursor.close()
    return pairs


def insert_event(conn, event: Event) -> None:
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO scraped_events (external_id, club_id, title, date, description, image_url, ticket_url, tags, categories)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            event.external_id,
            event.club_id,
            event.title,
            event.date,
            event.description,
            event.image_url,
            event.ticket_url,
            json.dumps(event.tags) if event.tags else None,
            json.dumps(event.categories) if event.categories else None,
        ),
    )
    conn.commit()
    cursor.close()
