from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Меню ремонта Android
repair_android_menu_builder = ReplyKeyboardBuilder()
repair_android_menu_builder.button(text="Samsung")
repair_android_menu_builder.button(text="Другие бренды")
repair_android_menu_builder.adjust(2)
repair_android_menu_builder.button(text="Главное меню")
repair_android_menu = repair_android_menu_builder.as_markup(resize_keyboard=True)

# Меню покупки Apple
buy_android_menu_builder = ReplyKeyboardBuilder()
buy_android_menu_builder.button(text="Samsung")
buy_android_menu_builder.button(text="Xiaomi")
buy_android_menu_builder.button(text="Honor")
buy_android_menu_builder.button(text="Infinix")
buy_android_menu_builder.adjust(2)
buy_android_menu_builder.button(text="Главное меню")
buy_android_menu = buy_android_menu_builder.as_markup(resize_keyboard=True)

