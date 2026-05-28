from src.database import get_connection


def run():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS scraped_events")

    cursor.execute("""
        CREATE TABLE scraped_events (
            id INT AUTO_INCREMENT PRIMARY KEY,
            external_id VARCHAR(100) NOT NULL,
            club_id INT NOT NULL,
            title VARCHAR(255) NOT NULL,
            date DATE NOT NULL,
            description TEXT,
            image_url VARCHAR(500),
            ticket_url VARCHAR(500),
            tags JSON,
            categories JSON,
            event_id INT DEFAULT NULL,
            status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY unique_external_id (external_id)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Migración completada.")


if __name__ == "__main__":
    run()
