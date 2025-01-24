import  asyncio
import logging
from aiogram import Bot
from bot_config import bot, dp,database
from handlers import (start, myinfo, random,review_dialog,)
from  handlers.menu_managmant import menu_managmant_router

async  def on_startup(bot:Bot):
    database.create_tables()

async  def main():
    dp.include_router(myinfo.myinfo_router)
    dp.include_router(random.random_router)
    dp.include_router(start.start_router)
    dp.include_router(review_dialog.review_router)
    dp.include_router(menu_managmant_router)
    dp.include_router(myinfo.other_router)


    dp.startup.register(on_startup)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())