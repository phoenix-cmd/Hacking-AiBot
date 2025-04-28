
# import logging
# import os
# import sys
# from inspect import getfullargspec
# from os import getenv
# from decouple import config
# import time
# from datetime import datetime
# from telethon import TelegramClient
# from telethon.sessions import StringSession

# REPO_NAME =  "Hacking-AiBot"
# StartTime = time.time()

# # logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# API_ID = config("API_ID", default=None, cast=int)
# API_HASH = config("API_HASH", default=None)
# OWNER_ID = config("OWNER_ID", cast=int)
# BOT_ID = config("BOT_ID", cast=int)
# BOT_USERNAME = config("BOT_USERNAME")
# HEROKU_API_KEY = config("HEROKU_API_KEY", default=None)
# HEROKU_APP_NAME  = config("HEROKU_APP_NAME", default=None)
# Bot_Token = config("Bot_Token", default=None)
# HNDLR = config("HANDLER")
# SUDO_USERS = list(map(int, config("SUDO_USERS").split()))
# DEV_USERS = list(map(int, config("DEV_USERS").split()))
# hn = HNDLR #lay-z af

# SUDO_USERS.append(OWNER_ID)
# DEV_USERS.append(OWNER_ID)
# SUDO_USERS = list(SUDO_USERS)
# DEV_USERS = list(DEV_USERS)

# #TELETHON BOT
# print("[INFO]: STARTING TELETHON BOT CLIENT")
# BotClient = TelegramClient('Bot', API_ID, API_HASH).start(bot_token=Bot_Token)
import logging
import os
import sys
from inspect import getfullargspec
from os import getenv
from decouple import config
import time
from datetime import datetime
from telethon import TelegramClient
from telethon.sessions import StringSession

REPO_NAME = "Hacking-AiBot"
StartTime = time.time()

# logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Load environment variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
OWNER_ID = config("OWNER_ID", cast=int)
BOT_ID = config("BOT_ID", cast=int)
BOT_USERNAME = config("BOT_USERNAME")
HEROKU_API_KEY = config("HEROKU_API_KEY", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
Bot_Token = config("Bot_Token", default=None)  # Bot token from environment variables
HNDLR = config("HANDLER")
SUDO_USERS = list(map(int, config("SUDO_USERS").split()))
DEV_USERS = list(map(int, config("DEV_USERS").split()))
hn = HNDLR  # lay-z af

# Ensure the Bot Token is available
if not Bot_Token:
    raise ValueError("Bot token is not set. Please configure the Bot_Token environment variable.")

# Adding OWNER_ID to SUDO and DEV users
SUDO_USERS.append(OWNER_ID)
DEV_USERS.append(OWNER_ID)
SUDO_USERS = list(SUDO_USERS)
DEV_USERS = list(DEV_USERS)

# TELETHON BOT
print("[INFO]: STARTING TELETHON BOT CLIENT")
BotClient = TelegramClient('Bot', API_ID, API_HASH).start(bot_token=Bot_Token)

