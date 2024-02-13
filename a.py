import asyncio
import time

from pyrogram import filters, Client, idle
from pyrogram.errors import FloodWait
from pyrogram.types import Message


# -----------------------------------------------------------------#

API_ID = 9181587
API_HASH = "77939cad267feab33e6c32bd9e32eb1f"

app = Client("userbot", api_id = API_ID, api_hash = API_HASH)




@app.on_message(filters.private & filters.me)
async def download(app, message):
	try:
		await message.reply_text("Working")
	except Exception as err:
		print(err)

app.start()
print("Program started, 120 seconds to test")
#idle()
time.sleep(120)
print("Program stopped")
app.stop()
