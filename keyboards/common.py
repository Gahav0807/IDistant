from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

# Главное меню
main_menu_builder = ReplyKeyboardBuilder()
main_menu_builder.button(text="Купить")
main_menu_builder.button(text="Продать")
main_menu_builder.button(text="Ремонт")
main_menu_builder.adjust(2)
main_menu_builder.button(text="Трейд-ин")
main_menu_builder.button(text="О нас")
main_menu_builder.adjust(2)
main_menu_builder.button(text="Связь с менеджером")
main_menu_builder.button(text="Главное меню")
main_menu = main_menu_builder.as_markup(resize_keyboard=True)

# Меню покупки
buy_menu_builder = ReplyKeyboardBuilder()
buy_menu_builder.button(text="Apple")
buy_menu_builder.button(text="Android")
buy_menu_builder.button(text="Dyson")
buy_menu_builder.adjust(2)
buy_menu_builder.button(text="Главное меню")
buy_menu = buy_menu_builder.as_markup(resize_keyboard=True)

# Меню продажи
sell_menu_builder = ReplyKeyboardBuilder()
sell_menu_builder.button(text="Apple")
sell_menu_builder.button(text="Android")
sell_menu_builder.adjust(2)
sell_menu_builder.button(text="Главное меню")
sell_menu = sell_menu_builder.as_markup(resize_keyboard=True)

# Меню ремонта
repair_menu_builder = ReplyKeyboardBuilder()
repair_menu_builder.button(text="Apple")
repair_menu_builder.button(text="Android")
repair_menu_builder.adjust(2)
repair_menu_builder.button(text="Главное меню")
repair_menu = repair_menu_builder.as_markup(resize_keyboard=True)

# Меню трейд-ин
trade_menu_builder = ReplyKeyboardBuilder()
trade_menu_builder.button(text="Apple")
trade_menu_builder.adjust(1)
trade_menu_builder.button(text="Главное меню")
trade_menu = trade_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора состояния товара
condition_menu_builder = ReplyKeyboardBuilder()
condition_menu_builder.button(text="Новое")
condition_menu_builder.button(text="БУ")
condition_menu_builder.adjust(2)
condition_menu_builder.button(text="Подобрать")
condition_menu_builder.adjust(1)
condition_menu_builder.button(text="Главное меню")
condition_menu = condition_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора памяти (128-512 ГБ)
while_512_memory_menu_builder = ReplyKeyboardBuilder()
while_512_memory_menu_builder.button(text="128 ГБ")
while_512_memory_menu_builder.button(text="256 ГБ")
while_512_memory_menu_builder.adjust(2)
while_512_memory_menu_builder.button(text="512 ГБ")
while_512_memory_menu_builder.adjust(1)
while_512_memory_menu_builder.button(text="Главное меню")
while_512_memory_menu = while_512_memory_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора памяти (128 ГБ - 1 ТБ)
all_memory_menu_builder = ReplyKeyboardBuilder()
all_memory_menu_builder.button(text="128 ГБ")
all_memory_menu_builder.button(text="256 ГБ")
all_memory_menu_builder.adjust(2)
all_memory_menu_builder.button(text="512 ГБ")
all_memory_menu_builder.button(text="1 ТБ")
all_memory_menu_builder.adjust(1)
all_memory_menu_builder.button(text="Главное меню")
all_memory_menu = all_memory_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора цвета
color_menu_builder = ReplyKeyboardBuilder()
color_menu_builder.button(text="Черный")
color_menu_builder.button(text="Белый")
color_menu_builder.adjust(2)
color_menu_builder.button(text="Синий")
color_menu_builder.button(text="Красный")
color_menu_builder.button(text="Зеленый")
color_menu_builder.adjust(1)
color_menu_builder.button(text="Главное меню")
color_menu = color_menu_builder.as_markup(resize_keyboard=True)

# Меню подтверждения
confirm_menu_builder = ReplyKeyboardBuilder()
confirm_menu_builder.button(text="Подтвердить")
confirm_menu_builder.button(text="Отменить")
confirm_menu_builder.adjust(2)
confirm_menu_builder.button(text="Главное меню")
confirm_menu = confirm_menu_builder.as_markup(resize_keyboard=True)

# Клавиатура с кнопкой "Поделиться номером"
share_phone_keyboard_builder = ReplyKeyboardBuilder()
share_phone_keyboard_builder.button(text="📞 Поделиться номером", request_contact=True)
share_phone_keyboard = share_phone_keyboard_builder.as_markup(resize_keyboard=True)
