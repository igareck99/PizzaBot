from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text


bot = Bot(token ='5181943973:AAGwCFyK7nwaox8NsTn8ZT0SUciA7VXXypI')
dp = Dispatcher(bot)
answer = dict()

urlkb = InlineKeyboardMarkup(row_width=2)
urlkb1 = InlineKeyboardButton(text='Ссылка', url = 'https://www.youtube.com')
urlkb2 = InlineKeyboardButton(text='Ссылка2', url = 'https://www.google.ru/?gws_rd=ssl')
x = [InlineKeyboardButton(text='Ссылка3', url = 'https://www.youtube.com'),
     InlineKeyboardButton(text='Ссылка4', url = 'https://www.youtube.com'),
     InlineKeyboardButton(text='Ссылка5', url = 'https://www.youtube.com')]
urlkb.add(urlkb1, urlkb2).row(*x).insert(InlineKeyboardButton(text='Ссылка', url = 'https://www.youtube.com'))

@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Список ссылок', reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width = 1).add(InlineKeyboardButton(text='Like', callback_data='like_1')).\
                                            add(InlineKeyboardButton(text='Not Like', callback_data='like_-1'))
@dp.message_handler(commands = 'test')
async def test_command(message: types.Message):
    await  message.answer('Голосуй', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback : types.CallbackQuery):
    #await callback.answer('Нажата инлайн кнопка')
    res = int(callback.data.split('_')[1])
    if str(callback.from_user.id) not in answer:
        print("wfxsefs")
        answer[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)
    # await callback.answer('Вы проголосовали')
    # await callback.answer('Нажата инлайн кнопка', show_alert=True)
    # await callback.answer()


executor.start_polling(dp, skip_updates=True)