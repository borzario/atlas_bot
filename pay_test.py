from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sklad
from keyboard_main import k_c_obr, kb_client_main


class Zakaz(StatesGroup):
    state1 = State()

async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Ведите полчателя")
    data["zak"] = message.text[6:-1]
    await Zakaz.state1.set()



async def opl(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["pol"] = message.text
    await print(data)
    await state.finish()









def registr_test(dp: Dispatcher):
    dp.register_message_handler(start, lambda message: "Test" in message.text, state = None)
    dp.register_message_handler(opl,  state=Zakaz.state1)
