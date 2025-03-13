from aiogram.fsm.state import State, StatesGroup

class BuyAppleStates(StatesGroup):
    choosing_category = State()
    choosing_model = State()
    choosing_memory = State()
    choosing_color = State()
    entering_phone = State()

class BuyAndroidStates(StatesGroup):
    choosing_brand = State()
    entering_budget = State()
    awaiting_admin_response = State()

class SellAppleStates(StatesGroup):
    choosing_device = State()
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
