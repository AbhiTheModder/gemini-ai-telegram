# This scripts contains use cases for userbots
# This is used on my Moon-Userbot: https://github.com/The-MoonTg-project/Moon-Userbot
# YOu can check it out for uses example
import os
import google.generativeai as genai

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from utils.misc import modules_help, prefix
from utils.scripts import format_exc
# from utils.config import GEMINI_KEY


API_KEY="your gemini api key here"


# genai.configure(api_key=GEMINI_KEY)
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')


@Client.on_message(filters.command("gemini", prefix) & filters.me)
async def say(_, message: Message):
    try:
        await message.edit_text("<code>Please Wait...</code>")

        if len(message.command) > 1:
         prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
         prompt = message.reply_to_message.text
        else:
         await message.edit_text(
            f"<b>Usage: </b><code>{prefix}gemini [prompt/reply to message]</code>"
        )
         return
    
        chat = model.start_chat()
        response = chat.send_message(prompt)
    
        await message.edit_text(f"**Question:**`{prompt}`\n**Answer:** {response.text}", parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        await message.edit_text(f"An error occurred: {format_exc(e)}")


modules_help["gemini"] = {
    "gemini [prompt]*": "Ask questions with Ai",
}
