from aiogram import Router, types
from aiogram.filters import Command
from keyboards.common import main_menu, buy_menu, sell_menu  # Предположим, что у нас есть главное меню с кнопками

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    # Приветственное сообщение
    welcome_message = (
        "Привет! 👋\n"
        "Я помогу тебе с покупкой, продажей, ремонтом устройств и многим другим.\n"
        "Выбери, что ты хочешь сделать:\n"
    )
    
    # Отправляем приветственное сообщение с кнопками
    await message.answer(welcome_message, reply_markup=main_menu)


@router.message(lambda message: message.text == "Главное меню")
async def start_buy(message: types.Message):
    await message.answer("Вы находитесь в главном меню", reply_markup=main_menu)

@router.message(lambda message: message.text == "Купить")
async def start_buy(message: types.Message):
    await message.answer("Выберите категорию устройства:", reply_markup=buy_menu)

@router.message(lambda message: message.text == "Продать")
async def start_buy(message: types.Message):
    await message.answer("Выберите категорию устройства:", reply_markup=sell_menu)