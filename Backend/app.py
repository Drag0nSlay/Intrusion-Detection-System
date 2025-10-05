import sys
import os
import sqlite3

# Add project root to sys.path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from Backend.database import insert_alert
from utils.auth import require_api_key
from utils.validator import validate_alert_data
from utils.logger import log_info, log_error

app = Flask(__name__)

DB_PATH = os.getenv("DB_NAME", "alerts.db")

def get_db_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/alerts", methods=["GET"])
def get_alerts():
    try:
        conn = sqlite3.connect("alerts.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM "Alerts" ORDER BY id DESC LIMIT 20')
        rows = [dict(row) for row in cur.fetchall()]
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print("DB Error:", e)
        return jsonify({"error": str(e)}), 500

@app.route("/ingest", methods=["POST"])
@require_api_key
def ingest_alert():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        if not validate_alert_data(data):
            return jsonify({"error": "Invalid alert payload (missing fields)"}), 400

        alert = data["alert"]
        # Use insert_alert from database.py (it uses parameterized queries)
        insert_alert(
            timestamp=data.get("timestamp"),
            src_ip=data.get("src_ip"),
            dest_ip=data.get("dest_ip"),
            proto=data.get("proto"),
            signature=alert.get("signature"),
            severity=alert.get("severity")
        )
        log_info(f"Alert ingested: {data.get('src_ip')} -> {data.get('dest_ip')}, sig={alert.get('signature')}")
        return jsonify({"status": "ok"})
    except Exception as e:
        log_error(f"Ingest error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    # run via: python -m Backend.app  (from project root)
    app.run(host="0.0.0.0", port=5000)