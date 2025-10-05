# ingest.py
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000/ingest")

# If testing locally, you can create a small eve.json with some alert lines and point to it
EVE_PATH = os.getenv("EVE_PATH", "test_eve.json")

def forward():
    headers = {"Content-Type": "application/json", "X-API-KEY": API_KEY}
    with open(EVE_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            # only forward alerts
            if obj.get("event_type") == "alert" or "alert" in obj:
                try:
                    r = requests.post(BACKEND_URL, json=obj, headers=headers, timeout=5)
                    print("POST", r.status_code, r.text)
                except Exception as e:
                    print("POST failed:", e)

if __name__ == "__main__":
    forward()