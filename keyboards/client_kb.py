from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

k1 = KeyboardButton('/Режим_работы')
k2 = KeyboardButton('/Адрес')

k3 = KeyboardButton('Поделиться номером', request_contact=True)
k4 = KeyboardButton('Поделиться номером', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.insert(k1).insert(k2)
kb_client.row(k3,k4)
#kb_client.row(k1,k2)