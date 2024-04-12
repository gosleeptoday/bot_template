from aiogram import types
from aiogram.filters.command import Command
from commands import commands_router

@commands_router.message(Command("my_info"))
async def command_start_hendler(message: types.Message):
    await message.reply(
        f"uid: {message.from_user.id}\nfio: {message.from_user.full_name}\nusername: @{message.from_user.username}\npremium: {message.from_user.is_premium}"
        )
