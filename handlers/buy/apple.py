from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states import BuyAppleStates
from keyboards.apple import apple_device_menu, iphone_models, apple_watch_models, apple_watch_simple_size, apple_watch_se1_size, apple_watch_se2_size, apple_watch_color
from keyboards.common import condition_menu, while_512_memory_menu, all_memory_menu, color_menu, confirm_menu, share_phone_keyboard, main_menu

apple_buy_router = Router()

# ---------------------------APPLE------------------------------------------

@apple_buy_router.message(lambda message: message.text == "Apple")
async def buy_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите устройство, которое хотите купить:", reply_markup=apple_device_menu)

@apple_buy_router.message(lambda message: message.text in ["IPhone", "Apple Watch", "AirPods", "Mac", "IPad"])
async def choose_condition(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(category=category)
    await message.answer("Выберите состояние устройства:", reply_markup=condition_menu)

@apple_buy_router.message(lambda message: message.text in ["Новое", "БУ", "Подобрать"])
async def process_condition(message: types.Message, state: FSMContext):
    condition = message.text
    data = await state.get_data()
    category = data['category']
    await state.update_data(condition=condition)
    
    if condition == "Подобрать":
        await message.answer("Введите ваш бюджет")
        await state.set_state(BuyAppleStates.pick_up_by_value)
        return
    
    if condition == "БУ":
        await message.answer("Наш канал с БУ")
        return
    
    if category.lower() == "iphone":
        if condition == "Новое":
            await message.answer("Выберите модель iPhone (13-16):", reply_markup=iphone_models)
            await state.set_state(BuyAppleStates.choosing_model)
            return
    
    if category.lower() == "apple watch":
        if condition == "Новое":
            await message.answer("Выберите модель Эпл вотч:", reply_markup=apple_watch_models)
            await state.set_state(BuyAppleStates.choosing_model)
            return

@apple_buy_router.message(BuyAppleStates.pick_up_by_value)
async def pick_up_value(message: types.Message, state: FSMContext):
    value = message.text
    await state.update_data(pick_up_by_value=value)

    await message.answer("Введите ваш номер телефона для связи или нажмите кнопку ниже:", reply_markup=share_phone_keyboard)
    await state.set_state(BuyAppleStates.entering_phone)

@apple_buy_router.message(BuyAppleStates.choosing_model)
async def choose_model(message: types.Message, state: FSMContext):
    model = message.text
    await state.update_data(model=model)

    data = await state.get_data()
    category = data['category']

    if category.lower() == "iphone":
        # Проверяем, содержит ли модель "Pro" или "Plus"
        if "Pro" in model or "Plus" in model:
            memory_menu = all_memory_menu
        else:
            memory_menu = while_512_memory_menu

        await message.answer("Выберите объем памяти:", reply_markup=memory_menu)
        await state.set_state(BuyAppleStates.choosing_memory)

    elif category.lower() == "apple watch":
        if "SE(1 поколения)" in model:
            await message.answer("Выберите размер часов:", reply_markup=apple_watch_se1_size)
            await state.set_state(BuyAppleStates.choosing_size)
        elif "SE(2 поколения)" in model:
            await message.answer("Выберите размер часов:", reply_markup=apple_watch_se2_size)
            await state.set_state(BuyAppleStates.choosing_size)
        else:
            await message.answer("Выберите размер часов:", reply_markup=apple_watch_simple_size)
            await state.set_state(BuyAppleStates.choosing_size)

@apple_buy_router.message(BuyAppleStates.choosing_size)
async def choose_size(message: types.Message, state: FSMContext):
    size = message.text
    await state.update_data(size=size)
    await message.answer("Выберите цвет:", reply_markup=apple_watch_color)
    await state.set_state(BuyAppleStates.choosing_color)

@apple_buy_router.message(BuyAppleStates.choosing_memory)
async def choose_color(message: types.Message, state: FSMContext):
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
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    condition = data['condition'].lower()
    category = data['category'].lower()

    if condition == 'подобрать':
        await state.update_data(phone_number=message.contact.phone_number)
        response = (f"Вы хотите подобрать: {data['category']}\n"
                f"Бюджет: {data['pick_up_by_value']}\n"
                f"Номер для связи: {phone_number}\n\n"
                f"Подтвердите или отмените заявку.")
        await message.answer(response, reply_markup=confirm_menu)
        await state.set_state(BuyAppleStates.confirming)
        return
    else:
        if category.lower() == 'apple watch':
            response = (f"Вы хотите купить: {data['category']} {data['model']} {data['color']}\n"
                        f"Номер для связи: {phone_number}\n\n"
                        f"Подтвердите или отмените заявку.")
            await message.answer(response, reply_markup=confirm_menu)
            await state.set_state(BuyAppleStates.confirming)
        else:
            response = (f"Вы хотите купить: {data['model']} {data['memory']} {data['color']}\n"
                        f"Номер для связи: {phone_number}\n\n"
                        f"Подтвердите или отмените заявку.")
            await message.answer(response, reply_markup=confirm_menu)
            await state.set_state(BuyAppleStates.confirming)

@apple_buy_router.message(BuyAppleStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    data = await state.get_data()
    condition = data['condition'].lower()
    category = data['category'].lower()

    if message.text == "Подтвердить":
        if condition == 'подобрать': 
            await message.answer("Готово! Ожидайте обратной связи от администратора", reply_markup=main_menu)
            return

        if category.lower() == 'apple watch':
            response = (f"Заявка подтверждена!\n"
                        f"Данные переданы менеджеру:\n"
                        f"{data['category']} \n{data['model']} \n{data['color']}\n"
                        f"Телефон: {data['phone_number']}")
        else:
            response = (f"Заявка подтверждена!\n"
                        f"Данные переданы менеджеру:\n"
                        f"{data['category']} \n{data['model']} \n{data['memory']} \n{data['color']}\n"
                        f"Телефон: {data['phone_number']}")

        # Здесь можно добавить отправку данных менеджеру
        await message.answer(response, reply_markup=main_menu)
    else:
        await message.answer("Вы отменили заявку.")
    
    await state.clear()
