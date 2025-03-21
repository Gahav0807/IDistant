from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states import SellAppleStates
from keyboards.apple import apple_device_menu
from keyboards.common import main_menu, share_phone_keyboard, confirm_menu
from config import ADMINS

apple_sell_router = Router()

@apple_sell_router.message(lambda message: message.text == "Apple💸")
async def sell_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите устройство, которое хотите продать:", reply_markup=apple_device_menu)
    await state.set_state(SellAppleStates.entering_device)

@apple_sell_router.message(SellAppleStates.entering_device)
async def select_device(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(category=category)

    if category.lower() == "airpods":
        await message.answer("Мы скупаем только оригинальные AirPods")
    await message.answer("Введите модель устройства:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(SellAppleStates.entering_model)

@apple_sell_router.message(SellAppleStates.entering_model)
async def enter_model(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await message.answer("Введите объем встроенной памяти и оперативную память (например, 512/16):")
    await state.set_state(SellAppleStates.entering_memory)

@apple_sell_router.message(SellAppleStates.entering_memory)
async def enter_memory(message: types.Message, state: FSMContext):
    await state.update_data(memory=message.text)
    await message.answer("Введите состояние аккумулятора в %:")
    await state.set_state(SellAppleStates.entering_battery)

@apple_sell_router.message(SellAppleStates.entering_battery)
async def enter_battery(message: types.Message, state: FSMContext):
    await state.update_data(battery=message.text)
    await message.answer("Прикрепите фото устройства:")
    await state.set_state(SellAppleStates.attaching_photos)

@apple_sell_router.message(SellAppleStates.attaching_photos)
async def upload_photo(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.answer("Пожалуйста, отправьте фото устройства.")
        return
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Опишите товар (есть ли дефекты, был ли в ремонте, комплект и т.д.):")
    await state.set_state(SellAppleStates.entering_description)

@apple_sell_router.message(SellAppleStates.entering_description)
async def enter_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите желаемую цену:")
    await state.set_state(SellAppleStates.entering_price)

@apple_sell_router.message(SellAppleStates.entering_price)
async def enter_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Введите ваш номер телефона или нажмите кнопку ниже:", reply_markup=share_phone_keyboard)
    await state.set_state(SellAppleStates.entering_phone)

@apple_sell_router.message(SellAppleStates.entering_phone, lambda message: message.contact)
async def confirm_sale(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()

    response = (
        f"Вы хотите продать:\n\n"
        f"📱 Устройство: {data['category']}\n"
        f"🔹 Модель: {data['model']} ({data.get('memory', '—')})\n"
        f"🔋 Состояние АКБ: {data.get('battery', '—')}%\n"
        f"ℹ️ Описание: {data['description']}\n"
        f"💰 Цена: {data['price']}\n"
        f"📞 Контакт: {phone_number}\n\n"
        "Подтвердите или отмените заявку."
    )

    await message.answer_photo(photo=data['photo'], caption=response, reply_markup=confirm_menu)
    await state.set_state(SellAppleStates.confirming)

@apple_sell_router.message(SellAppleStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        data = await state.get_data()
        user_id = message.from_user.id

        response_admin = (
            f"🔔 Новая заявка на продажу( Apple ):\n\n"
            f"📱 Устройство: {data['category']}\n"
            f"🔹 Модель: {data['model']} ({data.get('memory', '—')})\n"
            f"🔋 Состояние АКБ: {data.get('battery', '—')}%\n"
            f"ℹ️ Описание: {data['description']}\n"
            f"💰 Цена: {data['price']}\n"
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
