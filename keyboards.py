from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

# Главное меню
main_menu_builder = ReplyKeyboardBuilder()
main_menu_builder.button(text="Купить")
main_menu_builder.button(text="Продать")
main_menu_builder.button(text="Ремонт")
main_menu_builder.button(text="Трейд-ин")
main_menu_builder.button(text="О нас")
main_menu_builder.row()  # Перенос на новую строку
main_menu_builder.button(text="Связь с менеджером")
main_menu_builder.button(text="Главное меню")
main_menu = main_menu_builder.as_markup(resize_keyboard=True)

# Меню покупки
buy_menu_builder = ReplyKeyboardBuilder()
buy_menu_builder.button(text="Apple")
buy_menu_builder.button(text="Android")
buy_menu_builder.button(text="Dyson")
buy_menu_builder.row()  # Перенос на новую строку
buy_menu_builder.button(text="Главное меню")  # Кнопка для возврата
buy_menu = buy_menu_builder.as_markup(resize_keyboard=True)

# Меню продажи
sell_menu_builder = ReplyKeyboardBuilder()
sell_menu_builder.button(text="Apple")
sell_menu_builder.button(text="Android")
sell_menu_builder.row()  # Перенос на новую строку
sell_menu_builder.button(text="Главное меню")  # Кнопка для возврата
sell_menu = sell_menu_builder.as_markup(resize_keyboard=True)

# Меню ремонта
repair_menu_builder = ReplyKeyboardBuilder()
repair_menu_builder.button(text="Apple")
repair_menu_builder.button(text="Android")
repair_menu_builder.row()  # Перенос на новую строку
repair_menu_builder.button(text="Главное меню")  # Кнопка для возврата
repair_menu = repair_menu_builder.as_markup(resize_keyboard=True)

# Меню трейд-ин
trade_menu_builder = ReplyKeyboardBuilder()
trade_menu_builder.button(text="Apple")
trade_menu_builder.row()  # Перенос на новую строку
trade_menu_builder.button(text="Главное меню")  # Кнопка для возврата
trade_menu = trade_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора устройств Apple при покупке
buy_apple_menu_builder = ReplyKeyboardBuilder()
buy_apple_menu_builder.button(text="Айфон")
buy_apple_menu_builder.button(text="Эпл Вотч")
buy_apple_menu_builder.row()  # Перенос на новую строку
buy_apple_menu_builder.button(text="Подсы")
buy_apple_menu_builder.button(text="Мак")
buy_apple_menu_builder.button(text="Айпад")
buy_apple_menu_builder.row()  # Перенос на новую строку
buy_apple_menu_builder.button(text="Главное меню")  # Кнопка для возврата
buy_apple_menu = buy_apple_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора состояния товара (новое/БУ/подобрать)
condition_menu_builder = ReplyKeyboardBuilder()
condition_menu_builder.button(text="Новое")
condition_menu_builder.button(text="БУ")
condition_menu_builder.row()  # Перенос на новую строку
condition_menu_builder.button(text="Подобрать")
condition_menu_builder.row()  # Перенос на новую строку
condition_menu_builder.button(text="Главное меню")  # Кнопка для возврата
condition_menu = condition_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора конфигурации iPhone
iphone_models_builder = ReplyKeyboardBuilder()
iphone_models_builder.button(text="iPhone 13/14")
iphone_models_builder.button(text="iPhone 15")
iphone_models_builder.row()  # Перенос на новую строку
iphone_models_builder.button(text="iPhone 16")
iphone_models_builder.row()  # Перенос на новую строку
iphone_models_builder.button(text="Главное меню")  # Кнопка для возврата
iphone_models = iphone_models_builder.as_markup(resize_keyboard=True)

