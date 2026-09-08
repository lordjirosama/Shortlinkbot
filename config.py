import os
from typing import List

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7754709357"))
PICS = (os.environ.get("PICS", "https://graph.org/file/0591ce5558c3ec8fe7612-263292508134daf3e1.jpg https://graph.org/file/fdc4357abfaba23255e98-24d1bbfa3888cdfcfe.jpg")).split()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1004337666340"))
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "approve")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "-1002449922957").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
