import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from handlers import start, sell, repair
from handlers.buy import apple
from handlers.buy import android

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(start.router)
dp.include_router(android.android_buy_router)
dp.include_router(apple.apple_buy_router)
# dp.include_router(sell.router)
# dp.include_router(repair.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())