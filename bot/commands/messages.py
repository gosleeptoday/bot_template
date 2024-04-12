import os
import pandas as pd
from aiogram import types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from commands import commands_router
from repository.user import MessagesRepository

@commands_router.message(Command("messages"))
async def export_messages_to_excel(message: types.Message):
    messages = await MessagesRepository.get_all_messages()

    df = pd.DataFrame(messages)
    df = df.map(lambda x: x[1] if isinstance(x, tuple) else x)
    
    df = df.rename(columns={"date": "Дата", "telegram_id": "Telegram ID", "message": "Сообщение"})

    if len(df.columns) > 2:
        df = df.drop(df.columns[2], axis=1)
    excel_filename = "messages_export.xlsx"
    df.to_excel(excel_filename, index=False)
    
    excel_file = FSInputFile(excel_filename, filename="messages_export.xlsx")
    await message.reply_document(excel_file)
    os.remove(excel_filename)
