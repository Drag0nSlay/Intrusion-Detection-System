import json, requests

# Suricata logs file (eve.json) open karo
with open("/var/log/suricata/eve.json") as f:
    for line in f:
        data = json.loads(line)
        if "alert" in data:                # sirf alerts filter karo
            requests.post("http://10.70.18.25:5000/ingest", json=data)
