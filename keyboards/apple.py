from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Меню выбора устройств Apple при покупке
apple_device_menu_builder = ReplyKeyboardBuilder()
apple_device_menu_builder.button(text="IPhone")
apple_device_menu_builder.button(text="Apple Watch")
apple_device_menu_builder.adjust(2)
apple_device_menu_builder.button(text="AirPods")
apple_device_menu_builder.button(text="Mac")
apple_device_menu_builder.button(text="IPad")
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

# apple watch
apple_watch_models_builder = ReplyKeyboardBuilder()
apple_watch_models_builder.button(text="Apple Watch Series 8")
apple_watch_models_builder.button(text="Apple Watch SE(1 поколения)")
apple_watch_models_builder.adjust(2)  # Перенос на новую строку
apple_watch_models_builder.button(text="Apple Watch Series 9")
apple_watch_models_builder.button(text="Apple Watch SE(2 поколения)")
apple_watch_models_builder.adjust(2)  # Перенос на новую строку
apple_watch_models_builder.button(text="Главное меню")  # Кнопка для возврата
apple_watch_models = apple_watch_models_builder.as_markup(resize_keyboard=True)

apple_watch_simple_size_builder = ReplyKeyboardBuilder()
apple_watch_simple_size_builder.button(text="41 мм")
apple_watch_simple_size_builder.button(text="45 мм")
apple_watch_simple_size_builder.adjust(2)  
apple_watch_simple_size_builder.button(text="Главное меню")  # Кнопка для возврата
apple_watch_simple_size = apple_watch_simple_size_builder.as_markup(resize_keyboard=True)

apple_watch_se1_size_builder = ReplyKeyboardBuilder()
apple_watch_se1_size_builder.button(text="40 мм")
apple_watch_se1_size_builder.button(text="44 мм")
apple_watch_se1_size_builder.adjust(2)  
apple_watch_se1_size_builder.button(text="Главное меню")  # Кнопка для возврата
apple_watch_se1_size = apple_watch_se1_size_builder.as_markup(resize_keyboard=True)

apple_watch_se2_size_builder = ReplyKeyboardBuilder()
apple_watch_se2_size_builder.button(text="38 × 44 × 10,7 мм")
apple_watch_se2_size_builder.adjust(2)  
apple_watch_se2_size_builder.button(text="Главное меню")  # Кнопка для возврата
apple_watch_se2_size = apple_watch_se2_size_builder.as_markup(resize_keyboard=True)

apple_watch_color_builder = ReplyKeyboardBuilder()
apple_watch_color_builder.button(text="Черный")
apple_watch_color_builder.button(text="Серебристый")
apple_watch_color_builder.adjust(2)  
apple_watch_color_builder.button(text="Главное меню")  # Кнопка для возврата
apple_watch_color = apple_watch_color_builder.as_markup(resize_keyboard=True)

#  Подсы
air_pods_ways_builder = ReplyKeyboardBuilder()
air_pods_ways_builder.button(text="Оригинал")
air_pods_ways_builder.button(text="Копия")
air_pods_ways_builder.adjust(2)  
air_pods_ways_builder.button(text="Главное меню")  # Кнопка для возврата
air_pods_ways = air_pods_ways_builder.as_markup(resize_keyboard=True)

air_pods_models_builder = ReplyKeyboardBuilder()
air_pods_models_builder.button(text="AirPods 2")
air_pods_models_builder.button(text="AirPods 3")
air_pods_models_builder.adjust(3) 
air_pods_models_builder.button(text="AirPods 4") 
air_pods_models_builder.button(text="AirPods Pro")
air_pods_models_builder.button(text="AirPods Pro 2")
air_pods_models_builder.adjust(1) 
air_pods_models_builder.button(text="Главное меню")  # Кнопка для возврата
air_pods_models = air_pods_models_builder.as_markup(resize_keyboard=True)

