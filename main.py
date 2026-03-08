import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# ТВОЙ ТОКЕН
BOT_TOKEN = "8608243620:AAFLIgT0DPFFRbBYSdp2lgs-HsQuTZlMSUI"

# ССЫЛКА НА НОВЫЙ САЙТ
WEB_APP_URL = "https://aml-ton-wallet-new.vercel.app"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    """Приветственное сообщение без Markdown"""
    
    welcome_text = """
🛡️ Добро пожаловать в AML Ton Wallet!

🔐 Безопасная верификация TON кошельков

⚡ Как это работает:
1. Нажми кнопку "Открыть приложение"
2. Подключи свой TON кошелек
3. Пройди верификацию

👇 Нажми кнопку ниже, чтобы начать
    """
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="🚀 Открыть AML Ton Wallet",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]]
    )
    
    await message.answer(
        welcome_text,
        reply_markup=keyboard
    )

@dp.message()
async def help_handler(message: types.Message):
    """Ответ на другие сообщения"""
    await message.answer("Используй /start для запуска")

async def main():
    logging.info("Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())