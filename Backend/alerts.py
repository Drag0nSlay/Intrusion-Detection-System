import requests

dummy_alert = {
    "timestamp": "2025-09-29T23:45:00",
    "src_ip": "192.168.0.10",
    "dest_ip": "192.168.0.1",
    "proto": "ICMP",
    "alert": {
        "signature": "Test Alert",
        "severity": 2
    }
}

requests.post("http://127.0.0.1:5000/ingest", json=dummy_alert)