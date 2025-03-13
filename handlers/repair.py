from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from keyboards import repair_menu, repair_apple_menu, repair_android_menu, confirm_menu
from states import RepairStates

router = Router()

@router.message(Command("repair"))
async def start_repair(message: types.Message):
    await message.answer("Выберите категорию устройства для ремонта:", reply_markup=repair_menu)

# Разделение по платформам: Apple или Android
@router.message(lambda message: message.text == "Apple")
async def repair_apple(message: types.Message):
    await message.answer("Выберите модель устройства для ремонта:", reply_markup=repair_apple_menu)

@router.message(lambda message: message.text == "Android")
async def repair_android(message: types.Message):
    await message.answer("Выберите модель Android устройства для ремонта:", reply_markup=repair_android_menu)

# Ремонт для Apple
@router.message(lambda message: message.text in ["Айфон", "Эпл Вотч", "Мак", "Айпад"])
async def apple_repair(message: types.Message, state: FSMContext):
    await state.update_data(device=message.text)
    await message.answer("Опишите неисправность устройства:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RepairStates.entering_issue_description)

@router.message(RepairStates.entering_issue_description)
async def apple_repair_description(message: types.Message, state: FSMContext):
    await state.update_data(issue_description=message.text)
    await message.answer("Прикрепите фото устройства (если есть):", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RepairStates.attaching_photos)

@router.message(RepairStates.attaching_photos, content_types=types.ContentType.PHOTO)
async def apple_repair_photos(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Введите ваш номер телефона для связи:")
    await state.set_state(RepairStates.entering_phone)

@router.message(RepairStates.entering_phone)
async def apple_repair_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    response = (f"Вы отправили запрос на ремонт устройства {data['device']}:\n"
                f"Описание неисправности: {data['issue_description']}\n"
                f"Контактный номер: {data['phone']}\n\n"
                "С вами свяжется менеджер для уточнения деталей.")
    await message.answer_photo(data['photo'], caption=response, reply_markup=confirm_menu)
    await state.clear()

# Ремонт для Android
@router.message(lambda message: message.text in ["Samsung", "Другие бренды"])
async def android_repair(message: types.Message, state: FSMContext):
    await state.update_data(device=message.text)
    await message.answer("Опишите неисправность устройства:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RepairStates.entering_issue_description)

@router.message(RepairStates.entering_issue_description)
async def android_repair_description(message: types.Message, state: FSMContext):
    await state.update_data(issue_description=message.text)
    await message.answer("Прикрепите фото устройства (если есть):", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RepairStates.attaching_photos)

@router.message(RepairStates.attaching_photos, content_types=types.ContentType.PHOTO)
async def android_repair_photos(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Введите ваш номер телефона для связи:")
    await state.set_state(RepairStates.entering_phone)

@router.message(RepairStates.entering_phone)
async def android_repair_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    response = (f"Вы отправили запрос на ремонт устройства {data['device']}:\n"
                f"Описание неисправности: {data['issue_description']}\n"
                f"Контактный номер: {data['phone']}\n\n"
                "С вами свяжется менеджер для уточнения деталей.")
    await message.answer_photo(data['photo'], caption=response, reply_markup=confirm_menu)
    await state.clear()
