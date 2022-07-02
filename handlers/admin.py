from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from database.sqlite_db import sql_add_command
from keyboards import admin_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import sqlite_db

ID = 0

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# @dp.message_handler(commands=['moderator'], is_chat_admin = True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await message.reply('Что хотел хозяин?', reply_markup=admin_buttons.kb_admin)
    await message.delete()



#@dp.message_handler(commands='Загрузить', state = None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')

@dp.message_handler(state='*', commands='отмена')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

#@dp.message_handler(content_types= ['photo'], state = FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
            await FSMAdmin.next()
            await message.reply('Теперь введи название')

#@dp.message_handler(state = FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
            await FSMAdmin.next()
            await message.reply('Теперь введи описание')

#@dp.message_handler(state = FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
            await FSMAdmin.next()
            await message.reply('Теперь введи цену')

#@dp.message_handler(state = FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await sql_add_command(state)
        await state.finish()

@dp.message_handler(lambda x: x.text and x.text.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    print("wedfjkdslk")
    await sqlite_db.sql_delete_command(callback_query.data.replace('del',''))
    await callback_query.answer(text = f'{callback_query.data.replace("del ","")} удалена.', show_alert = True)

#@dp.message_handler(state = 'Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for res in read:
            await bot.send_photo(message.from_user.id, res[0], f'{res[1]}\nОписание: {res[2]}\nЦена {res[-1]}')
            print(f'del {res[1]}')
            await bot.send_message(message.from_user.id, text = '^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {res[1]}', callback_data=f'del {res[1]}')))



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'],state=None)
    dp.register_message_handler(load_photo, content_types= ['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, commands = ['отмена'])
    dp.register_message_handler(delete_item, commands=['Удалить'])
    dp.register_message_handler(make_changes_command, commands = 'moderator')
    dp.register_message_handler(del_callback_run, lambda x: x.text.startswith('del '))