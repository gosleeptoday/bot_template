from aiogram import Bot, types
from aiogram.filters.command import Command, CommandObject
from aiogram.fsm.context import FSMContext
from commands import commands_router
from keyboards import actions_keyboard, cancel_actions_keyboard
from states import UserActionState

@commands_router.message(Command("actions"))
async def user_actions(message: types.Message, command: CommandObject, state: FSMContext):

    await state.set_state(UserActionState.message)
    await message.reply(
        f"очень рад видеть пользователя",
        reply_markup=actions_keyboard,
    )

@commands_router.callback_query(UserActionState.message)
async def user_actions_buttons(call: types.CallbackQuery, state: FSMContext):
    if call.data == "reg":
        await call.message.answer("Начнем регистрацию. Напишите ФИО", reply_markup=cancel_actions_keyboard)
        await state.set_state(UserActionState.FIO)
    elif call.data == "info":
        await call.message.answer(" я крутой бот, я помогаю людям! ")

@commands_router.message(UserActionState.FIO)
async def user_fio(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await state.clear()
        await message.reply("Регистрация отменена.")
        return
    await message.reply("Отлично! Теперь укажите свой возраст:", reply_markup=cancel_actions_keyboard)
    await state.set_state(UserActionState.Age)


@commands_router.message(UserActionState.Age)
async def user_age(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await state.clear()
        await message.reply("Регистрация отменена.")
        return
    await message.reply("Спасибо! Теперь укажите свою почту:",reply_markup=cancel_actions_keyboard)
    await state.set_state(UserActionState.Email)


@commands_router.message(UserActionState.Email)
async def user_email(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await state.clear()
        await message.reply("Регистрация отменена.")
        return
    await message.reply("Отлично! Пожалуйста, укажите свой номер телефона:",reply_markup=cancel_actions_keyboard)
    await state.set_state(UserActionState.Phone)


@commands_router.message(UserActionState.Phone)
async def user_phone(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await state.clear()
        await message.reply("Регистрация отменена.")
        return
    user_data = await state.get_data()
    user_info = (
        f"ФИО: {user_data.get('fio')}\n"
        f"Возраст: {user_data.get('age')}\n"
        f"Email: {user_data.get('email')}\n"
        f"Телефон: {message.text}"
    )

    await message.reply(user_info)
    await state.clear()
    await message.reply("Спасибо за регистрацию!")