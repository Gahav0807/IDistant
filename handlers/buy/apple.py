from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states import BuyAppleStates
from keyboards.apple import apple_device_menu, iphone_models
from keyboards.common import condition_menu, while_512_memory_menu, all_memory_menu, color_menu, confirm_menu, share_phone_keyboard, main_menu

apple_buy_router = Router()

# ---------------------------APPLE------------------------------------------

@apple_buy_router.message(lambda message: message.text == "Apple")
async def buy_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите устройство, которое хотите купить:", reply_markup=apple_device_menu)

@apple_buy_router.message(lambda message: message.text in ["Айфон", "Эпл Вотч", "Подсы", "Мак", "Айпад"])
async def choose_condition(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(category=category)
    await message.answer("Выберите состояние устройства:", reply_markup=condition_menu)

@apple_buy_router.message(lambda message: message.text in ["Новое", "БУ", "Подобрать"])
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

@apple_buy_router.message(BuyAppleStates.choosing_model)
async def choose_iphone_memory(message: types.Message, state: FSMContext):
    model = message.text
    await state.update_data(model=model)

    # Проверяем, содержит ли модель "Pro" или "Plus"
    if "Pro" in model or "Plus" in model:
        memory_menu = all_memory_menu
    else:
        memory_menu = while_512_memory_menu

    await message.answer("Выберите объем памяти:", reply_markup=memory_menu)
    await state.set_state(BuyAppleStates.choosing_memory)

@apple_buy_router.message(BuyAppleStates.choosing_memory)
async def choose_iphone_color(message: types.Message, state: FSMContext):
    memory = message.text
    await state.update_data(memory=memory)
    await message.answer("Выберите цвет:", reply_markup=color_menu)
    await state.set_state(BuyAppleStates.choosing_color)

@apple_buy_router.message(BuyAppleStates.choosing_color)
async def enter_phone_number(message: types.Message, state: FSMContext):
    color = message.text
    await state.update_data(color=color)
    await message.answer("Введите ваш номер телефона для связи или нажмите кнопку ниже:", reply_markup=share_phone_keyboard)
    await state.set_state(BuyAppleStates.entering_phone)

@apple_buy_router.message(BuyAppleStates.entering_phone, lambda message: message.contact)
async def confirm_buy_contact(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    data = await state.get_data()
    response = (f"Вы хотите купить: {data['category']} {data['model']} {data['memory']} ГБ {data['color']}\n"
                f"Номер для связи: {phone_number}\n\n"
                f"Подтвердите или отмените заявку.")
    await state.update_data(phone_number=phone_number)
    await message.answer(response, reply_markup=confirm_menu)
    await state.set_state(BuyAppleStates.confirming)

@apple_buy_router.message(BuyAppleStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        data = await state.get_data()
        response = (f"Заявка подтверждена!\n"
                    f"Данные переданы менеджеру:\n"
                    f"{data['category']} \n{data['model']} \n{data['memory']} ГБ \n{data['color']}\n"
                    f"Телефон: {data['phone_number']}")
        # Здесь можно добавить отправку данных менеджеру
        await message.answer(response, reply_markup=main_menu)
    else:
        await message.answer("Вы отменили заявку.")
    await state.clear()
