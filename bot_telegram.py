from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token ='5181943973:AAGwCFyK7nwaox8NsTn8ZT0SUciA7VXXypI')
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот успешно запущен')

@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс, напишит ему')

@dp.message_handler(commands=['Режим_работы'])
async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПН-ВС 10:00 - 23:00')

@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет')
    #await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates = True, on_startup =  on_startup)