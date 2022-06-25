from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = '5181943973:AAGwCFyK7nwaox8NsTn8ZT0SUciA7VXXypI')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет')
    #await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates = True)