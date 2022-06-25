from aiogram import types, Dispatcher
from create_bot import dp, bot


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс, напишит ему')

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_work_time(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПН-ВС 10:00 - 23:00')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands = ['start','help'])
    dp.register_message_handler(pizza_work_time, commands = ['Режим_работы'])