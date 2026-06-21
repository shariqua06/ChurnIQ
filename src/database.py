import sqlite3
from pathlib import Path

DB_PATH = Path("database/users.db")

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    users = [
        ("admin@churniq.com", "Admin@123", "Admin"),
        ("analyst@churniq.com", "Analyst@123", "Analyst"),
        ("viewer@churniq.com", "Viewer@123", "Viewer")
    ]

    for user in users:
        try:
            cursor.execute(
                "INSERT INTO users (email,password,role) VALUES (?,?,?)",
                user
            )
        except:
            pass

    conn.commit()
    conn.close()