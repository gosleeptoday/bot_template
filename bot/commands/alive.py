from aiogram import types
from aiogram.filters.command import Command
import requests
from commands import commands_router


@commands_router.message(Command("alive"))
async def check_alive(message: types.Message):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            await message.reply("Приложение работает и доступно.")
        else:
            await message.reply("Приложение не доступно в данный момент.")
    except Exception as e:
        await message.reply(f"Ошибка при проверке состояния приложения: {e}")