# IoT-IDS Project - User Manual

## 1️⃣ Purpose
This manual provides instructions to **setup, run, and test** the Raspberry Pi–based IDS backend system for IoT networks.

---

## 2️⃣ Prerequisites

- **Python 3.12+** installed  
- **Flask 2.3.3**, **requests** library (`pip install -r requirements.txt`)  
- **SQLite3** installed  
- Raspberry Pi with Suricata IDS configured (for real-time alerts)  

---

## 3️⃣ Backend Setup

### Step 1: Clone the repository
```bash
git clone https://github.com/Drag0nSlay/Intrusion-Detection-System.git
cd Intrusion-Detection-System/Backend
```
### Step 2: (Optional) Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```
### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Run Flask backend
```bash
python app.py
```
- Backend runs at http://0.0.0.0:5000
- Accessible from Raspberry Pi or local network
---

## 4️⃣ Testing the Backend
<h3>4.1 Insert dummy alert</h3>

```bash
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
```

<h3>4.2 Fetch recent alerts</h3>

```bash
curl http://127.0.0.1:5000/alerts
```
- Returns JSON of last 20 alerts

## 5️⃣ Integration with Raspberry Pi / Suricata

- Configure Suricata on Raspberry Pi → output alerts to ```eve.json```
- Use ```forwarder.py``` to read ```eve.json``` and POST to backend
- Backend automatically stores the alerts in SQLite database
---

## 6️⃣ Notes for Users

- Make sure ```alerts.db``` is writable by Flask backend
- Use ```.gitignore``` to prevent local DB being pushed to GitHub
- Backend endpoints can be used by dashboard/frontend for visualization
---

## 7️⃣ Future Enhancements

- Add authentication for ```/ingest``` endpoint
- WebSocket integration for **real-time dashboard updates**
- Support for multiple Raspberry Pi nodes simultaneously
- Replace SQLite with production-grade database for high traffic
