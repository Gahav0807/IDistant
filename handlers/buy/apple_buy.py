from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states import BuyAppleStates
from keyboards.apple import *
from keyboards.common import (
    condition_menu, while_512_memory_menu, all_memory_menu, color_menu,
    confirm_menu, share_phone_keyboard, main_menu, to_main_menu
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS

apple_buy_router = Router()

# --------------------------- APPLE ------------------------------------------

@apple_buy_router.message(lambda message: message.text == "Apple🍎")
async def buy_apple(message: types.Message, state: FSMContext):
    """Начало процесса покупки устройства Apple."""
    await message.answer("Выберите устройство, которое хотите купить:", reply_markup=apple_device_menu)
    await state.set_state(BuyAppleStates.choosing_device)


@apple_buy_router.message(BuyAppleStates.choosing_device)
async def choose_condition(message: types.Message, state: FSMContext):
    """Обработка выбора устройства."""
    category = message.text
    await state.update_data(category=category)

    if category.lower() == "другое":
        await message.answer("Если в списке нет предпочитаемого варианта, свяжитесь с нашим менеджером, мы подберем товар специально для вас;\nНаш менеджер: ", reply_markup=air_pods_ways)

    if category.lower() == "airpods":
        await message.answer("Выберите вид AirPods:", reply_markup=air_pods_ways)
        await state.set_state(BuyAppleStates.choosing_airpods_way)
        return
    
    if category.lower() == "macbook":
        await message.answer("Выберите процессор:", reply_markup=macbook_cpu)
        await state.set_state(BuyAppleStates.choosing_macbook_cpu)
        return
    
    await message.answer("Выберите состояние устройства:", reply_markup=condition_menu)
    await state.set_state(BuyAppleStates.way_to_buy)

@apple_buy_router.message(BuyAppleStates.choosing_macbook_cpu)
async def choose_macbook_cpu(message: types.Message, state: FSMContext):
    cpu = message.text
    await state.update_data(macbook_cpu=cpu)

    if cpu.lower() == "m1":
        await message.answer("Выберите модель:", reply_markup=macbook_m1_models)
    elif cpu.lower() == "m2":
        await message.answer("Выберите модель:", reply_markup=macbook_m2_models)
    elif cpu.lower() == "m3":
        await message.answer("Выберите модель:", reply_markup=macbook_m3_models)

    await state.set_state(BuyAppleStates.choosing_model)

@apple_buy_router.message(BuyAppleStates.choosing_airpods_way)
async def choose_airpods_way(message: types.Message, state: FSMContext):
    """Обработка выбора типа AirPods (оригинал/копия)."""
    way = message.text
    await state.update_data(airpods_way=way)
    await message.answer("Выберите модель:", reply_markup=air_pods_models)
    await state.set_state(BuyAppleStates.choosing_model)


@apple_buy_router.message(BuyAppleStates.way_to_buy)
async def process_condition(message: types.Message, state: FSMContext):
    """Обработка выбора состояния устройства."""
    condition = message.text
    data = await state.get_data()
    category = data['category']
    await state.update_data(condition=condition)
    
    if condition == "Подобрать":
        await message.answer("Введите ваш бюджет:", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(BuyAppleStates.pick_up_by_value)
        return
    
    if condition == "БУ":
        await message.answer("Наш канал с БУ")
        return
    
    if category.lower() == "iphone" and condition == "Новое":
        await message.answer("Выберите модель iPhone (13-16):", reply_markup=iphone_models)
        await state.set_state(BuyAppleStates.choosing_model)
        return
    
    if category.lower() == "apple watch" and condition == "Новое":
        await message.answer("Выберите модель Apple Watch:", reply_markup=apple_watch_models)
        await state.set_state(BuyAppleStates.choosing_model)
        return
        
    if category.lower() == "ipad" and condition == "Новое":
        await message.answer("Выберите модель iPad:", reply_markup=ipad_models)
        await state.set_state(BuyAppleStates.choosing_model)
        return


@apple_buy_router.message(BuyAppleStates.pick_up_by_value)
async def pick_up_value(message: types.Message, state: FSMContext):
    """Обработка ввода бюджета для подбора устройства."""
    value = message.text
    await state.update_data(pick_up_by_value=value)
    await message.answer("Введите ваш номер телефона для связи или нажмите кнопку ниже:", reply_markup=share_phone_keyboard)
    await state.set_state(BuyAppleStates.entering_phone)


@apple_buy_router.message(BuyAppleStates.choosing_model)
async def choose_model(message: types.Message, state: FSMContext):
    """Обработка выбора модели устройства."""
    model = message.text
    await state.update_data(model=model)
    data = await state.get_data()
    category = data['category'].lower()

    if category == "iphone":
        memory_menu = all_memory_menu if "Pro" in model or "Plus" in model else while_512_memory_menu
        await message.answer("Выберите объем памяти:", reply_markup=memory_menu)
        await state.set_state(BuyAppleStates.choosing_memory)

    elif category == "apple watch":
        if "SE(1 поколения)" in model:
            await message.answer("Выберите размер часов:", reply_markup=apple_watch_se1_size)
        elif "SE(2 поколения)" in model:
            await message.answer("Выберите размер часов:", reply_markup=apple_watch_se2_size)
        elif "10" in model: # Apple Watch Series 10
            await message.answer("Выберите размер часов:", reply_markup=apple_watch_10_size)
        else: # Apple Watch Series 8, 9 
            await message.answer("Выберите размер часов:", reply_markup=apple_watch_simple_size)

        await state.set_state(BuyAppleStates.choosing_size)

    elif category == "airpods":
        airpods_prices = {
            "airpods 2": 990,
            "airpods 3": 1990,
            "airpods 4": 1990,
            "airpods pro": 1420,
            "airpods pro 2": 1990,
        }
        value = airpods_prices.get(model.lower(), 0)
        await state.update_data(value_of_airpods=value)
        await message.answer("Введите свой номер связи:", reply_markup=share_phone_keyboard)
        await state.set_state(BuyAppleStates.entering_phone)

    elif category == "ipad":
        memory_menus = {
            "ipad air (5)": ipad_air_5_memory,
            "ipad pro 12,9 (6)": ipad_pro_12_9_6_memory,
            "ipad pro 11 (5)": ipad_pro_11_5_memory,
        }
        memory_menu = memory_menus.get(model.lower())
        await message.answer("Выберите объем памяти:", reply_markup=memory_menu)
        await state.set_state(BuyAppleStates.choosing_memory)
    
    elif category == "macbook":
        await message.answer("Выберите объем памяти:", reply_markup=macbook_memory)
        await state.set_state(BuyAppleStates.choosing_memory)


@apple_buy_router.message(BuyAppleStates.choosing_size)
async def choose_size(message: types.Message, state: FSMContext):
    """Обработка выбора размера Apple Watch."""
    size = message.text
    await state.update_data(size=size)
    await message.answer("Выберите цвет:", reply_markup=apple_watch_color)
    await state.set_state(BuyAppleStates.choosing_color)


@apple_buy_router.message(BuyAppleStates.choosing_memory)
async def choose_memory(message: types.Message, state: FSMContext):
    """Обработка выбора объема памяти."""
    memory = message.text
    await state.update_data(memory=memory)
    data = await state.get_data()
    category = data['category'].lower()

    if category == "macbook":
        await message.answer("Поделитесь вашим номером телефона: ", reply_markup=share_phone_keyboard)
        await state.set_state(BuyAppleStates.entering_phone)

    elif category == "ipad":
        if data['model'].lower() == "ipad air (5)":
            await message.answer("Поделитесь вашим номером телефона:", reply_markup=share_phone_keyboard)
            await state.set_state(BuyAppleStates.entering_phone)
        else:
            access_memory = ipad_pro_12_9_6_access_memory if data['model'].lower() == "ipad pro 12,9 (6)" else ipad_pro_11_5_access_memory
            await message.answer("Выберите объем оперативной памяти:", reply_markup=access_memory)
            await state.set_state(BuyAppleStates.choosing_access_memory)
    else:
        await message.answer("Выберите цвет:", reply_markup=color_menu)
        await state.set_state(BuyAppleStates.choosing_color)


@apple_buy_router.message(BuyAppleStates.choosing_access_memory)
async def choose_access_memory(message: types.Message, state: FSMContext):
    """Обработка выбора оперативной памяти для iPad."""
    access_memory = message.text
    await state.update_data(access_memory=access_memory)
    await message.answer("Поделитесь вашим номером телефона: ", reply_markup=share_phone_keyboard)
    await state.set_state(BuyAppleStates.entering_phone)


@apple_buy_router.message(BuyAppleStates.choosing_color)
async def choose_color(message: types.Message, state: FSMContext):
    """Обработка выбора цвета устройства."""
    color = message.text
    await state.update_data(color=color)
    await message.answer("Поделитесь вашим номером телефона: ", reply_markup=share_phone_keyboard)
    await state.set_state(BuyAppleStates.entering_phone)


@apple_buy_router.message(BuyAppleStates.entering_phone, lambda message: message.contact)
async def confirm_buy_contact(message: types.Message, state: FSMContext):
    """Обработка ввода номера телефона через контакт."""
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    await confirm_order(message, state)


async def confirm_order(message: types.Message, state: FSMContext):
    """Подтверждение заказа с добавлением смайликов."""
    data = await state.get_data()
    category = data['category'].lower()
    condition = data.get('condition', '').lower()
    phone_number = data['phone_number']

    # Базовые смайлики для всех сообщений
    confirm_text = "\n\n✅ Подтвердите или ❌ отмените заявку."
    contact_text = f"\n📞 Контакт: +{phone_number}"

    if condition == 'подобрать':
        response = (
            f"🔍 Вы хотите подобрать: {data['category']}\n"
            f"💰 Бюджет: {data['pick_up_by_value']} руб."
            f"{contact_text}"
            f"{confirm_text}"
        )
    else:
        device_emojis = {
            'macbook': '💻',
            'iphone': '📱',
            'apple watch': '⌚',
            'ipad': '📲',
            'airpods': '🎧'
        }
        emoji = device_emojis.get(category, '📦')
        
        if category == 'macbook':
            response = (
                f"{emoji} Вы хотите купить: {data['model']} {data['macbook_cpu']} {data['memory']}\n"
                f"⚡ Процессор: {data['macbook_cpu']}\n"
                f"💾 Память: {data['memory']}"
                f"{contact_text}"
                f"{confirm_text}"
            )
        elif category == 'iphone':
            response = (
                f"{emoji} Вы хотите купить: {data['model']}\n"
                f"🎨 Цвет: {data['color']}\n"
                f"💾 Память: {data['memory']}"
                f"{contact_text}"
                f"{confirm_text}"
            )
        elif category == 'apple watch':
            response = (
                f"{emoji} Вы хотите купить: {data['model']}\n"
                f"📏 Размер: {data.get('size', 'не указан')}\n"
                f"🎨 Цвет: {data['color']}"
                f"{contact_text}"
                f"{confirm_text}"
            )
        elif category == 'ipad':
            response = (
                f"{emoji} Вы хотите купить: {data['model']}\n"
                f"💾 Память: {data['memory']}\n"
                f"⚡ RAM: {data.get('access_memory', 'не указано')}"
                f"{contact_text}"
                f"{confirm_text}"
            )
        elif category == 'airpods':
            if data.get('airpods_way', '').lower() == 'копия':
                response = (
                    f"{emoji} Вы хотите купить: {data['model']} (Копия)\n"
                    f"💲 Цена: {data['value_of_airpods']} руб."
                    f"{contact_text}"
                    f"{confirm_text}"
                )
            else:
                response = (
                    f"{emoji} Вы хотите купить: {data['model']} (Оригинал)"
                    f"{contact_text}"
                    f"{confirm_text}"
                )

    await message.answer(response, reply_markup=confirm_menu)
    await state.set_state(BuyAppleStates.confirming)


@apple_buy_router.message(BuyAppleStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    """Обработка подтверждения заказа."""
    if message.text == "Подтвердить":
        data = await state.get_data()
        user_id = message.from_user.id
        category = data['category']
        condition = data.get('condition', '').lower()

        response_admin = f"🔔 Новая заявка на продажу (Apple, {category}):\n\n"
        if condition == 'подобрать':
            response_admin += (
                f"Пользователь желает подобрать девайс!\n\n"
                f"📱 Категория: {data['category']}\n"
                f"💸 Бюджет: {data['pick_up_by_value']}\n"
                f"📞 Контакт: +{data['phone_number']}\n"
            )
        else:
            if category.lower() == 'macbook':
                response_admin += (
                    f"💻 Модель: {data['model']} {data['macbook_cpu']} {data['memory']} \n"
                    f"📞 Контакт: +{data['phone_number']}\n\n"
                )

            if category.lower() == 'iphone':
                response_admin += (
                    f"📱 Модель: {data['model']} {data['memory']} {data['color']}\n"
                    f"📞 Контакт: +{data['phone_number']}\n"
                )
            elif category.lower() == 'apple watch':
                response_admin += (
                    f"⌚ Модель: {data['model']} {data['color']}\n"
                    f"📞 Контакт: +{data['phone_number']}\n"
                )
            elif category.lower() == 'ipad':
                response_admin += (
                    f"📱 Модель: {data['model']} {data['memory']} {data.get('access_memory', '')}\n"
                    f"📞 Контакт: +{data['phone_number']}\n"
                )
            elif category.lower() == 'airpods':
                if data.get('airpods_way', '').lower() == 'копия':
                    response_admin += (
                        f"🎧 Модель: {data['model']}\n"
                        f"💸 Цена: {data['value_of_airpods']} руб.\n"
                        f"📞 Контакт: +{data['phone_number']}\n"
                    )
                else:
                    response_admin += (
                        f"🎧 Модель: {data['model']}\n"
                        f"📞 Контакт: +{data['phone_number']}\n"
                    )

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="Ответить пользователю", callback_data=f"admin_reply:{user_id}")
            ]]
        )

        try:
            for admin_id in ADMINS:
                await message.bot.send_message(chat_id=admin_id, text=response_admin, reply_markup=keyboard)

            await message.answer("Заявка отправлена! Ожидайте ответа менеджера.", reply_markup=main_menu)
        except:
            await message.answer("Ошибка при отправке сообщения администратору. Попробуйте позже.")
    else:
        await message.answer("Вы отменили заявку.", reply_markup=main_menu)

    await state.clear()