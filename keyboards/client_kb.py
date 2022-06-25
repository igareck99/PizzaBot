from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

k1 = KeyboardButton('/Режим_работы')
k2 = KeyboardButton('/Адрес')

kb_client = ReplyKeyboardMarkup()
kb_client.add(k1).add(k2)