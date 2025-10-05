# # populate_alerts.py
# import sqlite3
# import random
# import datetime
# import argparse
# import os
# from dotenv import load_dotenv

# load_dotenv()
# DB_PATH = os.getenv("DB_NAME", "alerts.db")

# SAMPLE_SIGNATURES = [
#     "ICMP PING detected",
#     "POTENTIAL PORTSCAN - SYN flood/scan",
#     "SSH Brute Force Attempt",
#     "HTTP suspicious user-agent",
#     "ARP Spoofing detected"
# ]
# PROTOS = ["TCP", "UDP", "ICMP"]

# def random_ip():
#     return f"192.168.{random.randint(0,5)}.{random.randint(2,250)}"

# def insert(conn, ts, src, dst, proto, sig, sev):
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO Alerts (timestamp, src_ip, dest_ip, proto, signature, severity) VALUES (?, ?, ?, ?, ?, ?)",
#         (ts, src, dst, proto, sig, sev)
#     )
#     conn.commit()

# def main(count=20):
#     if not os.path.exists(DB_PATH):
#         print("DB not found:", DB_PATH)
#         return
#     conn = sqlite3.connect(DB_PATH)
#     for i in range(count):
#         ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
#         insert(conn, ts, random_ip(), random_ip(), random.choice(PROTOS), random.choice(SAMPLE_SIGNATURES), random.randint(1,3))
#     conn.close()
#     print("Inserted", count, "alerts into", DB_PATH)

# if __name__ == "__main__":
#     p = argparse.ArgumentParser()
#     p.add_argument("--count", type=int, default=20)
#     args = p.parse_args()
#     main(args.count)