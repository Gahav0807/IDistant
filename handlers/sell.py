from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from states import SellAppleStates, SellAndroidStates
from keyboards import sell_menu, apple_sell_menu

router = Router()

@router.message(Command("sell"))
async def start_sell(message: types.Message):
    await message.answer("Выберите категорию устройства:", reply_markup=sell_menu)

@router.message(lambda message: message.text == "Apple")
async def sell_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите устройство, которое хотите продать:", reply_markup=apple_sell_menu)

@router.message(lambda message: message.text in ["Айфон", "Эпл Вотч", "Мак", "Подсы", "Айпад"])
async def enter_model(message: types.Message, state: FSMContext):
    category = message.text
    if category == "Подсы":
        await message.answer("Скупаем только оригинальные наушники")
        return
    
    await state.update_data(category=category)
    await message.answer("Введите модель устройства:")
    await state.set_state(SellAppleStates.entering_model)

@router.message(SellAppleStates.entering_model)
async def enter_memory(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await message.answer("Введите объем памяти:")
    await state.set_state(SellAppleStates.entering_memory)

@router.message(SellAppleStates.entering_memory)
async def enter_battery(message: types.Message, state: FSMContext):
    await state.update_data(memory=message.text)
    await message.answer("Введите состояние аккумулятора (например, 85%):")
    await state.set_state(SellAppleStates.entering_battery)

@router.message(SellAppleStates.entering_battery)
async def attach_photos(message: types.Message, state: FSMContext):
    await state.update_data(battery=message.text)
    await message.answer("Прикрепите фото устройства:")
    await state.set_state(SellAppleStates.attaching_photos)

@router.message(SellAppleStates.attaching_photos, content_types=types.ContentType.PHOTO)
async def enter_description(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Опишите товар (дефекты, ремонт, комплект и т.д.):")
    await state.set_state(SellAppleStates.entering_description)

@router.message(SellAppleStates.entering_description)
async def enter_price(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите цену:")
    await state.set_state(SellAppleStates.entering_price)

@router.message(SellAppleStates.entering_price)
async def enter_phone(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Введите ваш номер телефона:")
    await state.set_state(SellAppleStates.entering_phone)

@router.message(SellAppleStates.entering_phone)
async def confirm_sell(message: types.Message, state: FSMContext):
    data = await state.get_data()
    response = (f"Вы продаете: {data['category']} {data['model']} {data['memory']}\n"
                f"Батарея: {data['battery']}\n"
                f"Описание: {data['description']}\n"
                f"Цена: {data['price']}\n"
                f"Контакт: {message.text}\n\nМенеджер свяжется с вами.")
    await message.answer_photo(data['photo'], caption=response)
    await state.clear()

@router.message(lambda message: message.text == "Android")
async def sell_android(message: types.Message, state: FSMContext):
    await message.answer("Скупаем только телефоны. Введите модель устройства:")
    await state.set_state(SellAndroidStates.entering_model)

@router.message(SellAndroidStates.entering_model)
async def enter_android_memory(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await message.answer("Введите объем памяти:")
    await state.set_state(SellAndroidStates.entering_memory)

@router.message(SellAndroidStates.entering_memory)
async def attach_android_photos(message: types.Message, state: FSMContext):
    await state.update_data(memory=message.text)
    await message.answer("Прикрепите фото устройства:")
    await state.set_state(SellAndroidStates.attaching_photos)

@router.message(SellAndroidStates.attaching_photos, content_types=types.ContentType.PHOTO)
async def enter_android_description(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Опишите товар (дефекты, ремонт, комплект и т.д.):")
    await state.set_state(SellAndroidStates.entering_description)

@router.message(SellAndroidStates.entering_description)
async def enter_android_price(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите цену:")
    await state.set_state(SellAndroidStates.entering_price)

@router.message(SellAndroidStates.entering_price)
async def enter_android_phone(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Введите ваш номер телефона:")
    await state.set_state(SellAndroidStates.entering_phone)

@router.message(SellAndroidStates.entering_phone)
async def confirm_android_sell(message: types.Message, state: FSMContext):
    data = await state.get_data()
    response = (f"Вы продаете: Android {data['model']} {data['memory']}\n"
                f"Описание: {data['description']}\n"
                f"Цена: {data['price']}\n"
                f"Контакт: {message.text}\n\nМенеджер свяжется с вами.")
    await message.answer_photo(data['photo'], caption=response)
    await state.clear()
