<p align="center">
  <img src="docs/Screenshots/file_00000000752872099b4d7e1ebf5308b1.png" alt="IDS Banner" width="800" height=650/>
</p>

<h1 align="center">🛡️ Software-based Intrusion Detection System (IDS)</h1>

<p align="center">
  <img src="docs/Screenshots/logo.png" alt="IDS Logo" width="120"/>
</p>

<p align="center">
  <b> Fully Software-Based Intrusion Detection System for Network Security  </b>
  <br/>  Developed & maintained independently
</p>

---

<p align="center">
  <!-- Shields.io badges -->
  <img src="https://img.shields.io/badge/python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/flask-2.3.3-black?logo=flask" />
  <img src="https://img.shields.io/badge/sqlite-DB-orange?logo=sqlite" />
  <img src="https://img.shields.io/badge/status-in%20progress-yellow" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <a href="https://github.com/Drag0nSlay/Intrusion-Detection-System/actions/workflows/pylint.yml">
  <img src="https://github.com/Drag0nSlay/Intrusion-Detection-System/actions/workflows/pylint.yml/badge.svg" alt="Pylint">
</a>
  <img src="https://img.shields.io/badge/dependabot-active-brightgreen?style=flat-square&logo=dependabot" />

</p>

---
## 📑 Table of Contents
- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Documentation](#-documentation)
- [Setup](#%EF%B8%8F-setup-backend)
- [API Endpoints](#-api-endpoints)
- [Demo Output](#-demo-output)
- [Tech Stack](#-tech-stack)
- [Roadmap](#-roadmap)
- [License](https://github.com/Drag0nSlay/Intrusion-Detection-System?tab=MIT-1-ov-file)
---

## 🚀 Overview
This project implements a **fully software-based Intrusion Detection System (IDS)** designed to monitor, detect, and log malicious network activities in real time.

The system uses **Suricata IDS** as the detection engine and a **Flask-based backend** to ingest, store, and expose security alerts through REST APIs. A lightweight frontend dashboard enables visualization of detected intrusions..

> ⚡ In short: Suricata analyzes network traffic, while the backend processes and stores alerts, forming a modular, scalable, and hardware-independent IDS pipeline suitable for academic, research, and SOC-style environments.
---

## 🗂 Project Structure
```
IDS/
│
├── backend/
│   ├── app.py                  # Flask/FastAPI alert ingestion + APIs
│   ├── database.py             # SQLite / PostgreSQL handler
│   ├── alerts.db
│   ├── requirements.txt
│   └── __init__.py
│
├── ids-engine/
│   ├── suricata.yaml           # Suricata config (software mode)
│   ├── local.rules             # Custom detection rules
│   ├── eve_forwarder.py        # Reads eve.json & sends to backend
│   └── eve.json                # Generated alerts (runtime)
│
├── frontend/                   # Optional but GOOD for marks
│   ├── index.html
│   ├── static/
│   └── script.js
│
├── attack-simulation/          # Testing environment
│   ├── nmap_scan.sh
│   ├── brute_force.py
│   └── arp_spoof.sh
│
├── docs/
│   ├── Report.docx
│   ├── Report.pdf
│   └── Screenshots/
│       ├── nmap_detected.png
│       ├── brute_force_alert.png
│
└── README.md
```
---

## 📖 Documentation
- 📐 [System Architecture](docs/architecture.md)
- 📑 [User Manual](docs/user_manual.md)

---


## ⚙️ Setup (Backend)

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Drag0nSlay/Intrusion-Detection-System.git
cd Intrusion-Detection-System/Backend
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Run Backend
```bash
python app.py
```
Backend runs at → http://localhost:5000

---

## 🖥 API Endpoints
| Endpoint  | Method | Description            |
| --------- | ------ | ---------------------- |
| `/ingest` | POST   | Ingest Suricata alerts |
| `/alerts` | GET    | Fetch last 20 alerts   |

**Post Example (Expected)**
```bash
{
  "timestamp": "2025-09-29T23:45:00",
  "src_ip": "192.168.0.10",
  "dest_ip": "192.168.0.1",
  "proto": "ICMP",
  "alert": {
    "signature": "ICMP PING detected",
    "severity": 2
  }
}
```
---

## 📊 Demo Output
<p align="center"> <img src="docs/Screenshots/file_0000000015b07209a64417eece06ea10.png" alt="Dashboard Example" width="700"/> </p>

## 🛠 Tech Stack
- Python 3.12
- Flask 2.3.3
- SQLite
- Suricata IDS
- HTML / CSS / JavaScript
- Requests (alert forwarding)

## 📌 Roadmap

<h3> ✅ Current Features — Network IDS </h3>

- Software-based Suricata IDS
- Real-time alert ingestion via REST API
- SQLite-based alert storage
- Attack simulation and validation
- Basic web dashboard

## 🔄 Future Enhancements
- Advanced dashboard analytics
- Multiple IDS instances reporting to a central server
- Secure alert transport (TLS / message queue)
- SIEM / ELK stack integration
- Rule management via web interface

This project is licensed under the [MIT License](https://github.com/Drag0nSlay/Intrusion-Detection-System?tab=MIT-1-ov-file).
<p align="center">💡 💡 Built independently with a strong focus on cybersecurity, detection engineering, real-world IDS workflows and lots of ☕</p> ```
