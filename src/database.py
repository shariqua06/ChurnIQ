import sqlite3
import bcrypt
from pathlib import Path

DB_PATH = Path("database/users.db")

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

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
        ("admin@churniq.com", hash_password("Admin@123"), "Admin"),
        ("analyst@churniq.com", hash_password("Analyst@123"), "Analyst"),
        ("viewer@churniq.com", hash_password("Viewer@123"), "Viewer")
    ]

    for user in users:
        try:
            cursor.execute(
                "INSERT INTO users (email,password,role) VALUES (?,?,?)",
                user
            )
        except sqlite3.IntegrityError:
            pass
    cursor.execute("SELECT email, password, role FROM users")
    print(cursor.fetchall())
    
    conn.commit()
    conn.close()