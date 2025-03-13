from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from states import BuyAppleStates, BuyAndroidStates
from keyboards import buy_menu, buy_apple_menu, condition_menu, iphone_models, memory_menu, color_menu, confirm_menu

router = Router()

@router.message(lambda message: message.text == "Купить")
async def start_buy(message: types.Message):
    await message.answer("Выберите категорию устройства:", reply_markup=buy_menu)

@router.message(lambda message: message.text == "Apple")
async def buy_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите устройство, которое хотите купить:", reply_markup=buy_apple_menu)

@router.message(lambda message: message.text in ["Айфон", "Эпл Вотч", "Подсы", "Мак", "Айпад"])
async def choose_condition(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(category=category)
    await message.answer("Выберите состояние устройства:", reply_markup=condition_menu)

@router.message(lambda message: message.text in ["Новое", "БУ", "Подобрать"])
async def process_condition(message: types.Message, state: FSMContext):
    condition = message.text
    data = await state.get_data()
    category = data['category']
    
    if condition == "Подобрать":
        await message.answer("Заполните анкету для подбора устройства.")
        await state.set_state(BuyAppleStates.entering_phone)
        return
    
    if category == "Айфон":
        if condition == "Новое":
            await message.answer("Выберите модель iPhone (13-16):", reply_markup=iphone_models)
            await state.set_state(BuyAppleStates.choosing_model)
        elif condition == "БУ":
            await message.answer("Переходим в канал с бу телефонами.")
            # Здесь нужно добавить логику для перехода в канал с бу телефонами
            await state.clear()

@router.message(BuyAppleStates.choosing_model)
async def choose_iphone_memory(message: types.Message, state: FSMContext):
    model = message.text
    await state.update_data(model=model)
    await message.answer("Выберите объем памяти:", reply_markup=memory_menu)
    await state.set_state(BuyAppleStates.choosing_memory)

@router.message(BuyAppleStates.choosing_memory)
async def choose_iphone_color(message: types.Message, state: FSMContext):
    memory = message.text
    await state.update_data(memory=memory)
    await message.answer("Выберите цвет:", reply_markup=color_menu)
    await state.set_state(BuyAppleStates.choosing_color)

@router.message(BuyAppleStates.choosing_color)
async def enter_phone_number(message: types.Message, state: FSMContext):
    color = message.text
    await state.update_data(color=color)
    await message.answer("Введите ваш номер телефона для связи:", reply_markup=confirm_menu)
    await state.set_state(BuyAppleStates.entering_phone)

@router.message(BuyAppleStates.entering_phone)
async def confirm_buy(message: types.Message, state: FSMContext):
    data = await state.get_data()
    response = (f"Вы хотите купить: {data['category']} {data['model']} {data['memory']} ГБ {data['color']}\n"
                f"Номер для связи: {message.text}\n\nМенеджер свяжется с вами.")
    await message.answer(response)
    await state.clear()

@router.message(lambda message: message.text == "Android")
async def buy_android(message: types.Message, state: FSMContext):
    await message.answer("Из нового только Samsung (модели 23-25). Выберите марку телефона:", reply_markup=buy_apple_menu)
    await state.set_state(BuyAndroidStates.choosing_brand)

@router.message(BuyAndroidStates.choosing_brand)
async def enter_android_budget(message: types.Message, state: FSMContext):
    brand = message.text
    await state.update_data(brand=brand)
    await message.answer("Введите ваш бюджет:")
    await state.set_state(BuyAndroidStates.entering_budget)

@router.message(BuyAndroidStates.entering_budget)
async def awaiting_admin_response(message: types.Message, state: FSMContext):
    budget = message.text
    await state.update_data(budget=budget)
    await message.answer("Менеджер свяжется с вами с предложением. Введите ваш номер телефона:")
    await state.set_state(BuyAndroidStates.awaiting_admin_response)

@router.message(BuyAndroidStates.awaiting_admin_response)
async def confirm_android_buy(message: types.Message, state: FSMContext):
    data = await state.get_data()
    response = (f"Вы хотите купить Android {data['brand']} с бюджетом {data['budget']}.\n"
                f"Номер для связи: {message.text}\n\nМенеджер свяжется с вами.")
    await message.answer(response)
    await state.clear()

@router.message(lambda message: message.text == "Dyson")
async def buy_dyson(message: types.Message, state: FSMContext):
    await message.answer("Мы продаем только Dyson. Для покупки, пожалуйста, напишите вашему менеджеру.")
    await state.clear()

