from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import autofication

storage = MemoryStorage()
bot = Bot(token = autofication.TOKEN)
pay_token = autofication.PAY_TOKEN
#загнать сюда токен админа еще
dp = Dispatcher(bot, storage=storage)