from aiogram import Router, types
from aiogram.filters import Command
from keyboards import main_menu  # Предположим, что у нас есть главное меню с кнопками

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
