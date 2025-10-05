# # post_dummy_alerts.py
# import requests, random, datetime, time, argparse
# from dotenv import load_dotenv
# import os

# load_dotenv()
# API_KEY = os.getenv("API_KEY")
# URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000/ingest")

# SIGS = [
#     "ICMP PING detected",
#     "POTENTIAL PORTSCAN - SYN flood/scan",
#     "SSH Brute Force Attempt",
#     "HTTP suspicious user-agent",
#     "ARP Spoofing detected"
# ]

# def random_ip():
#     return f"192.168.{random.randint(0,5)}.{random.randint(2,250)}"

# def make_alert():
#     return {
#         "timestamp": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
#         "src_ip": random_ip(),
#         "src_port": random.randint(1024,65535),
#         "dest_ip": random_ip(),
#         "dest_port": random.choice([22,80,443,53]),
#         "proto": random.choice(["TCP","UDP","ICMP"]),
#         "alert": {
#             "signature": random.choice(SIGS),
#             "severity": random.randint(1,3)
#         }
#     }

# def main(count=20, delay=0.1):
#     headers = {"Content-Type": "application/json", "X-API-KEY": API_KEY}
#     for i in range(count):
#         a = make_alert()
#         try:
#             r = requests.post(URL, json=a, headers=headers, timeout=5)
#             print(i+1, r.status_code, r.text)
#         except Exception as e:
#             print("POST failed:", e)
#         time.sleep(delay)

# if __name__ == "__main__":
#     p = argparse.ArgumentParser()
#     p.add_argument("--count", type=int, default=20)
#     p.add_argument("--delay", type=float, default=0.1)
#     args = p.parse_args()
#     main(args.count, args.delay)