# database.py
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_NAME", "alerts.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def insert_alert(timestamp, src_ip, dest_ip, proto, signature, severity):
    """
    Parameterized insert into Alerts table.
    Keeps behavior identical to previous code but prevents SQL injection.
    """
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Alerts (timestamp, src_ip, dest_ip, proto, signature, severity) VALUES (?, ?, ?, ?, ?, ?)",
        (timestamp, src_ip, dest_ip, proto, signature, severity)
    )
    conn.commit()
    conn.close()