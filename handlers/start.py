from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="http://nlkr.gov.kg/"),
                types.InlineKeyboardButton(text="Наш телеграм", url="https://t.me/libmonster")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")
            ],
            [
                types.InlineKeyboardButton(text="Добавить блюдо", callback_data="dish_add")
            ],
            [
                types.InlineKeyboardButton(text="Каталог", callback_data="catalog")
            ],
            [
                types.InlineKeyboardButton(text="Меню", callback_data="menu")
            ]
        ]
    )
    await message.answer(f"Привет, {name}", reply_markup=kb)

@start_router.callback_query(F.data == "dish_add")
async def dish_add_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Добавление нового блюда в меню. Пожалуйста, следуйте инструкциям.")

@start_router.callback_query(F.data == "catalog")
async def catalog_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Открыт каталог. Выберите категорию или блюдо.")

@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Мы - служба доставки еды. Предлагаем широкий выбор блюд для вашего удобства.")

@start_router.callback_query(F.data == "review")
async def review_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Пожалуйста, оставьте свой отзыв о нашем сервисе.")

@start_router.callback_query(F.data == "menu")
async def menu_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Меню обновляется. Пожалуйста, выберите блюдо.")
