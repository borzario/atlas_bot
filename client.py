from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType

import create_bot
import sp_adm
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sklad
from keyboard_main import k_c_obr, kb_client_main


class FSMClient(StatesGroup):
    photo = State()
    name = State()
    adres = State()
    tel = State()
    zak = State()


async def start(message: types.Message):
    await sklad.put_to_base(message)
    await FSMClient.photo.set()
    await message.reply('Оплатите выбранный товар переводом на карту ХХХХ. Для продолжения оформления заказа отправьте '
                        'боту скриншот с переводом. Для отмены оформления нажмите кнопку "Отмена"')



"""#zakazaka = None
#начало диалога с ботом по адмиской части
#@dp.message_hendler(commands = ["загрузить"])
async def start(message: types.Message):
    #global zakazaka
    zakazaka = message.text
    await sklad.put_to_base(message)
    price_from_base = await sklad.test_load_price(zakazaka[9:-1])
    price = [LabeledPrice( "К оплате за товар", price_from_base*100)]
    await bot.send_invoice(message.from_user.id,
                           title=sklad.spisokT[f'{zakazaka[9:-1]}'].split('.')[0],
                           description='Счет на оплату товара',
                           provider_token=create_bot.pay_token,
                           photo_url="https://sun9-east.userapi.com/sun9-76/s/v1/ig2/P4VMiUEUHEFCeE4wycf5hpufl_gVBACAitld4QfuIt_g2KJbyGB-E3ytLE1vQqrTP3P80GaMKx0nX6UMP1rxOlPz.jpg?size=733x730&quality=95&type=album",
                           photo_width= '50',
                           photo_height= '50',
                           currency='rub',
                           prices=price,
                           start_parameter='example',
                           payload='some_invoice')
    #
    #await message.reply("Оплатите товар согласно указанному в описании ценнику переводом на карту 5280 4137 5183 6755 (получатель Никита П.).\nПрикрепите чек (отправьте сообщением)\n\n\
    #Для отмены заказа нажмите кнопку 'Отмена'")

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def s_pay(message: Message):
    await bot.send_message(message.from_user.id, 'Платеж прошел успешно!!!')
    await bot.send_message(message.from_user.id, 'Введите имя получателя')
    await FSMClient.name.set()"""

class Obr(StatesGroup):
    sost1 = State()

async def obr1(message: types.Message):
    await message.reply("Введите ваше обращение (в одном сообщении). Для отмены обращения нажмите кнопку 'Отмена'", reply_markup=k_c_obr)
    await Obr.sost1.set()

async def obr2(message : types.Message, state = FSMContext):
    num = message.text
    await sklad.obras(message, num)
    await state.finish()
    await bot.send_message(message.from_user.id, "Для продолжения работы с ботом выберите категорию", reply_markup=kb_client_main)


#запиливаем функцию отмены загрузки
#@dp.message_hendler(state = "*", commands = 'отмена')
#@dp.message_hendler(Text(equals = 'отмена', ignore_case = True), state = "*")
async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")

"""#первый ответ ловится, заполняется словарь
#@dp.message_hendler(content_types = ['photo'], state = FSMAdmin.photo)
async def load_photo(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMClient.next()
    await message.reply("Введи имя получателя")"""

async def load_photo(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await bot.send_message(message.from_user.id, 'Введите имя получателя')
    await FSMClient.name.set()

async def load_name(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        #data["photo"] = "скрин у пользователя в платежке"
        data["name"] = message.text
    await FSMClient.next()
    await message.reply("Введи адрес получения")

async def load_adres(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["adres"] = message.text
    await FSMClient.next()
    await message.reply("Введи телефон\контакт в телеграме для связи по заказу")

async def load_tel(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["tel"] = message.text
        data["zak"] = await sklad.get_from_base(message)
    await FSMClient.next()
    if data["zak"]  in "ЗЛ" or (data["zak"][2] == "M" and len(data["zak"]) == 6):
        await message.reply("Отправьте выбранный цвет чехла для изделия (Multicam, A-TACS FG, Khaki, Coyote Brown, Ranger Green, Dark Olive, ЕМР, Черный), укажите дополнительную информацию к заказу")
    else:
        await message.reply("Укажите дополнительную информацию к заказу")


async def load_zak(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        await message.reply("Заказ оформлен")
        await bot.send_photo(sp_adm.admin, data['photo'])
        await bot.send_message(sp_adm.admin, (sklad.spisokT[f'{data["zak"]}'] + f'\n {data["name"]},\n {data["tel"]},\n {data["adres"]}'))
    await bot.send_message(sp_adm.admin, message.text)
    await sklad.zakaz_add(state, message.from_user.id)
    await state.finish()



class IzmZak(StatesGroup):
    sost1 = State()
    sost2 = State()
    sost3 = State()
    sost4 = State()

async def izm1(message: types.Message):
    await message.reply("Введите номер заказа, данные получателя которого вы хотите изменить")
    await IzmZak.sost1.set()

async def izm2(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["number"] = message.text
        data['user'] = message.from_user.id
    await message.reply("Введите имя актуального получателя")
    await IzmZak.sost2.set()

async def izm3(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.reply("Введите адрес актуального получателя")
    await IzmZak.sost3.set()

async def izm4(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["adres"] = message.text
    await message.reply("Введите контактные данные актуального получателя (телефон или телеграмм")
    await IzmZak.sost4.set()

async def izm5(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["tel"] = message.text
    await sklad.izmzak(state)
    await message.reply("Готово")
    await state.finish()

#регистрация хендлеров для передачи в основной файл
def registr_client(dp: Dispatcher):
    dp.register_message_handler(izm1, lambda message: "Изменить Данные Получателя" in message.text, state=None)
    dp.register_message_handler(start, lambda message: "Заказать" in message.text, state = None)
    dp.register_message_handler(cancel, state="*", commands='отмена')
    dp.register_message_handler(obr1, lambda message: "Обратиться в поддержку" in message.text, state=None)
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(obr2, state=Obr.sost1)
    dp.register_message_handler(izm2, state=IzmZak.sost1)
    dp.register_message_handler(izm3, state=IzmZak.sost2)
    dp.register_message_handler(izm4, state=IzmZak.sost3)
    dp.register_message_handler(izm5, state=IzmZak.sost4)
    dp.register_message_handler(load_photo, content_types = ['photo'], state = FSMClient.photo)
    dp.register_message_handler(load_name, state = FSMClient.name)
    dp.register_message_handler(load_adres, state=FSMClient.adres)
    dp.register_message_handler(load_tel, state=FSMClient.tel)
    dp.register_message_handler(load_zak, state=FSMClient.zak)
