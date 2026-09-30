import sqlite3
from datetime import datetime


DATABASE_NAME = "jarvis.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            jarvis_response TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_conversation(user_message, jarvis_response):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO conversations
        (user_message, jarvis_response, timestamp)
        VALUES (?, ?, ?)
    """, (user_message, jarvis_response, timestamp))

    connection.commit()
    connection.close()