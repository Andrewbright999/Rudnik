import os
from dotenv import load_dotenv 

load_dotenv() 

TG_TOKEN = os.getenv("TG_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")
ADMIN_ID = os.getenv("ADMIN_ID")
