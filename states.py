from aiogram.fsm.state import State, StatesGroup

class BuyAppleStates(StatesGroup):
    choosing_category = State()    # Выбор категории (Айфон, Эпл Вотч, Подсы, Мак, Айпад)
    choosing_model = State()       # Выбор модели (iPhone, Apple Watch, Подсы, Mac)
    choosing_memory = State()      # Выбор объёма памяти (только для iPhone)
    choosing_color = State()       # Выбор цвета (iPhone, Apple Watch)
    entering_phone = State()       # Ввод номера телефона
    confirming = State()           # Подтверждение заявки
    choosing_type = State()        # Выбор типа для Подсов и Мак (Оригинал/Копия)
    choosing_size = State()        # Выбор размера для Apple Watch
    pick_up_by_value = State() 
    condition = State() 
    choosing_airpods_way = State()

class BuyAndroidStates(StatesGroup):
    choosing_brand = State()
    entering_budget = State()
    awaiting_admin_response = State()

class SellAppleStates(StatesGroup):
    entering_device = State()
    entering_model = State()
    entering_memory = State()
    entering_battery = State()
    attaching_photos = State()
    entering_description = State()
    entering_price = State()
    entering_phone = State()

class SellAndroidStates(StatesGroup):
    entering_model = State()
    entering_memory = State()
    attaching_photos = State()
    entering_description = State()
    entering_price = State()
    entering_phone = State()

class RepairStates(StatesGroup):
    choosing_brand = State()
    choosing_model = State()
    entering_issue_description = State()
    attaching_photos = State()
    entering_phone = State()

class TradeInStates(StatesGroup):
    choosing_current_model = State()
    entering_memory = State()
    entering_battery = State()
    attaching_photos = State()
    entering_description = State()
    choosing_new_model = State()
    entering_phone = State()