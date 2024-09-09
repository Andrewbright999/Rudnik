import os, json
from dotenv import load_dotenv 

load_dotenv() 

TG_TOKEN = os.getenv("TG_TOKEN")

with open("config.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    ADMIN_LIST = data["admins"]
    GROUP_ID = data["groups"]
    LESDS_FIELDS = data["leads_fields"]

GROUP_ID = os.getenv("GROUP_ID")
ADMIN_ID = os.getenv("ADMIN_ID")
