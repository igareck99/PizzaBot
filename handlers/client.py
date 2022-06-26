from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from database import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    print(message)
    await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup= kb_client)
    await message.delete()

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_work_time(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПН-ВС 10:00 - 23:00')

async def pizza_adress(message: types.Message):
    await bot.send_message(message.from_user.id, 'Улица Пушкина дом 34', reply_markup= ReplyKeyboardRemove())

@dp.message_handler(commands = ['Меню'])
async def pizza_menu_command(message: types.Message):
   await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands = ['start','help'])
    dp.register_message_handler(pizza_work_time, commands = ['Режим_работы'])
    dp.register_message_handler(pizza_adress, commands=['Адрес'])
    dp.register_message_handler(pizza_menu_command, commands = ['Меню'])