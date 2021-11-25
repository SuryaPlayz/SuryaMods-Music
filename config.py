import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "dlwrml")
ALIVE_NAME = getenv("ALIVE_NAME", "SuryaModsOwner")
BOT_USERNAME = getenv("BOT_USERNAME", "Surya_MusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Surya_MusicAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "SuryaModsChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SuryaModsYTl")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b1ec962de7edaba274291.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("https://telegra.ph/file/b1ec962de7edaba274291.jpg")
IMG_2 = getenv("https://telegra.ph/file/b1ec962de7edaba274291.jpg")
