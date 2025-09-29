import sqlite3

DB_NAME = "alerts.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def insert_alert(data):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO Alerts (timestamp, src_ip, dest_ip, proto, signature, severity)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (data["timestamp"], data["src_ip"], data["dest_ip"], data["proto"],
         data["alert"]["signature"], data["alert"]["severity"])
    )
    conn.commit()
    conn.close()

def fetch_alerts(limit=20):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Alerts ORDER BY id DESC LIMIT ?", (limit,))
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows