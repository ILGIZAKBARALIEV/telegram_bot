from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram import types



start_router = Router()



kb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text='Review', callback_data='review')]
])


@start_router.message(Command('start'))
async def start_handlers(message: types.Message):
    name = message.from_user.fist_name
    await message.answer(f'Привет {name}',reply_markup=kb)
