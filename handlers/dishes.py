from aiogram import Router, types
from aiogram.filters import Command
from bot_config import database

dish_router = Router()

@dish_router.message(Command("list_dish"))
async def list_dishes(message: types.Message):
    dishes = database.get_all_dishes()  # Получаем все блюда из БД
    if not dishes:
        await message.answer("Список блюд пуст.")
        return

    response = "📌 *Список блюд:*\n\n"
    for dish in dishes:
        response += f"🍽 *{dish['name']}*\n💰 Цена: {dish['price']} \n📖 Описание: {dish['description']} \n🍴 Порция: {dish['portion']}\n\n"

    await message.answer(response, parse_mode="Markdown")
