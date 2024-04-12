from datetime import datetime
from database.models import User, Messages


class UserRepository(object):
    @staticmethod
    async def exists_by_id(user_id: int) -> bool:
        return await User.exists(id=user_id)

    @staticmethod
    async def exists_by_telegram_id(telegram_id: int) -> bool:
        return await User.exists(telegram_id=telegram_id)

    @staticmethod
    async def create_user(telegram_id: int) -> None:
        await User.create(telegram_id=telegram_id)

    @staticmethod
    async def user_count() -> int:
        return len(await User.all())

    @staticmethod
    async def get_all_users() -> list[User]:
        return await User.all()

class MessagesRepository(object):
    @staticmethod
    async def save_message(user_id: int, message: str) -> None:
        await Messages.create(telegram_id=user_id, message=message, date=datetime.now())

    @staticmethod
    async def get_all_messages() -> list[Messages]:
        return await Messages.all()