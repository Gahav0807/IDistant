from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Меню выбора устройств Apple при покупке
apple_device_menu_builder = ReplyKeyboardBuilder()
apple_device_menu_builder.button(text="IPhone")
apple_device_menu_builder.button(text="Apple Watch")
apple_device_menu_builder.adjust(2)  # Перенос на новую строку
apple_device_menu_builder.button(text="AirPods")
# apple_device_menu_builder.button(text="Mac")
apple_device_menu_builder.button(text="IPad")
apple_device_menu_builder.adjust(1)
apple_device_menu_builder.button(text="Главное меню")
apple_device_menu = apple_device_menu_builder.as_markup(resize_keyboard=True)

# Меню выбора конфигурации iPhone
iphone_models_builder = ReplyKeyboardBuilder()
iphone_models_builder.button(text="iPhone 13")
iphone_models_builder.button(text="iPhone 14")
iphone_models_builder.adjust(2)  # Перенос на новую строку
iphone_models_builder.button(text="iPhone 15")
iphone_models_builder.button(text="iPhone 16")
iphone_models_builder.adjust(2)  # Перенос на новую строку
iphone_models_builder.button(text="iPhone 15 Pro Max")
iphone_models_builder.button(text="iPhone 16 Pro Max")
iphone_models_builder.adjust(2)  # Перенос на новую строку
iphone_models_builder.button(text="Главное меню")  # Кнопка для возврата
iphone_models = iphone_models_builder.as_markup(resize_keyboard=True)

# Все модели iPhone
all_iphone_models_builder = ReplyKeyboardBuilder()
all_iphone_models_builder.button(text="iPhone 16")
all_iphone_models_builder.button(text="iPhone 16 Pro")
all_iphone_models_builder.button(text="iPhone 16 Pro Max")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone 15")
all_iphone_models_builder.button(text="iPhone 15 Pro")
all_iphone_models_builder.button(text="iPhone 15 Pro Max")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone 14")
all_iphone_models_builder.button(text="iPhone 14 Pro")
all_iphone_models_builder.button(text="iPhone 14 Pro Max")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone SE (3rd gen)")
all_iphone_models_builder.button(text="iPhone 13")
all_iphone_models_builder.button(text="iPhone 13 Pro")
all_iphone_models_builder.button(text="iPhone 13 Pro Max")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone 12")
all_iphone_models_builder.button(text="iPhone 12 Pro")
all_iphone_models_builder.button(text="iPhone 12 Pro Max")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone SE (2nd gen)")
all_iphone_models_builder.button(text="iPhone 11")
all_iphone_models_builder.button(text="iPhone 11 Pro")
all_iphone_models_builder.button(text="iPhone 11 Pro Max")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone XS")
all_iphone_models_builder.button(text="iPhone XS Max")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone X")
all_iphone_models_builder.button(text="iPhone XR")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone 8")
all_iphone_models_builder.button(text="iPhone 8 Plus")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone 7")
all_iphone_models_builder.button(text="iPhone 7 Plus")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone 6s")
all_iphone_models_builder.button(text="iPhone 6s Plus")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone 6")
all_iphone_models_builder.button(text="iPhone 6 Plus")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="iPhone 5s")
all_iphone_models_builder.button(text="iPhone 5")
all_iphone_models_builder.adjust(2)  # Перенос на новую строку
all_iphone_models_builder.button(text="Главное меню")  # Кнопка для возврата
all_iphone_models = all_iphone_models_builder.as_markup(resize_keyboard=True)

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

# Меню выбора AirPods: оригинал или копия
air_pods_ways_builder = ReplyKeyboardBuilder()
air_pods_ways_builder.button(text="Оригинал")
air_pods_ways_builder.button(text="Копия")
air_pods_ways_builder.adjust(2)  # Перенос на новую строку
air_pods_ways_builder.button(text="Главное меню")  # Кнопка для возврата
air_pods_ways = air_pods_ways_builder.as_markup(resize_keyboard=True)

