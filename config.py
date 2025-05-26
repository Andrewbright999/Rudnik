import os, json
from dotenv import load_dotenv 

load_dotenv() 

TG_TOKEN = os.getenv("TG_TOKEN")

with open("config.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    ADMIN_LIST = data["admins"]
    GROUP_ID = data["groups"]

#  /etc/systemd/system/curs_bot.service                                        
# [Unit]
# Description=tolgonai curs bot
# After=network.target

# [Service]
# User=root
# Group=root
# WorkingDirectory=/root/bots/curs_bot
# ExecStart=/root/bots/curs_bot/venv/bin/python main.py
# Restart=always

# [Install]
# WantedBy=multi-user.target



