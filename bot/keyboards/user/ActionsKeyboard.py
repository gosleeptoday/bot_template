from aiogram import types

keyboard = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Регистрация", callback_data="reg"),
            types.InlineKeyboardButton(text="Информация", callback_data="info"),
        ]
    ]
)

kb = [
        [types.KeyboardButton(text="отмена")],
    ]
cancel_actions_keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard= True)