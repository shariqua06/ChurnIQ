import sqlite3
import bcrypt

DB_PATH = "database/users.db"

def authenticate_user(email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password, role FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        stored_password, role = user

        if bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        ):
            return role

    return None