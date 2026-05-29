import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from dotenv import load_dotenv
from src.database import get_connection

load_dotenv()


def promote():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM scraped_events WHERE status = 'pending' ORDER BY date ASC"
    )
    events = cursor.fetchall()
    cursor.close()

    if not events:
        print("No hay eventos pendientes.")
        conn.close()
        return

    promoted = 0
    skipped = 0

    for row in events:
        categories = json.loads(row["categories"]) if row["categories"] else []

        try:
            cur = conn.cursor()

            cur.execute(
                """
                INSERT INTO event (club_id, external_id, title, description, image_url, ticket_url)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    row["club_id"],
                    row["external_id"],
                    row["title"],
                    row["description"],
                    row["image_url"],
                    row["ticket_url"],
                ),
            )
            event_id = cur.lastrowid

            for category_id in categories:
                cur.execute(
                    "INSERT INTO event_category (event_id, category_id) VALUES (%s, %s)",
                    (event_id, category_id),
                )

            if row["ticket_url"]:
                cur.execute(
                    "INSERT INTO event_detail (event_id, ticket_url) VALUES (%s, %s)",
                    (event_id, row["ticket_url"]),
                )

            cur.execute(
                "INSERT INTO event_schedule (event_id, event_date) VALUES (%s, %s)",
                (event_id, row["date"]),
            )

            cur.execute(
                "UPDATE scraped_events SET event_id = %s, status = 'approved' WHERE id = %s",
                (event_id, row["id"]),
            )

            conn.commit()
            cur.close()

            print(f"  ✓ [{row['date']}] {row['title']} → event_id={event_id}")
            promoted += 1

        except Exception as e:
            conn.rollback()
            print(f"  ✗ [{row['date']}] {row['title']} → ERROR: {e}")
            skipped += 1

    print(f"\n{'=' * 40}")
    print(f"Promovidos: {promoted}")
    print(f"Errores:    {skipped}")

    conn.close()


if __name__ == "__main__":
    promote()
