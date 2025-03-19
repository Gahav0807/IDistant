from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup

admin_router = Router()

# Состояние администратора при ответе
class AdminReplyState(StatesGroup):
    replying = State()

pending_requests = {}  # Храним заявки пользователей

# Обработчик для ответа админу по заявке
@admin_router.callback_query(lambda c: c.data.startswith("admin_reply:"))
async def admin_start_reply(callback: types.CallbackQuery, state: FSMContext):
    user_id = int(callback.data.split(":")[1])
    await state.update_data(user_id=user_id)
    await callback.message.answer("Введите ваш ответ пользователю:")
    await state.set_state(AdminReplyState.replying)

# Обработчик ввода ответа от администратора
@admin_router.message(AdminReplyState.replying)
async def admin_send_reply(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = data["user_id"]
    await message.bot.send_message(chat_id=user_id, text=f"📢 Ответ от менеджера:\n\n{message.text}")
    await message.answer("✅ Ваш ответ отправлен пользователю.")
    await state.clear()
