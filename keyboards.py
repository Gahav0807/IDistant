from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Купить"))
main_menu.add(KeyboardButton("Продать"))
main_menu.add(KeyboardButton("Ремонт"))
main_menu.add(KeyboardButton("О нас"))
main_menu.add(KeyboardButton("Связь с менеджером"))
main_menu.add(KeyboardButton("Трейд-ин"))

# Меню покупки
buy_menu = ReplyKeyboardMarkup(resize_keyboard=True)
buy_menu.add(KeyboardButton("Apple"))
buy_menu.add(KeyboardButton("Android"))
buy_menu.add(KeyboardButton("Dyson"))

# Меню продажи
sell_menu = ReplyKeyboardMarkup(resize_keyboard=True)
sell_menu.add(KeyboardButton("Apple"))
sell_menu.add(KeyboardButton("Android"))

# Меню ремонта
repair_menu = ReplyKeyboardMarkup(resize_keyboard=True)
repair_menu.add(KeyboardButton("Apple"))
repair_menu.add(KeyboardButton("Android"))

# Меню трейд-ин
trade_menu = ReplyKeyboardMarkup(resize_keyboard=True)
trade_menu.add(KeyboardButton("Apple"))

# Меню выбора устройств Apple при покупке
buy_apple_menu = ReplyKeyboardMarkup(resize_keyboard=True)
buy_apple_menu.add(KeyboardButton("Айфон"))
buy_apple_menu.add(KeyboardButton("Эпл Вотч"))
buy_apple_menu.add(KeyboardButton("Подсы"))
buy_apple_menu.add(KeyboardButton("Мак"))
buy_apple_menu.add(KeyboardButton("Айпад"))

# Меню выбора состояния товара (новое/БУ/подобрать)
condition_menu = ReplyKeyboardMarkup(resize_keyboard=True)
condition_menu.add(KeyboardButton("Новое"))
condition_menu.add(KeyboardButton("БУ"))
condition_menu.add(KeyboardButton("Подобрать"))

# Меню выбора конфигурации iPhone
iphone_models = ReplyKeyboardMarkup(resize_keyboard=True)
iphone_models.add(KeyboardButton("iPhone 13/14"))
iphone_models.add(KeyboardButton("iPhone 15"))
iphone_models.add(KeyboardButton("iPhone 16"))

# Меню выбора памяти
memory_menu = ReplyKeyboardMarkup(resize_keyboard=True)
memory_menu.add(KeyboardButton("128 ГБ"))
memory_menu.add(KeyboardButton("256 ГБ"))
memory_menu.add(KeyboardButton("512 ГБ"))
memory_menu.add(KeyboardButton("1 ТБ"))

# Меню выбора цвета
color_menu = ReplyKeyboardMarkup(resize_keyboard=True)
color_menu.add(KeyboardButton("Черный"))
color_menu.add(KeyboardButton("Белый"))
color_menu.add(KeyboardButton("Синий"))
color_menu.add(KeyboardButton("Красный"))
color_menu.add(KeyboardButton("Зеленый"))

# Меню подтверждения
confirm_menu = ReplyKeyboardMarkup(resize_keyboard=True)
confirm_menu.add(KeyboardButton("Подтвердить"))
confirm_menu.add(KeyboardButton("Отменить"))

# Меню продажи Apple
sell_apple_menu = ReplyKeyboardMarkup(resize_keyboard=True)
sell_apple_menu.add(KeyboardButton("Айфон"))
sell_apple_menu.add(KeyboardButton("Эпл Вотч"))
sell_apple_menu.add(KeyboardButton("Подсы"))
sell_apple_menu.add(KeyboardButton("Мак"))
sell_apple_menu.add(KeyboardButton("Айпад"))

# Меню продажи Android
sell_android_menu = ReplyKeyboardMarkup(resize_keyboard=True)
sell_android_menu.add(KeyboardButton("Samsung"))
sell_android_menu.add(KeyboardButton("Другие бренды"))

# Меню ремонта Apple
repair_apple_menu = ReplyKeyboardMarkup(resize_keyboard=True)
repair_apple_menu.add(KeyboardButton("Айфон"))
repair_apple_menu.add(KeyboardButton("Эпл Вотч"))
repair_apple_menu.add(KeyboardButton("Мак"))
repair_apple_menu.add(KeyboardButton("Айпад"))

# Меню ремонта Android
repair_android_menu = ReplyKeyboardMarkup(resize_keyboard=True)
repair_android_menu.add(KeyboardButton("Samsung"))
repair_android_menu.add(KeyboardButton("Другие бренды"))

# Меню трейд-ин Apple
trade_in_apple_menu = ReplyKeyboardMarkup(resize_keyboard=True)
trade_in_apple_menu.add(KeyboardButton("Айфон"))
trade_in_apple_menu.add(KeyboardButton("Эпл Вотч"))
trade_in_apple_menu.add(KeyboardButton("Мак"))
trade_in_apple_menu.add(KeyboardButton("Айпад"))
