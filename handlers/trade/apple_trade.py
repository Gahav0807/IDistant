from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states import TradeInStates
from keyboards.apple import *
from keyboards.common import main_menu, share_phone_keyboard, confirm_menu, all_memory_menu, while_512_memory_menu

apple_trade_router = Router()

@apple_trade_router.message(lambda message: message.text == "Apple🔄️")
async def sell_apple(message: types.Message, state: FSMContext):
    await message.answer("Выберите модель, которую хотите обменять:", reply_markup=all_iphone_models)
    await state.set_state(TradeInStates.choosing_current_model)

@apple_trade_router.message(TradeInStates.choosing_current_model)
async def enter_model(message: types.Message, state: FSMContext):
    model=message.text
    await state.update_data(current_model=model)

    await message.answer("Введите объем встроенной памяти, а также оперативную память; пример:\n512/16", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(TradeInStates.entering_memory)
           
@apple_trade_router.message(TradeInStates.entering_memory)
async def enter_memory(message: types.Message, state: FSMContext):
    await state.update_data(memory=message.text)
    await message.answer("Введите состояние аккумулятора в %:")
    await state.set_state(TradeInStates.entering_battery)

@apple_trade_router.message(TradeInStates.entering_battery)
async def enter_battery(message: types.Message, state: FSMContext):
    await state.update_data(battery=message.text)
    await message.answer("Прикрепите фото устройства:")
    await state.set_state(TradeInStates.attaching_photos)

@apple_trade_router.message(TradeInStates.attaching_photos)
async def upload_photo(message: types.ChatPhoto, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)
    await message.answer("Опишите товар (есть ли дефекты, был ли в ремонте, комплект и т.д.):")
    await state.set_state(TradeInStates.entering_description)

@apple_trade_router.message(TradeInStates.entering_description)
async def enter_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите модель на которую хотите обменять своё устройство:", reply_markup=all_iphone_models)
    await state.set_state(TradeInStates.choosing_new_model)

@apple_trade_router.message(TradeInStates.choosing_new_model)
async def enter_price(message: types.Message, state: FSMContext):
    await state.update_data(new_model=message.text)
    await message.answer("Введите ваш номер телефона или нажмите кнопку ниже:", reply_markup=share_phone_keyboard)
    await state.set_state(TradeInStates.entering_phone)

@apple_trade_router.message(TradeInStates.entering_phone, lambda message: message.contact)
async def confirm_sale(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    
    response = (
            f"Вы хотите обменять:\n"
            f"Устройство: {data['current_model']}\n"
            f"Описание: {data['description']}\n"
            f"АКБ: {data['battery']}\n\n"
            f"Номер телефона: {phone_number}\n\n"
            f"На модель: {data['new_model']}\n\n"
            "Подтвердите или отмените заявку.")
    
    await message.answer_photo(photo=data['photo'], caption=response, reply_markup=confirm_menu)
    await state.set_state(TradeInStates.confirming)

@apple_trade_router.message(TradeInStates.confirming)
async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        await message.answer("Заявка отправлена! В ближайшее время с вами свяжется менеджер.", reply_markup=main_menu)
    else:
        await message.answer("Вы отменили заявку.", reply_markup=main_menu)
    await state.clear()
