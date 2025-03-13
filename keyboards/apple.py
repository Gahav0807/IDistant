from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Меню выбора устройств Apple при покупке
apple_device_menu_builder = ReplyKeyboardBuilder()
apple_device_menu_builder.button(text="Айфон")
apple_device_menu_builder.button(text="Эпл Вотч")
apple_device_menu_builder.adjust(2)
apple_device_menu_builder.button(text="Подсы")
apple_device_menu_builder.button(text="Мак")
apple_device_menu_builder.button(text="Айпад")
apple_device_menu_builder.adjust(1)
apple_device_menu_builder.button(text="Главное меню")
apple_device_menu = apple_device_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора конфигурации iPhone
iphone_models_builder = ReplyKeyboardBuilder()
iphone_models_builder.button(text="iPhone 13")
iphone_models_builder.adjust(2)  # Перенос на новую строку

iphone_models_builder.button(text="iPhone 14")
iphone_models_builder.adjust(2)  # Перенос на новую строку

iphone_models_builder.button(text="iPhone 15")
iphone_models_builder.button(text="iPhone 15 Plus")
iphone_models_builder.button(text="iPhone 15 Pro")
iphone_models_builder.button(text="iPhone 15 Pro Max")
iphone_models_builder.adjust(2)  # Перенос на новую строку

iphone_models_builder.button(text="iPhone 16")
iphone_models_builder.button(text="iPhone 16 Plus")
iphone_models_builder.button(text="iPhone 16 Pro")
iphone_models_builder.adjust(2)  # Перенос на новую строку
iphone_models_builder.button(text="iPhone 16 Pro Max")

iphone_models_builder.button(text="Главное меню")  # Кнопка для возврата
iphone_models = iphone_models_builder.as_markup(resize_keyboard=True)