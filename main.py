import  asyncio
import logging
from aiogram import Bot
from bot_config import  bot, dp,database
from handlers import (start, myinfo, random, review_dialog,dish_fsm,dishes,admin,name,)

async  def main():
    dp.include_router(myinfo.myinfo_router)
    dp.include_router(name.name_router)
    dp.include_router(random.random_router)
    dp.include_router(review_dialog.review_router)
    dp.include_router(start.start_router)
    dp.include_router(dish_fsm.dish_router)
    dp.include_router(dishes.dish_router)
    dp.include_router(admin.admin_router)
    database.create_tables()
    dp.include_router(myinfo.other_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())