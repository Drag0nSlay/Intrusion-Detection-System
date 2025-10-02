from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route("/alerts", methods=["GET"])
def get_alerts():
    rows = database.fetch_alerts(limit=20)
    return jsonify(rows)

@app.route("/ingest", methods=["POST"])
def ingest_alert():
    data = request.get_json()
    if "alert" in data:
        database.insert_alert(data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
