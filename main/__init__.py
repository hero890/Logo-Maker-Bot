import aiohttp
from pyrogram import Client
from config import *

app = Client(
  "bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

print("[INFO]: STARTING BOT....[click Here](https://t.me/aapna_Movies)")
app.start()

print("[INFO]: STARTING AIOHTTP CLIENT")
session = aiohttp.ClientSession()
