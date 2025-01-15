import  asyncio
from bot_config import bot, dp
from handlers import (start, myinfo, random)


async  def main():
    dp.include_router(myinfo.myinfo_router)
    dp.include_router(random.random_router)
    dp.include_router(start.start_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
        asyncio.run(main())