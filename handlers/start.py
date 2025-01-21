from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



start_router = Router()



kb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text='review', callback_data='review')]
])


@start_router.message(Command('start'))
async def start_handlers(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f'Привет {name}',reply_markup=kb)

