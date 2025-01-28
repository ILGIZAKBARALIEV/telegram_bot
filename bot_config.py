from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from database import Database
import asyncio
token= dotenv_values(".env")["TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
database = Database("db.db")

async def create_db_pool():
    return await asyncio.create_pool(
        user="ваш_пользователь",
        password="ваш_пароль",
        database="ваша_база",
        host="localhost"
    )

database = None