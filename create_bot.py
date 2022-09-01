from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token = os.getenv("TOKEN"))
pay_token = os.getenv("PAY_TOKEN")
#загнать сюда токен админа еще
dp = Dispatcher(bot, storage=storage)