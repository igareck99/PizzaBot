from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

load_button = KeyboardButton('/Загрузить')
delete_button = KeyboardButton('/Удалить')
menu_button = KeyboardButton('/Меню')


kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(load_button).insert(delete_button).add(menu_button)