from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from states import SellAndroidStates
from keyboards.common import confirm_menu, main_menu, share_phone_keyboard
from config import ADMINS

android_sell_router = Router()

# --------------------------ANDROID--------------------------------------

@android_sell_router.message(lambda message: message.text == "Android💸")
async def buy_android(message: types.Message, state: FSMContext):
    await message.answer("Введите бренд & модель телефона:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(SellAndroidStates.entering_model)

@android_sell_router.message(SellAndroidStates.entering_model)
async def enter_android_budget(message: types.Message, state: FSMContext):
    await state.update_data(brand_and_model=message.text)
    await message.answer("Введите цену:")
    await state.set_state(SellAndroidStates.entering_price)

@android_sell_router.message(SellAndroidStates.entering_price)
async def enter_battery(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Прикрепите фото устройства:")
    await state.set_state(SellAndroidStates.attaching_photos)

@android_sell_router.message(SellAndroidStates.attaching_photos)
async def upload_photo(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.answer("Пожалуйста, отправьте фото устройства.")
        return
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Опишите товар (есть ли дефекты, был ли в ремонте, комплект и т.д.):")
    await state.set_state(SellAndroidStates.entering_description)

@android_sell_router.message(SellAndroidStates.entering_description)
async def awaiting_admin_response(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите ваш номер телефона:", reply_markup=share_phone_keyboard)
    await state.set_state(SellAndroidStates.entering_phone)

@android_sell_router.message(SellAndroidStates.entering_phone, lambda message: message.contact)
async def confirm_sale(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()

    response = (f"Вы хотите продать:\n\n"
                f"📱 Модель: {data['brand_and_model']}\n"
                f"💰 Цена: {data['price']} руб.\n"
                f"ℹ️ Описание: {data['description']}\n"
                f"📞 Контакт: {phone_number}\n\n"
                "Подтвердите или отмените заявку.")

    await message.answer_photo(photo=data['photo'], caption=response, reply_markup=confirm_menu)
    await state.set_state(SellAndroidStates.confirming)

@android_sell_router.message(SellAndroidStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        data = await state.get_data()
        user_id = message.from_user.id
        
        response_admin = (f"🔔 Новая заявка на продажу( Android ):\n\n"
                          f"📱 Модель: {data['brand_and_model']}\n"
                          f"💰 Цена: {data['price']} руб.\n"
                          f"ℹ️ Описание: {data['description']}\n"
                          f"📞 Контакт: {data['phone_number']}")

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Ответить пользователю", callback_data=f"admin_reply:{user_id}")]
            ]
        )

        for admin_id in ADMINS:
            await message.bot.send_photo(chat_id=admin_id, photo=data['photo'], caption=response_admin, reply_markup=keyboard)

        await message.answer("Заявка отправлена! Ожидайте ответа менеджера.", reply_markup=main_menu)
    else:
        await message.answer("Вы отменили заявку.", reply_markup=main_menu)

    await state.clear()