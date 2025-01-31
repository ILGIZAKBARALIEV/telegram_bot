from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram import F
from bot_config import database

dish_router = Router()

class Dish(StatesGroup):
    name = State()
    price = State()
    description = State()
    category = State()
    portion = State()
    photo = State()


@dish_router.message(Command("dish_add"))
async def add_dish(message: Message, state: FSMContext):
    await message.answer("Введите название блюда:")
    await state.set_state(Dish.name)

@dish_router.message(Dish.name)
async def process_name(m: Message, state: FSMContext):
    await state.update_data(name=m.text)
    await m.answer("Введите цену блюда:")
    await state.set_state(Dish.price)

@dish_router.message(Dish.price)
async def process_price(m: Message, state: FSMContext):
    try:
        price = float(m.text)
        await state.update_data(price=price)
        await m.answer("Введите описание блюда:")
        await state.set_state(Dish.description)
    except ValueError:
        await m.answer("Цена должна быть числом. Введите корректное значение:")

@dish_router.message(Dish.description)
async def process_description(m: Message, state: FSMContext):
    await state.update_data(description=m.text)
    await m.answer("Введите категорию блюда:")
    await state.set_state(Dish.category)

@dish_router.message(Dish.category)
async def process_category(m: Message, state: FSMContext):
    await state.update_data(category=m.text)
    await m.answer("Введите размер порции блюда:")
    await state.set_state(Dish.portion)

@dish_router.message(Dish.portion)
async def process_portion(m: Message, state: FSMContext):
    await state.update_data(portion=m.text)
    await m.answer("Пришлите фотографию блюда (если есть). Если нет, отправьте 'нет'.")
    await state.set_state(Dish.photo)

# Обработчик сообщений с фотографиями
@dish_router.message(Dish.photo, F.photo)
async def process_photo(m: Message, state: FSMContext):
    photo = m.photo[-1].file_id  # Получаем ID самого большого фото
    await state.update_data(photo=photo)

    data = await state.get_data()
    database.save_dish(data)

    await m.answer(f"✅ Блюдо {data['name']} успешно добавлено!")
    await state.clear()


@dish_router.message(Dish.photo)
async def process_no_photo(m: Message, state: FSMContext):
    if m.text.lower() == "нет":
        await state.update_data(photo=None)

        data = await state.get_data()
        database.save_dish(data)

        await m.answer(f"✅ Блюдо {data['name']} успешно добавлено!")
        await state.clear()
    else:
        await m.answer("Отправьте фотографию или напишите 'нет'.")
