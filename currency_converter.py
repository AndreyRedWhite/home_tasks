import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from config import telegram_api_key

API_TOKEN = telegram_api_key # Замените YOUR_TOKEN на токен вашего бота

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Отправь мне сумму в индонезийских рупиях, и я переведу её в российские рубли.")


@dp.message(F.text)
async def convert(message: types.Message):
    try:
        amount = float(message.text) * 1000
        result = amount / 162
        await message.answer(f'{amount} IDR равно {result:.2f} RUB')
    except ValueError:
        await message.answer('Пожалуйста, отправьте мне число.')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