# Меню моделей AirPods
air_pods_models_builder = ReplyKeyboardBuilder()
air_pods_models_builder.button(text="AirPods 2")
air_pods_models_builder.button(text="AirPods 3")
air_pods_models_builder.adjust(2)  # Перенос на новую строку
air_pods_models_builder.button(text="AirPods 4")
air_pods_models_builder.button(text="AirPods Pro")
air_pods_models_builder.button(text="AirPods Pro 2")
air_pods_models_builder.adjust(1)  # Перенос на новую строку
air_pods_models_builder.button(text="Главное меню")  # Кнопка для возврата
air_pods_models = air_pods_models_builder.as_markup(resize_keyboard=True)

# Меню выбора моделей iPad
ipad_models_builder = ReplyKeyboardBuilder()
ipad_models_builder.button(text="iPad Air (5)")
ipad_models_builder.button(text="iPad Pro 12,9 (6)")
ipad_models_builder.adjust(2)  # Перенос на новую строку
ipad_models_builder.button(text="iPad Pro 11 (5)")
ipad_models_builder.adjust(1)  # Перенос на новую строку
ipad_models_builder.button(text="Главное меню")  # Кнопка для возврата
ipad_models = ipad_models_builder.as_markup(resize_keyboard=True)

# Выбор памяти для iPad Air (5)
ipad_air_5_memory_builder = ReplyKeyboardBuilder()
ipad_air_5_memory_builder.button(text="64 ГБ")
ipad_air_5_memory_builder.button(text="256 ГБ")
ipad_air_5_memory_builder.adjust(2)  # Перенос на новую строку
ipad_air_5_memory_builder.button(text="Главное меню")
ipad_air_5_memory = ipad_air_5_memory_builder.as_markup(resize_keyboard=True)

ipad_pro_12_9_6_memory_builder = ReplyKeyboardBuilder()
ipad_pro_12_9_6_memory_builder.button(text="128 ГБ")
ipad_pro_12_9_6_memory_builder.button(text="256 ГБ")
ipad_pro_12_9_6_memory_builder.adjust(2)
ipad_pro_12_9_6_memory_builder.button(text="512 ГБ")
ipad_pro_12_9_6_memory_builder.button(text="1 ТБ")
ipad_pro_12_9_6_memory_builder.button(text="2 ТБ")
ipad_pro_12_9_6_memory_builder.adjust(1)
ipad_pro_12_9_6_memory_builder.button(text="Главное меню")
ipad_pro_12_9_6_memory = ipad_pro_12_9_6_memory_builder.as_markup(resize_keyboard=True)

ipad_pro_12_9_6_access_memory_builder = ReplyKeyboardBuilder()
ipad_pro_12_9_6_access_memory_builder.button(text="8 ГБ")
ipad_pro_12_9_6_access_memory_builder.button(text="16 ГБ")
ipad_pro_12_9_6_access_memory_builder.adjust(1)
ipad_pro_12_9_6_access_memory_builder.button(text="Главное меню")
ipad_pro_12_9_6_access_memory = ipad_pro_12_9_6_access_memory_builder.as_markup(resize_keyboard=True)

ipad_pro_11_5_memory_builder = ReplyKeyboardBuilder()
ipad_pro_11_5_memory_builder.button(text="128 ГБ")
ipad_pro_11_5_memory_builder.button(text="256 ГБ")
ipad_pro_11_5_memory_builder.adjust(2)
ipad_pro_11_5_memory_builder.button(text="512 ГБ")
ipad_pro_11_5_memory_builder.button(text="1 ТБ")
ipad_pro_11_5_memory_builder.button(text="2 ТБ")
ipad_pro_11_5_memory_builder.adjust(1)
ipad_pro_11_5_memory_builder.button(text="Главное меню")
ipad_pro_11_5_memory = ipad_pro_11_5_memory_builder.as_markup(resize_keyboard=True)

ipad_pro_11_5_access_memory_builder = ReplyKeyboardBuilder()
ipad_pro_11_5_access_memory_builder.button(text="8 ГБ")
ipad_pro_11_5_access_memory_builder.button(text="16 ГБ")
ipad_pro_11_5_access_memory_builder.adjust(1)
ipad_pro_11_5_access_memory_builder.button(text="Главное меню")
ipad_pro_11_5_access_memory = ipad_pro_11_5_access_memory_builder.as_markup(resize_keyboard=True)
