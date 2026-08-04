import sqlite3

def create_database():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        issue TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
