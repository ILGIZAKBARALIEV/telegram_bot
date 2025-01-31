from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ChatPermissions
from datetime import datetime, timedelta
from aiogram.exceptions import TelegramBadRequest

admin_router = Router()

FORBIDDEN_WORDS = {"xd"}

def parse_time(time_str: str):
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    try:
        unit = time_str[-1]
        value = int(time_str[:-1])
        return value * units.get(unit, 60)
    except ValueError:
        return 600

@admin_router.message(F.chat.type.in_({"group", "supergroup"}))
async def check_message(message: types.Message):
    if any(word in message.text.lower() for word in FORBIDDEN_WORDS):
        try:
            await message.chat.ban_chat_member(user_id=message.from_user.id)
            await message.answer(f"{message.from_user.first_name} был забанен за использование запрещённых слов.")
        except TelegramBadRequest:
            await message.answer("Не удалось забанить пользователя.")

@admin_router.message(Command("ban"))
async def ban_user(message: types.Message):
    args = message.text.split()
    if len(args) < 2 and not message.reply_to_message:
        await message.answer("Использование: /ban @username [время] или ответьте на сообщение пользователя.")
        return

    duration = parse_time(args[2]) if len(args) > 2 else 600

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
    else:
        mention = args[1]
        if mention.startswith("@"):
            try:
                member = await message.chat.get_chat_member(mention[1:])
                user_id = member.user.id
                user_name = member.user.first_name
            except:
                await message.answer("Не удалось найти пользователя по @username.")
                return
        else:
            await message.answer("Некорректное использование команды.")
            return

    try:
        until_date = datetime.now() + timedelta(seconds=duration)
        await message.chat.ban_chat_member(user_id=user_id, until_date=until_date)
        await message.answer(f"Пользователь {user_name} забанен на {duration // 60} минут.")
    except TelegramBadRequest:
        await message.answer("Не удалось забанить пользователя.")