# Меню выбора памяти
memory_menu_builder = ReplyKeyboardBuilder()
memory_menu_builder.button(text="128 ГБ")
memory_menu_builder.button(text="256 ГБ")
memory_menu_builder.row()  # Перенос на новую строку
memory_menu_builder.button(text="512 ГБ")
memory_menu_builder.button(text="1 ТБ")
memory_menu_builder.row()  # Перенос на новую строку
memory_menu_builder.button(text="Главное меню")  # Кнопка для возврата
memory_menu = memory_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора цвета
color_menu_builder = ReplyKeyboardBuilder()
color_menu_builder.button(text="Черный")
color_menu_builder.button(text="Белый")
color_menu_builder.row()  # Перенос на новую строку
color_menu_builder.button(text="Синий")
color_menu_builder.button(text="Красный")
color_menu_builder.button(text="Зеленый")
color_menu_builder.row()  # Перенос на новую строку
color_menu_builder.button(text="Главное меню")  # Кнопка для возврата
color_menu = color_menu_builder.as_markup(resize_keyboard=True)

# Меню подтверждения
confirm_menu_builder = ReplyKeyboardBuilder()
confirm_menu_builder.button(text="Подтвердить")
confirm_menu_builder.button(text="Отменить")
confirm_menu_builder.row()  # Перенос на новую строку
confirm_menu_builder.button(text="Главное меню")  # Кнопка для возврата
confirm_menu = confirm_menu_builder.as_markup(resize_keyboard=True)

# Меню продажи Apple
sell_apple_menu_builder = ReplyKeyboardBuilder()
sell_apple_menu_builder.button(text="Айфон")
sell_apple_menu_builder.button(text="Эпл Вотч")
sell_apple_menu_builder.row()  # Перенос на новую строку
sell_apple_menu_builder.button(text="Подсы")
sell_apple_menu_builder.button(text="Мак")
sell_apple_menu_builder.button(text="Айпад")
sell_apple_menu_builder.row()  # Перенос на новую строку
sell_apple_menu_builder.button(text="Главное меню")  # Кнопка для возврата
sell_apple_menu = sell_apple_menu_builder.as_markup(resize_keyboard=True)

# Меню продажи Android
sell_android_menu_builder = ReplyKeyboardBuilder()
sell_android_menu_builder.button(text="Samsung")
sell_android_menu_builder.button(text="Другие бренды")
sell_android_menu_builder.row()  # Перенос на новую строку
sell_android_menu_builder.button(text="Главное меню")  # Кнопка для возврата
sell_android_menu = sell_android_menu_builder.as_markup(resize_keyboard=True)

# Меню ремонта Apple
repair_apple_menu_builder = ReplyKeyboardBuilder()
repair_apple_menu_builder.button(text="Айфон")
repair_apple_menu_builder.button(text="Эпл Вотч")
repair_apple_menu_builder.row()  # Перенос на новую строку
repair_apple_menu_builder.button(text="Мак")
repair_apple_menu_builder.button(text="Айпад")
repair_apple_menu_builder.row()  # Перенос на новую строку
repair_apple_menu_builder.button(text="Главное меню")  # Кнопка для возврата
repair_apple_menu = repair_apple_menu_builder.as_markup(resize_keyboard=True)

# Меню ремонта Android
repair_android_menu_builder = ReplyKeyboardBuilder()
repair_android_menu_builder.button(text="Samsung")
repair_android_menu_builder.button(text="Другие бренды")
repair_android_menu_builder.row()  # Перенос на новую строку
repair_android_menu_builder.button(text="Главное меню")  # Кнопка для возврата
repair_android_menu = repair_android_menu_builder.as_markup(resize_keyboard=True)

# Меню трейд-ин Apple
trade_in_apple_menu_builder = ReplyKeyboardBuilder()
trade_in_apple_menu_builder.button(text="Айфон")
trade_in_apple_menu_builder.button(text="Эпл Вотч")
trade_in_apple_menu_builder.row()  # Перенос на новую строку
trade_in_apple_menu_builder.button(text="Мак")
trade_in_apple_menu_builder.button(text="Айпад")
trade_in_apple_menu_builder.row()  # Перенос на новую строку
trade_in_apple_menu_builder.button(text="Главное меню")  # Кнопка для возврата
trade_in_apple_menu = trade_in_apple_menu_builder.as_markup(resize_keyboard=True)
