import os
import PIL.Image
import google.generativeai as genai

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from utils.misc import modules_help, prefix
from utils.scripts import format_exc

API_KEY="your api key here"

model = genai.GenerativeModel("gemini-pro-vision")


@Client.on_message(filters.command("aimage", prefix) & filters.me)
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
        await message.edit_text(f"An error occurred: {format_exc(e)}")
    finally:
        os.remove(base_img)


modules_help["aimage"] = {
    "aimage [reply to image]*": "Get details of image with Ai",
}

