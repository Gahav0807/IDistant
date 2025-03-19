import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from handlers import start
from handlers.buy import apple_buy
from handlers.sell import apple_sell
from handlers.repair import apple_repair
from handlers.trade import apple_trade

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(start.router)
dp.include_router(apple_buy.apple_buy_router)
dp.include_router(apple_sell.apple_sell_router)
dp.include_router(apple_repair.apple_repair_router)
dp.include_router(apple_trade.apple_trade_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())