# This scripts contains use cases for simple bots
# import requirements 
import os
import asyncio
import PIL.Image
import google.generativeai as genai
from pathlib import Path
from pyrogram import Client, filters, enums
from pyrogram.types import Message

generation_config_cook = {
  "temperature": 0.35,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}

# API KEYS
# Gemini Ai API KEY
API_KEY= os.environ['API_KEY']
# Telegram Auth API ID
API_ID = os.environ['API_ID']
# Telegram Auth API HASH
API_HASH = os.environ['API_HASH']
# Telegram Bot API TOKEN generated from @botfather
BOT_TOKEN = os.environ['BOT_TOKEN']

# configure API KEY for gemini 
genai.configure(api_key=API_KEY)

# Setup models
model = genai.GenerativeModel("gemini-pro-vision")
model_text = genai.GenerativeModel("gemini-pro")
model_cook = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config_cook)
# configure pyrogram client 
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
         await i.delete()
         await message.reply_text(
            f"<b>Usage: </b><code>/askai [prompt/reply to message]</code>"
        )
         return

        chat = model_text.start_chat()
        response = chat.send_message(prompt)
        await i.delete()

        await message.reply_text(f"**Answer:** {response.text}", parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        await i.delete()
        await message.reply_text(f"An error occurred: {str(e)}")

@app.on_message(filters.text & filters.private)
async def say(_, message: Message):
    try:

        prompt = message.text
        chat = model_text.start_chat()
        response = chat.send_message(prompt)
        await message.reply_chat_action(enums.ChatAction.TYPING)

        await message.reply_text(f"{response.text}", parse_mode=enums.ParseMode.MARKDOWN)
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
            f"**Detail Of Image:** {response.parts[0].text}", parse_mode=enums.ParseMode.MARKDOWN
        )
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(str(e))

@app.on_message(filters.command("aicook") & filters.group)
async def say(_, message: Message):
    try:
        i = await message.reply_text("<code>Cooking...</code>")

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)
        cook_img = [
        "Accurately identify the baked good in the image and provide an appropriate and recipe consistent with your analysis. ",
        img,
        ]

        response = model_cook.generate_content(cook_img)
        await i.delete()

        await message.reply_text(
            f"{response.text}", parse_mode=enums.ParseMode.MARKDOWN
        )
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(str(e))

@app.on_message(filters.command("aiseller") & filters.group)
async def say(_, message: Message):
    try:
        i = await message.reply_text("<code>Generating...</code>")
        if len(message.command) > 1:
         taud = message.text.split(maxsplit=1)[1]
        else:
         await i.delete()
         await message.reply_text(
            f"<b>Usage: </b><code>/aiseller [target audience] [reply to product image]</code>"
        )
         return

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)
        sell_img = [
        "Given an image of a product and its target audience, write an engaging marketing description",
        "Product Image: ",
        img,
        "Target Audience: ",
        taud
        ]

        response = model.generate_content(sell_img)
        await i.delete()

        await message.reply_text(
            f"{response.text}", parse_mode=enums.ParseMode.MARKDOWN
        )
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(f"<b>Usage: </b><code>/aiseller [target audience] [reply to product image]</code>")

# Run the bot
if __name__ == "__main__":
    app.run()
