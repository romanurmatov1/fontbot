from app import bot, dp
from config import admin_id
import json

from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
   await bot.send_message(chat_id=admin_id, text="<i>Salom Raxmatjon bot ishga tushdi</i>", parse_mode='HTML')
@dp.message_handler()
async def echo(message: Message):
   chat_id = message["from"]["id"]
   text = message.text
   if text == '/start':
      await bot.send_message(chat_id=chat_id, text="Iltimos bir nima deb yozing!")
   else:
      await bot.send_message(chat_id=chat_id, text=f"<b>{text}</b>", parse_mode='HTML')
      await bot.send_message(chat_id=chat_id, text=f"<i>{text}</i>", parse_mode='HTML')
      await bot.send_message(chat_id=chat_id, text=f"<u>{text}</u>", parse_mode='HTML')
      await bot.send_message(chat_id=chat_id, text=f"<pre>{text}</pre>", parse_mode='HTML')
      await bot.send_message(chat_id=chat_id, text=f"<s>{text}</s>", parse_mode='HTML')
   
   # await message.answer(text=text)