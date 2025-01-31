from aiogram import Router, types
from aiogram.filters import Command
from bot_config import database

dish_router = Router()

@dish_router.message(Command("list_dish"))
async def list_dishes(message: types.Message, page: int = 1):
    limit = 5
    offset = (page - 1) * limit
    dishes = database.get_list_dish(limit=limit, offset=offset)
    total_dish = len(database.get_list_dish())
    total_pages = (total_dish + limit - 1) // limit

    if not dishes:
        await message.answer("Список блюд пуст.")
        return

    response = "📌 *Список блюд:*\n\n"
    for dish in dishes:
        response += f"🍽 *{dish['name']}*\n💰 Цена: {dish['price']} \n📖 Описание: {dish['description']} \n🍴 Порция: {dish['portion']}\n"


        if 'photo' in dish and dish['photo']:
            await message.answer(response, photo=dish['photo'])
        else:
            await message.answer(response)

        response = ""  # Сбросим response для следующего блюда


    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[])  # создаем пустой inline_keyboard
    if page > 1:
        keyboard.row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page_{page - 1}"))
    if page < total_pages:
        keyboard.row(types.InlineKeyboardButton(text="Вперед ➡️", callback_data=f"page_{page + 1}"))

    if total_pages > 1:
        await message.answer(f"Страница {page}/{total_pages}", reply_markup=keyboard)

@dish_router.callback_query(lambda c: c.data.startswith("page_"))
async def pagination_handler(callback: types.CallbackQuery):
    page = int(callback.data.split("_")[1])
    await list_dishes(callback.message, page=page)
    await callback.answer()
