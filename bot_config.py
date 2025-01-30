from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from database import Database
import asyncio
token= dotenv_values(".env")["TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
database = Database("bot_database.db")
