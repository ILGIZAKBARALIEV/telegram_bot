from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram import types

start_router = Router()


@start_router.message(Command('start'))
async def star_handlers(message: types.Message):
    name = message.from_user.fist_name
    await message.answer(f'Привет {name}\n'
                         f'Мои команды:')
