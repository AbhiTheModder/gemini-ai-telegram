# This scripts contains use cases for group bots
import os
import asyncio
import PIL.Image
import google.generativeai as genai

from pyrogram import Client, filters, enums
from pyrogram.types import Message

API_KEY= os.environ['API_KEY']

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro-vision")
model_text = genai.GenerativeModel("gemini-pro")

API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']

app = Client("gemini_ai", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("askai") & filters.group)
async def say(_, message: Message):
    try:
        i = await message.reply_text("<code>Please Wait...</code>")
        
        
        if len(message.command) > 1:
         prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
         prompt = message.reply_to_message.text
        else:
         await message.reply_text(
            f"<b>Usage: </b><code>/askai [prompt/reply to message]</code>"
        )
         return

        chat = model_text.start_chat()
        response = chat.send_message(prompt)
        await i.delete()

        await message.reply_text(f"**Question:**`{prompt}`\n**Answer:** {response.text}", parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

@app.on_message(filters.text & filters.private)
async def say(_, message: Message):
    try:
        i = await message.reply_text("<code>Please Wait...</code>")

        prompt = message.text
        chat = model_text.start_chat()
        response = chat.send_message(prompt)
        await i.delete()

        await message.reply_text(f"**Question:**`{prompt}`\n**Answer:** {response.text}", parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

@app.on_message(filters.command("getai") & filters.group)
async def say(_, message: Message):
    try:
        i = await message.reply_text("<code>Please Wait...</code>")

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)

        response = model.generate_content(img)
        await i.delete()

        await message.reply_text(
            f"**Detail Of Image:** {response.text}", parse_mode=enums.ParseMode.MARKDOWN
        )
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
    finally:
        os.remove(base_img)

if __name__ == "__main__":
    app.run()
