from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from states import SellAppleStates
from keyboards.common import main_menu, confirm_menu
from keyboards.apple import apple_device_menu

sell_apple_router = Router()

# Кнопки выбора категории устройства Apple
apple_devices_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="Эпл Вотч"), types.KeyboardButton(text="Айфон")],
        [types.KeyboardButton(text="Мак"), types.KeyboardButton(text="Подсы")],
        [types.KeyboardButton(text="Айпад")]
    ],
    resize_keyboard=True
)

@sell_apple_router.message(lambda message: message.text == "Продать Apple")
async def sell_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите устройство, которое хотите продать:", reply_markup=apple_device_menu)
    await state.set_state(SellAppleStates.entering_device)

@sell_apple_router.message(SellAppleStates.entering_device)
async def enter_device_details(message: types.Message, state: FSMContext):
    device = message.text
    if device == "Подсы":
        await message.answer("Скупаем только оригинал.")
        return
    await state.update_data(device=device)
    await message.answer("Введите модель устройства:")
    await state.set_state(SellAppleStates.entering_model)

@sell_apple_router.message(SellAppleStates.entering_model)
async def enter_memory(message: types.Message, state: FSMContext):
    model = message.text
    await state.update_data(model=model)
    await message.answer("Введите объем памяти устройства:")
    await state.set_state(SellAppleStates.entering_memory)

@sell_apple_router.message(SellAppleStates.entering_memory)
async def enter_battery(message: types.Message, state: FSMContext):
    memory = message.text
    await state.update_data(memory=memory)
    await message.answer("Введите состояние аккумулятора (например, 85%):")
    await state.set_state(SellAppleStates.entering_battery)

@sell_apple_router.message(SellAppleStates.entering_battery)
async def attach_photo(message: types.Message, state: FSMContext):
    battery = message.text
    await state.update_data(battery=battery)
    await message.answer("Прикрепите фото устройства:")
    await state.set_state(SellAppleStates.attaching_photo)

@sell_apple_router.message(SellAppleStates.attaching_photo, content_types=types.ContentType.PHOTO)
async def enter_description(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)
    await message.answer("Опишите товар (есть ли дефекты, был ли в ремонте, комплектность и т. д.):")
    await state.set_state(SellAppleStates.entering_description)

@sell_apple_router.message(SellAppleStates.entering_description)
async def enter_price(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    await message.answer("Введите вашу цену за устройство:")
    await state.set_state(SellAppleStates.entering_price)

@sell_apple_router.message(SellAppleStates.entering_price)
async def enter_phone_number(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(price=price)
    await message.answer("Введите ваш номер телефона для связи или нажмите кнопку ниже:", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="Отправить номер телефона", request_contact=True)]],
        resize_keyboard=True
    ))
    await state.set_state(SellAppleStates.entering_phone)

@sell_apple_router.message(SellAppleStates.entering_phone, content_types=types.ContentType.CONTACT)
async def confirm_submission(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    data = await state.get_data()
    response = (f"Вы хотите продать {data['device']} {data['model']} {data['memory']} ГБ.\n"
                f"Состояние аккумулятора: {data['battery']}\n"
                f"Описание: {data['description']}\n"
                f"Цена: {data['price']}\n"
                f"Телефон: {phone_number}\n\n"
                f"Подтвердите или отмените заявку.")
    await state.update_data(phone_number=phone_number)
    await message.answer_photo(data['photo'], caption=response, reply_markup=confirm_menu)
    await state.set_state(SellAppleStates.confirming)

@sell_apple_router.message(SellAppleStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        data = await state.get_data()
        response = (f"Заявка принята! Данные переданы менеджеру:\n"
                    f"{data['device']} {data['model']} {data['memory']} ГБ\n"
                    f"Аккумулятор: {data['battery']}\n"
                    f"Цена: {data['price']}\n"
                    f"Телефон: {data['phone_number']}")
        # Здесь можно добавить отправку данных менеджеру
        await message.answer(response, reply_markup=main_menu)
    else:
        await message.answer("Вы отменили заявку.")
    await state.clear()
