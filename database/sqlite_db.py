import sqlite3 as sq
from create_bot import dp, bot


def sql_start():
    global base, cur
    base = sq.connect('database.db')
    cur = base.cursor()
    if base:
        print('Database is connected')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for res in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, res[0], f'{res[1]}\nОписание: {res[2]}\nЦена {res[-1]}')