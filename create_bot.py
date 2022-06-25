from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()


bot = Bot(token ='5181943973:AAGwCFyK7nwaox8NsTn8ZT0SUciA7VXXypI')
dp = Dispatcher(bot, storage=storage)