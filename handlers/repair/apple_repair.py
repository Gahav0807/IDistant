from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states import RepairStates
from keyboards.apple import *
from keyboards.common import main_menu, share_phone_keyboard, confirm_menu, all_memory_menu, while_512_memory_menu

apple_repair_router = Router()

@apple_repair_router.message(lambda message: message.text == "Apple⚙️")
async def sell_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите устройство, которое хотите продать:", reply_markup=all_iphone_models)
    await state.set_state(RepairStates.choosing_model)

@apple_repair_router.message(RepairStates.choosing_model)
async def select_device(message: types.Message, state: FSMContext):
    model = message.text
    await state.update_data(model=model)
    
    await message.answer("Опишите деффект устройства: ", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RepairStates.entering_issue_description)

@apple_repair_router.message(RepairStates.entering_issue_description)
async def enter_model(message: types.Message, state: FSMContext):
    issue_description = await state.get_data()
    await state.update_data(issue_description=issue_description)

    await message.answer("Отправьте фото устройства с повреждением:")
    await state.set_state(RepairStates.attaching_photos)

@apple_repair_router.message(RepairStates.attaching_photos)
async def upload_photo(message: types.ChatPhoto, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)
    await message.answer("Введите ваш номер телефона или нажмите кнопку ниже:", reply_markup=share_phone_keyboard)
    await state.set_state(RepairStates.entering_phone)

@apple_repair_router.message(RepairStates.entering_phone, lambda message: message.contact)
async def confirm_sale(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    
    response = (
        f"Ваша заяка на ремонт:\n"
        f"Устройство: {data['model']}\n"
        f"Описание: {data['issue_description']}\n"
        f"Номер телефона: {phone_number}\n\n"
        "Подтвердите или отмените заявку.")

    await message.answer_photo(photo=data['photo'], caption=response, reply_markup=confirm_menu)
    await state.set_state(RepairStates.confirming)

@apple_repair_router.message(RepairStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        await message.answer("Заявка отправлена! В ближайшее время с вами свяжется менеджер.", reply_markup=main_menu)
    else:
        await message.answer("Вы отменили заявку.", reply_markup=main_menu)
    await state.clear()
