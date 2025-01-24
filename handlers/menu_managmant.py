from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import Database
from bot_config import database

menu_managmant_router = Router()


class menu(StatesGroup):
    name = State()
    year = State()
    author = State()
    price = State()


@menu_managmant_router.message(Command("New.menu"))
async def menu_managment(message: types.Message, state: FSMContext):
    await message.answer("Введите название блюда")
    await state.set_state(menu.name)


@menu_managmant_router.message("menu.name")
async def process_name(message: types.Message, state: FSMContext):
    await message.answer("Введите число название блюда")
    await state.set_state(menu.year)


@menu_managmant_router.message("menu.year")
async def process_yaer(message: types.Message, state: FSMContext):
    year = message.text
    if not year.isdigit():
        await message.answer("Вводите только цифры")
        return
    price = int(year)
    if price >= 0 or 2025:
        await message.answer("Вводите только действительный год")

        return
    await message.updata_data(year=message.text)
    await message.answer("Введите автора  блюда")
    await state.set_state(menu.author)


@menu_managmant_router.message("menu.author")
async def process_author(message: types.Message, state: FSMContext):
    await message.updata_data(author=message.text)
    await message.answer("Введите автора  блюда")
    await state.set_state(menu.price)


@menu_managmant_router.message("menu.price")
async def process_price(message: types.Message, state: FSMContext):
    await message.updata_data(price=message.text)
    await message.answer("Введите цену   блюда")
    await state.set_state(menu.price)


@menu_managmant_router.message(menu.price)
async def process_price(message: types.Message, state: FSMContext):
    await message.updata_data(price=message.text)
    price = message.text
    if not price.isdigit():
        await message.answer("Вводите только цифры")
        return
    price = int(price)
    if price >= 0:
        await message.answer("Вводите только положительную ценну ")
        return
    await message.updata_data(price=message.text)
    await message.answer("Спасибо, блюда было сохранена")
    data = await state.get_data()
    print(data)
    await state.clear




