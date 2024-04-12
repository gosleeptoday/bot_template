import os
from aiogram import types
from aiogram.filters.command import Command
from commands import commands_router
from config import ADMIN_IDS

@commands_router.message(Command("send_cat_photo"))
async def send_cat_photo(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    photo_path = "static/img/cat.jpg"
    if not os.path.exists(photo_path):
        await message.reply("Файл с фотографией кота не найден.")
        return
    await message.reply_photo(photo=types.FSInputFile(photo_path))
