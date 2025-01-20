from aiogram import Bot,Dispatcher,Router
from aiogram.filters import Command
from aiogram import types

myinfo_router = Router()

@myinfo_router.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.full_name
    nickname = message.from_user.username
    await message.answer(f"Вашк имя: {name}:"
                         f"Ваш nickname {nickname}:"
                         f"Ваш id {id}")