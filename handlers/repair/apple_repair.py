from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states import RepairStates
from keyboards.apple import all_iphone_models
from keyboards.common import main_menu, share_phone_keyboard, confirm_menu
from config import ADMINS

apple_repair_router = Router()

@apple_repair_router.message(lambda message: message.text == "Apple⚙️")
async def repair_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите модель, которую хотите отремонтировать:", reply_markup=all_iphone_models)
    await state.set_state(RepairStates.choosing_model)

@apple_repair_router.message(RepairStates.choosing_model)
async def select_device(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await message.answer("Опишите дефект устройства:", reply_markup=types.ReplyKeyboardRemove)
    await state.set_state(RepairStates.entering_issue_description)

@apple_repair_router.message(RepairStates.entering_issue_description)
async def enter_issue_description(message: types.Message, state: FSMContext):
    await state.update_data(issue_description=message.text)
    await message.answer("Отправьте фото устройства с повреждением:")
    await state.set_state(RepairStates.attaching_photos)

@apple_repair_router.message(RepairStates.attaching_photos)
async def upload_photo(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.answer("Пожалуйста, отправьте фото устройства.")
        return
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Введите ваш номер телефона или нажмите кнопку ниже:", reply_markup=share_phone_keyboard)
    await state.set_state(RepairStates.entering_phone)

@apple_repair_router.message(RepairStates.entering_phone, lambda message: message.contact)
async def confirm_repair(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()

    response = (
        f"📌 Ваша заявка на ремонт:\n\n"
        f"📱 Устройство: {data['model']}\n"
        f"⚠️ Проблема: {data['issue_description']}\n"
        f"📞 Контакт: {phone_number}\n\n"
        "Подтвердите или отмените заявку."
    )

    await message.answer_photo(photo=data['photo'], caption=response, reply_markup=confirm_menu)
    await state.set_state(RepairStates.confirming)

@apple_repair_router.message(RepairStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        data = await state.get_data()
        user_id = message.from_user.id

        response_admin = (
            f"🔧 Новая заявка на ремонт( Apple ):\n\n"
            f"📱 Устройство: {data['model']}\n"
            f"⚠️ Проблема: {data['issue_description']}\n"
            f"📞 Контакт: {data['phone_number']}"
        )

        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [types.InlineKeyboardButton(text="Ответить пользователю", callback_data=f"admin_reply:{user_id}")]
            ]
        )

        try:
            for admin_id in ADMINS:
                await message.bot.send_photo(chat_id=admin_id, photo=data['photo'], caption=response_admin, reply_markup=keyboard)

            await message.answer("Заявка отправлена! В ближайшее время с вами свяжется менеджер.", reply_markup=main_menu)
        except:
            await message.answer("Ошибка при отправке сообщения администратору. Попробуйте позже.")
    else:
        await message.answer("Вы отменили заявку.", reply_markup=main_menu)

    await state.clear()
