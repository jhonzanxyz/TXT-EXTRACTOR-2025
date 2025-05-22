import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "29344139"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "6972ba754ccab4894a193ac7b5150325")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7842780078:AAG-8EEvMIq9iofWEkTgIc_HdCQn2fq5j14")

OWNER_ID = int(os.environ.get("OWNER_ID", "6444269766"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "6444269766").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002610392890"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002656760888")  # Optional here you'll get all logs
