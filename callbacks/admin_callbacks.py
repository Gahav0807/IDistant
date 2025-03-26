from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.common import main_menu

admin_router = Router()

# Состояния администратора при ответе
class AdminReplyState(StatesGroup):
    replying = State()
    in_dialog = State()  # Новое состояние для продолжения диалога

pending_requests = {}  # Храним заявки пользователей

# Обработчик для начала ответа админа по заявке
@admin_router.callback_query(lambda c: c.data.startswith("admin_reply:"))
async def admin_start_reply(callback: types.CallbackQuery, state: FSMContext):
    user_id = int(callback.data.split(":")[1])
    await state.update_data(user_id=user_id)
    await callback.message.answer(
        "Введите ваш ответ пользователю (или нажмите 'Завершить диалог', чтобы закончить):",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Завершить диалог")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await state.set_state(AdminReplyState.replying)

# Обработчик ввода ответа от администратора
@admin_router.message(AdminReplyState.replying)
async def admin_send_reply(message: types.Message, state: FSMContext):
    if message.text == "Завершить диалог":
        await message.answer(
            "Диалог завершён.",
            reply_markup=main_menu
        )
        await state.clear()
        return
    
    data = await state.get_data()
    user_id = data["user_id"]
    
    try:
        await message.bot.send_message(
            chat_id=user_id,
            text=f"📢 Ответ от менеджера:\n\n{message.text}"
        )
        await message.answer(
            "✅ Ваш ответ отправлен. Продолжайте писать или нажмите 'Завершить диалог'.",
            reply_markup=types.ReplyKeyboardMarkup(
                keyboard=[
                    [types.KeyboardButton(text="Завершить диалог")]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )
    except Exception as e:
        await message.answer(f"❌ Ошибка при отправке: {e}")
        await state.clear()