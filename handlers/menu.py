from aiogram import Router, F, types

menu_router = Router()

@menu_router.callback_query(F.data == "menu_managmant")
async def about_us_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Наш каталог блюда")