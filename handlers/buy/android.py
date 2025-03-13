from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states import BuyAndroidStates
from keyboards.android import buy_android_menu

android_buy_router = Router()

# --------------------------ANDROID--------------------------------------

@android_buy_router.message(lambda message: message.text == "Android")
async def buy_android(message: types.Message, state: FSMContext):
    await message.answer("Из нового только Samsung (модели 23-25). Выберите марку телефона:", reply_markup=buy_android_menu)
    await state.set_state(BuyAndroidStates.choosing_brand)

@android_buy_router.message(BuyAndroidStates.choosing_brand)
async def enter_android_budget(message: types.Message, state: FSMContext):
    brand = message.text
    await state.update_data(brand=brand)
    await message.answer("Введите ваш бюджет:")
    await state.set_state(BuyAndroidStates.entering_budget)

@android_buy_router.message(BuyAndroidStates.entering_budget)
async def awaiting_admin_response(message: types.Message, state: FSMContext):
    budget = message.text
    await state.update_data(budget=budget)
    await message.answer("Менеджер свяжется с вами с предложением. Введите ваш номер телефона:")
    await state.set_state(BuyAndroidStates.awaiting_admin_response)

@android_buy_router.message(BuyAndroidStates.awaiting_admin_response)
async def confirm_android_buy(message: types.Message, state: FSMContext):
    data = await state.get_data()
    response = (f"Вы хотите купить Android {data['brand']} с бюджетом {data['budget']}.\n"
                f"Номер для связи: {message.text}\n\nМенеджер свяжется с вами.")
    await message.answer(response)
    await state.clear()

@android_buy_router.message(lambda message: message.text == "Dyson")
async def buy_dyson(message: types.Message, state: FSMContext):
    await message.answer("Мы продаем только Dyson. Для покупки, пожалуйста, напишите вашему менеджеру.")
    await state.clear()
