# This scripts contains use cases for simple bots

import os
import PIL.Image
import google.generativeai as genai

from pyrogram import Client, filters, enums
from pyrogram.types import Message

API_KEY="your gemini api key here"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro-vision")

API_ID = your_api_id
API_HASH = 'your_api_hash'
BOT_TOKEN = 'your_bot_token'

app = Client("gemini_ai_image", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
        chat = model.start_chat()
        prompt = "Hi"
        response = chat.send_message(prompt)
    
        await message.reply_text(f"{response.text}", parse_mode=enums.ParseMode.MARKDOWN)

@app.on_message(filters.command("ask") & filters.private)
async def say(_, message: Message):
    try:
        await message.edit_text("<code>Please Wait...</code>")
        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)

        response = model.generate_content(img)

        await message.edit_text(
            f"**Detail Of Image:** {response.text}", parse_mode=enums.ParseMode.MARKDOWN
        )
    except Exception as e:
        await message.edit_text(f"An error occurred: {str(e)}")
    finally:
        os.remove(base_img)

if __name__ == "__main__":
    app.run()
