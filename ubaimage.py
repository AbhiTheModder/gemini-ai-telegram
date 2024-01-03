# This scripts contains use cases for userbots
# This is used on my Moon-Userbot: https://github.com/The-MoonTg-project/Moon-Userbot
# YOu can check it out for uses example
import os
import PIL.Image
import google.generativeai as genai

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from utils.misc import modules_help, prefix
from utils.scripts import format_exc

# from utils.config import GEMINI_KEY

API_KEY="your gemini api key here"


# genai.configure(api_key=GEMINI_KEY)
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro-vision")


@Client.on_message(filters.command("aimage", prefix) & filters.me)
async def say(_, message: Message):
    try:
        await message.edit_text("<code>Please Wait...</code>")
        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)

        response = model.generate_content(img)

        await message.edit_text(
            f"**Detail Of Image:** {response.parts[0].text}", parse_mode=enums.ParseMode.MARKDOWN
        )
    except Exception as e:
        await message.edit_text(f"An error occurred: {format_exc(e)}")
    finally:
        os.remove(base_img)


modules_help["aimage"] = {
    "aimage [reply to image]*": "Get details of image with Ai",
}

