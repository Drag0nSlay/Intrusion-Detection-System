# utils/logger.py
import logging
import os
from dotenv import load_dotenv

load_dotenv()
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

# ensure logs dir exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logger = logging.getLogger("ids_backend")
logger.setLevel(logging.INFO)

# avoid duplicate handlers
if not logger.handlers:
    fh = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

def log_info(msg):
    logger.info(msg)

def log_error(msg):
    logger.error(msg)