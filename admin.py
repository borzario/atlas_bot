from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

import sp_adm
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sklad

import keyboard_main


ID = sp_adm.admin


async def zakbtr(message: types.Message):
    if message.from_user.id == ID:
        await sklad.zakbeztrack(message)

class Ponomeru(StatesGroup):
    sost1 = State()

async def zakpn1(message: types.Message):
    if message.from_user.id == ID:
        await message.reply("веди номер заказа")
        await Ponomeru.sost1.set()

async def zakpn2(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        num = message.text
        await sklad.zakpn(message,num)
        await state.finish()

class Vbit(StatesGroup):
    sost1 = State()

async def vtr1(message: types.Message):
    if message.from_user.id == ID:
        await message.reply("веди номер заказа, трек номер через пробел")
        await Vbit.sost1.set()

async def vtr2(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        num = message.text.split()
        if len(num) == 2:
            await sklad.vbittrack(num[0], num[1])
        await state.finish()

class Answer(StatesGroup):
    sost1 = State()
    sost2 = State()

async def ans1(message: types.Message):
    if message.from_user.id == ID:
        await message.reply("vведи номер обращения")
        await Answer.sost1.set()

async def ans2(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["number"] = message.text
        await message.reply("Введи ответ на обращение")
        await Answer.sost2.set()

async def ans3(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["answer"] = message.text
        await sklad.otvobr(state)
        await message.reply("Готово")
        await state.finish()


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#начало диалога с ботом по адмиской части
#@dp.message_hendler(commands = ["загрузить"])
async def start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply("Загрузи фото товара")


#запиливаем функцию отмены загрузки
#@dp.message_hendler(state = "*", commands = 'отмена')
#@dp.message_hendler(Text(equals = 'отмена', ignore_case = True), state = "*")
async def cancel(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply("OK")

#первый ответ ловится, заполняется словарь
#@dp.message_hendler(content_types = ['photo'], state = FSMAdmin.photo)
async def load_photo(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["photo"] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Введи название товара")

#второй ответ ловится, заполняется словарь
#@dp.message_hendler(state = FSMAdmin.name)
async def load_name(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["name"] = message.text
        await FSMAdmin.next()
        await message.reply("Введи описание товара")

#третий ответ ловится
#@dp.message_hendler(state = FSMAdmin.description)
async def load_description(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["description"] = message.text
        await FSMAdmin.next()
        await message.reply("Введи цену товара")

#@dp.message_hendler(state = FSMAdmin.price)
async def load_price(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["price"] = message.text
        await sklad.sklad_add(state)
        await state.finish()

async def vall(message: types.Message):
    if message.from_user.id == ID:
        await sklad.vall(message)


async def tp(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери что хочешь замутить с обращением", reply_markup=keyboard_main.kb_adm_obr)

async def obrBezOtv(message: types.Message):
    if message.from_user.id == ID:
        await sklad.obrBezOtv(message)


#регистрация хендлеров для передачи в основной файл
def registr_admin(dp: Dispatcher):
    dp.register_message_handler(tp, commands=["обращения"], state=None)
    dp.register_message_handler(zakpn1, commands=["заказпономеру"], state = None)
    dp.register_message_handler(vtr1, commands=["вбитьтрекномер"], state = None)
    dp.register_message_handler(ans1, commands=["ответить_на_обращение"], state = None)
    dp.register_message_handler(zakbtr, commands=["безтрека"])
    dp.register_message_handler(obrBezOtv, commands=["обращения_без_ответа"])
    dp.register_message_handler(vall, commands=["выгрузитьвсе"])
    dp.register_message_handler(start, commands=["загрузить"], state = None)
    dp.register_message_handler(cancel, state="*", commands='отмена')
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(zakpn2, state=Ponomeru.sost1)
    dp.register_message_handler(vtr2, state=Vbit.sost1)
    dp.register_message_handler(ans2, state=Answer.sost1)
    dp.register_message_handler(ans3, state=Answer.sost2)
    dp.register_message_handler(load_photo, content_types = ['photo'], state = FSMAdmin.photo)
    dp.register_message_handler(load_name, state = FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
