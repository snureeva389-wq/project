import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот-каталог книг.\n"
        "Пришли мне фразу из книги, и я найду, откуда она.\n"
        "Список команд: /help"
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Команды бота:\n"
        "/start — приветствие\n"
        "/help — список команд\n"
        "/search — поиск книги по цитате (скоро)\n"
        "/quote — цитата дня (скоро)\n"
        "/mybooks — мой список чтения (скоро)"
    )


async def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN не найден. Создайте файл .env по образцу .env.example")
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())