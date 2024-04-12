from repository.user import MessagesRepository
from aiogram import F, types
from handlers import handle_router

@handle_router.message(F.text)
async def handle_text_message(message: types.Message):
    user_id = message.from_user.id
    text_message = message.text
    print("save")
    await MessagesRepository.save_message(user_id, text_message)