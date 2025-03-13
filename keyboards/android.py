from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Меню продажи Android
sell_android_menu_builder = ReplyKeyboardBuilder()
sell_android_menu_builder.button(text="Samsung")
sell_android_menu_builder.button(text="Другие бренды")
sell_android_menu_builder.adjust(2)
sell_android_menu_builder.button(text="Главное меню")
sell_android_menu = sell_android_menu_builder.as_markup(resize_keyboard=True)

# Меню ремонта Android
repair_android_menu_builder = ReplyKeyboardBuilder()
repair_android_menu_builder.button(text="Samsung")
repair_android_menu_builder.button(text="Другие бренды")
repair_android_menu_builder.adjust(2)
repair_android_menu_builder.button(text="Главное меню")
repair_android_menu = repair_android_menu_builder.as_markup(resize_keyboard=True)

# Меню покупки Apple
buy_android_menu_builder = ReplyKeyboardBuilder()
repair_android_menu_builder.button(text="Samsung")
repair_android_menu_builder.button(text="Другие бренды")
repair_android_menu_builder.adjust(2)
repair_android_menu_builder.button(text="Главное меню")
buy_android_menu = repair_android_menu_builder.as_markup(resize_keyboard=True)

