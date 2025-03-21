from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from states import BuyAndroidStates
from keyboards.android import buy_android_menu
from keyboards.common import confirm_menu, main_menu, share_phone_keyboard
from config import ADMINS

android_buy_router = Router()

# --------------------------ANDROID--------------------------------------

@android_buy_router.message(lambda message: message.text == "Android🤖")
async def buy_android(message: types.Message, state: FSMContext):
    await message.answer("Выберите марку телефона:", reply_markup=buy_android_menu)
    await state.set_state(BuyAndroidStates.choosing_brand)

@android_buy_router.message(BuyAndroidStates.choosing_brand)
async def enter_android_budget(message: types.Message, state: FSMContext):
    brand = message.text
    await state.update_data(brand=brand)
    await message.answer("Введите ваш бюджет:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(BuyAndroidStates.entering_budget)

@android_buy_router.message(BuyAndroidStates.entering_budget)
async def awaiting_admin_response(message: types.Message, state: FSMContext):
    budget = message.text
    await state.update_data(budget=budget)
    await message.answer("Введите ваш номер телефона:", reply_markup=share_phone_keyboard)
    await state.set_state(BuyAndroidStates.entering_phone)

@android_buy_router.message(BuyAndroidStates.entering_phone, lambda message: message.contact)
async def confirm_sale(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    
    response = (f"Вы хотите купить:\n\n"
                f"Android {data['brand']}.\n"
                f"Бюджет {data['budget']}.\n"
                f"Номер для связи: {phone_number}\n\n"
                "Подтвердите или отмените заявку."
                )
    
    await message.answer(response, reply_markup=confirm_menu)
    await state.set_state(BuyAndroidStates.confirming)

@android_buy_router.message(BuyAndroidStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        data = await state.get_data()
        user_id = message.from_user.id
        
        response_admin = (f"🔔 Новая заявка на продажу( Android ):\n\n"
                          f"📱 Модель: {data['brand']}\n"
                          f"💰 Цена: {data['budget']} руб.\n"
                          f"📞 Контакт: {data['phone_number']}")

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Ответить пользователю", callback_data=f"admin_reply:{user_id}")]
            ]
        )

        for admin_id in ADMINS:
            await message.bot.send_message(chat_id=admin_id, text=response_admin, reply_markup=keyboard)

        await message.answer("Заявка отправлена! Ожидайте ответа менеджера.", reply_markup=main_menu)
    else:
        await message.answer("Вы отменили заявку.", reply_markup=main_menu)

    await state.clear()