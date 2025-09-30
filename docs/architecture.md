# IoT-IDS Project - System Architecture

## 1️⃣ Overview
This document explains the **architecture** of the Raspberry Pi–based Intrusion Detection System (IDS) for IoT networks.  
The system consists of multiple components working together to detect suspicious activity, store alerts, and visualize them in a dashboard.

---

## 2️⃣ High-Level Architecture

     +----------------+        Ethernet / Wi‑Fi        +----------------+
     | Attacker Host  |  <---- (nmap scans, ping) ---- |   Network /    |
     | (laptop/Kali)  |                                |   Switch/Router|
     +----------------+                                +--------+-------+
                                                                  |
                                                                  v
                                                         +----------------+
                                                         | Raspberry Pi   |
                                                         | (IDS Node)     |
                                                         | - Packet capture|
                                                         | - Suricata IDS |
                                                         | - forwarder.py |
                                                         +--------+-------+
                                                                  |
                                       HTTP POST (JSON alerts)    |
                                                                  v
                                                         +----------------+
                                                         | Backend Server |
                                                         | (Flask app)    |
                                                         | - ingest API   |
                                                         | - SQLite DB    |
                                                         +--------+-------+
                                                                  |
                                                                  v
                                                         +----------------+
                                                         | Frontend UI /  |
                                                         | Dashboard      |
                                                         | (uses /alerts) |
                                                         +----------------+

## 3️⃣ Components & responsibilities
- Attacker Host (nmap)
  - Generates network activity (SYN scans, version scans, pings) to simulate attacks.
  - Runs from a laptop on the same lab network (use only on owned/test hosts).

- Network / Switch / Router
  - Standard home/small-lab network connecting attacker, Pi, and backend machine.
  - Optionally use port-mirroring/SPAN if you want the Pi to receive mirrored traffic.
 
- Raspberry Pi (IDS Node)
  - Runs Suricata for packet capture & signature-based detection.
  - Stores alerts to /var/log/suricata/eve.json.
  - Runs ingest.py (ingest script) that tails eve.json and POSTs alert JSON to backend /ingest.
  - Interfaces: ```eth0``` for wired capture (recommended) or ```wlan0``` with compatible adapter.
 
- Backend Server (Flask + SQLite)
  - Exposes:
    - POST /ingest — receives Suricata alert JSON (forwarder sends here).
    - GET /alerts — serves recent alerts for dashboard.
  - Persists alerts in alerts.db (SQLite).
  - Recommended to run on a development laptop for ease (Option B) or on the Pi itself (Option A).

- Frontend Dashboard
  - Fetches /alerts and visualizes: recent alerts table, counts by severity, timeline graph.
  - Can be a simple static page (index.html + Chart.js) or a small React/Flask UI.
 
## 4️⃣ Data flow (detailed sequence)

- **Attack generation** — Attacker host runs nmap (-sS, -sV, etc.) targeting lab hosts.
- **Packet capture** — Raspberry Pi captures packets on the interface (e.g., eth0).
- **Suricata detection** — Suricata inspects packets and writes alert records (JSON) to /var/log/suricata/eve.json.
- **Forwarding** — ingest.py tails eve.json. For each event_type == "alert", it HTTP POSTs the JSON to http://<backend-ip>:5000/ingest.
- **Storage** — Flask /ingest validates and inserts alert fields into Alerts table in alerts.db.
- **Visualization** — Frontend fetches GET /alerts and renders UI. Demo screenshots recorded from this UI.

## 5️⃣ Network & deployment options

- Option A — All-in-one (Pi host backend + IDS)
  -Pros: Single device, less network config.
  - Cons: Pi resource limits (use Pi 4 recommended).
  - Deploy: Suricata + forwarder + Flask all run on Pi. Forwarder uses http://127.0.0.1:5000/ingest.

- Option B — Pi IDS + Laptop Backend (recommended for dev/demo)
  - Pros: Easier development, more CPU for backend, easier to view dashboard.
  - Cons: Need to use laptop IP in forwarder.
  - Deploy: Suricata + forwarder on Pi. Backend runs on laptop at http://<laptop-ip>:5000.

- Port mirroring (optional)
  - If you have a managed switch that supports SPAN, mirror IoT VLAN to Pi to capture all device traffic without bridging.
