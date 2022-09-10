"""
Указанный модуль представляет собой функции, работающие с базами данных, используемыми ботом
"""

import sqlite3 as sq
from datetime import date
from create_bot import dp, bot
import sp_adm

spisokT = {"ЗЛ": "Универсальная защита лица.",
           "5EL": "Бронеплита 5 класса защиты, размер Extra Large.",
           "5L": "Бронеплита 5 класса защиты, размер Large.",
           "5M": "Бронеплита 5 класса защиты, размер Medium.",
           "4EL": "Бронеплита 4 класса защиты, размер Extra Large.",
           "4L": "Бронеплита 4 класса защиты, размер Large.",
           "4M": "Бронеплита 4 класса защиты, размер Medium",
           "3+EL": "Бронеплита 3+ класса защиты, размер Extra Large.",
           "3+L": "Бронеплита 3+ класса защиты, размер Large.",
           "3+M": "Бронеплита 3+ класса защиты, размер Medium.",
           "0YSB56": "Бронешлем МК0. Ушастый. Штатная комплектация. Черный. 56 размер",
           "0YSB58": "Бронешлем МК0. Ушастый. Штатная комплектация. Черный. 58 размер",
           "0YSB60": "Бронешлем МК0. Ушастый. Штатная комплектация. Черный. 60 размер",
           "0YSS56": "Бронешлем МК0. Ушастый. Штатная комплектация. Песочный. 56 размер",
           "0YSS58": "Бронешлем МК0. Ушастый. Штатная комплектация. Песочный. 58 размер",
           "0YSS60": "Бронешлем МК0. Ушастый. Штатная комплектация. Песочный. 60 размер",
           "0YSO56": "Бронешлем МК0. Ушастый. Штатная комплектация. Оливковый. 56 размер",
           "0YSO58": "Бронешлем МК0. Ушастый. Штатная комплектация. Оливковый. 58 размер",
           "0YSO60": "Бронешлем МК0. Ушастый. Штатная комплектация. Оливковый. 60 размер",
           "0YMB56": "Бронешлем МК0. Ушастый. МОД+ комплектация. Черный. 56 размер",
           "0YMB58": "Бронешлем МК0. Ушастый. МОД+ комплектация. Черный. 58 размер",
           "0YMB60": "Бронешлем МК0. Ушастый. МОД+ комплектация. Черный. 60 размер",
           "0YMS56": "Бронешлем МК0. Ушастый. МОД+ комплектация. Песочный. 56 размер",
           "0YMS58": "Бронешлем МК0. Ушастый. МОД+ комплектация. Песочный. 58 размер",
           "0YMS60": "Бронешлем МК0. Ушастый. МОД+ комплектация. Песочный. 60 размер",
           "0YMO56": "Бронешлем МК0. Ушастый. МОД+ комплектация. Оливковый. 56 размер",
           "0YMO58": "Бронешлем МК0. Ушастый. МОД+ комплектация. Оливковый. 58 размер",
           "0YMO60": "Бронешлем МК0. Ушастый. МОД+ комплектация. Оливковый. 60 размер",
           "0BSB56": "Бронешлем МК0. Безухий. Штатная комплектация. Черный. 56 размер",
           "0BSB58": "Бронешлем МК0. Безухий. Штатная комплектация. Черный. 58 размер",
           "0BSB60": "Бронешлем МК0. Безухий. Штатная комплектация. Черный. 60 размер",
           "0BSS56": "Бронешлем МК0. Безухий. Штатная комплектация. Песочный. 56 размер",
           "0BSS58": "Бронешлем МК0. Безухий. Штатная комплектация. Песочный. 58 размер",
           "0BSS60": "Бронешлем МК0. Безухий. Штатная комплектация. Песочный. 60 размер",
           "0BSO56": "Бронешлем МК0. Безухий. Штатная комплектация. Оливковый. 56 размер",
           "0BSO58": "Бронешлем МК0. Безухий. Штатная комплектация. Оливковый. 58 размер",
           "0BSO60": "Бронешлем МК0. Безухий. Штатная комплектация. Оливковый. 60 размер",
           "0BMB56": "Бронешлем МК0. Безухий. МОД+ комплектация. Черный. 56 размер",
           "0BMB58": "Бронешлем МК0. Безухий. МОД+ комплектация. Черный. 58 размер",
           "0BMB60": "Бронешлем МК0. Безухий. МОД+ комплектация. Черный. 60 размер",
           "0BMS56": "Бронешлем МК0. Безухий. МОД+ комплектация. Песочный. 56 размер",
           "0BMS58": "Бронешлем МК0. Безухий. МОД+ комплектация. Песочный. 58 размер",
           "0BMS60": "Бронешлем МК0. Безухий. МОД+ комплектация. Песочный. 60 размер",
           "0BMO56": "Бронешлем МК0. Безухий. МОД+ комплектация. Оливковый. 56 размер",
           "0BMO58": "Бронешлем МК0. Безухий. МОД+ комплектация. Оливковый. 58 размер",
           "0BMO60": "Бронешлем МК0. Безухий. МОД+ комплектация. Оливковый. 60 размер",
           "2YSB56": "Бронешлем MK2. Ушастый. Штатная комплектация. Черный. 56 размер",
           "2YSB58": "Бронешлем MK2. Ушастый. Штатная комплектация. Черный. 58 размер",
           "2YSB60": "Бронешлем MK2. Ушастый. Штатная комплектация. Черный. 60 размер",
           "2YSS56": "Бронешлем MK2. Ушастый. Штатная комплектация. Песочный. 56 размер",
           "2YSS58": "Бронешлем MK2. Ушастый. Штатная комплектация. Песочный. 58 размер",
           "2YSS60": "Бронешлем MK2. Ушастый. Штатная комплектация. Песочный. 60 размер",
           "2YSO56": "Бронешлем MK2. Ушастый. Штатная комплектация. Оливковый. 56 размер",
           "2YSO58": "Бронешлем MK2. Ушастый. Штатная комплектация. Оливковый. 58 размер",
           "2YSO60": "Бронешлем MK2. Ушастый. Штатная комплектация. Оливковый. 60 размер",
           "2YMB56": "Бронешлем MK2. Ушастый. МОД+ комплектация. Черный. 56 размер",
           "2YMB58": "Бронешлем MK2. Ушастый. МОД+ комплектация. Черный. 58 размер",
           "2YMB60": "Бронешлем MK2. Ушастый. МОД+ комплектация. Черный. 60 размер",
           "2YMS56": "Бронешлем MK2. Ушастый. МОД+ комплектация. Песочный. 56 размер",
           "2YMS58": "Бронешлем MK2. Ушастый. МОД+ комплектация. Песочный. 58 размер",
           "2YMS60": "Бронешлем MK2. Ушастый. МОД+ комплектация. Песочный. 60 размер",
           "2YMO56": "Бронешлем MK2. Ушастый. МОД+ комплектация. Оливковый. 56 размер",
           "2YMO58": "Бронешлем MK2. Ушастый. МОД+ комплектация. Оливковый. 58 размер",
           "2YMO60": "Бронешлем MK2. Ушастый. МОД+ комплектация. Оливковый. 60 размер",
           "2BSB56": "Бронешлем MK2. Безухий. Штатная комплектация. Черный. 56 размер",
           "2BSB58": "Бронешлем MK2. Безухий. Штатная комплектация. Черный. 58 размер",
           "2BSB60": "Бронешлем MK2. Безухий. Штатная комплектация. Черный. 60 размер",
           "2BSS56": "Бронешлем MK2. Безухий. Штатная комплектация. Песочный. 56 размер",
           "2BSS58": "Бронешлем MK2. Безухий. Штатная комплектация. Песочный. 58 размер",
           "2BSS60": "Бронешлем MK2. Безухий. Штатная комплектация. Песочный. 60 размер",
           "2BSO56": "Бронешлем MK2. Безухий. Штатная комплектация. Оливковый. 56 размер",
           "2BSO58": "Бронешлем MK2. Безухий. Штатная комплектация. Оливковый. 58 размер",
           "2BSO60": "Бронешлем MK2. Безухий. Штатная комплектация. Оливковый. 60 размер",
           "2BMB56": "Бронешлем MK2. Безухий. МОД+ комплектация. Черный. 56 размер",
           "2BMB58": "Бронешлем MK2. Безухий. МОД+ комплектация. Черный. 58 размер",
           "2BMB60": "Бронешлем MK2. Безухий. МОД+ комплектация. Черный. 60 размер",
           "2BMS56": "Бронешлем MK2. Безухий. МОД+ комплектация. Песочный. 56 размер",
           "2BMS58": "Бронешлем MK2. Безухий. МОД+ комплектация. Песочный. 58 размер",
           "2BMS60": "Бронешлем MK2. Безухий. МОД+ комплектация. Песочный. 60 размер",
           "2BMO56": "Бронешлем MK2. Безухий. МОД+ комплектация. Оливковый. 56 размер",
           "2BMO58": "Бронешлем MK2. Безухий. МОД+ комплектация. Оливковый. 58 размер",
           "2BMO60": "Бронешлем MK2. Безухий. МОД+ комплектация. Оливковый. 60 размер",
           }

"""Функция бота по созданию использумых баз данных. Запускается при старте бота"""
def sklad_bd_start():
    global base, cur
    base = sq.connect("sklad.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS sklad(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS zakaz(img TEXT, zak TEXT, name TEXT, adres TEXT, tel TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS klient(klient TEXT, zak TEXT, name TEXT, adres TEXT, tel TEXT, time TEXT, track TEXT)')
    base.execute("CREATE TABLE IF NOT EXISTS obr(klient TEXT, text TEXT, otv TEXT)")
    base.execute("CREATE TABLE IF NOT EXISTS users(user TEXT PRIMARY KEY)")
    base.execute("CREATE TABLE IF NOT EXISTS prices(tov TEXT, price INT)")
    base.execute("CREATE TABLE IF NOT EXISTS zakazaka(id TEXT, tovar TEXT)")
    base.commit()


"""Функция бота добавляющиая уникальных пользователй в базу users"""
async def user_add(message):
    try:
        cur.execute("INSERT INTO users VALUES (?)", (message.from_user.id,))
    except:
        pass
    base.commit()

"""Админская функция, используемая для добавления нового товара в базу sklad"""
async def sklad_add(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO sklad VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()

"""Админская функция, используемая для получения информации о необработанных заказах"""
async def zakbeztrack(message):
    for ret in cur.execute(f"SELECT *, ROWID FROM klient WHERE track == 'Не отправлено'").fetchall():
        await bot.send_message(message.from_user.id, f"{ret}" )

"""Админская функция, используемая для получения информации о всех заказах"""
async def vall(message):
    for ret in cur.execute(f"SELECT *, ROWID FROM klient").fetchall():
        await bot.send_message(message.from_user.id, f"{ret}" )

"""Админская функция, используемая для получения информации о заказе по его номеру"""
async def zakpn(message, num):
    ret = cur.execute(f"SELECT * FROM klient WHERE ROWID == {num}").fetchall()
    await bot.send_message(message.from_user.id, f"{ret}" )

"""Админская функция, используемая для изменения трек номера заказа"""
async def vbittrack(num, tr):
    ret = cur.execute(f"SELECT * FROM klient WHERE ROWID == {num[0]}").fetchall()
    cur.execute(f"UPDATE klient SET track == ? WHERE ROWID == {num[0]}", (f"{tr}",))
    base.commit()
    await bot.send_message(ret[0][0], f"Изменен статус по вашему заказу от {ret[0][5]}. Трек номер: {tr}. По указанному трек номеру вы можете отследить статус доставки на официальном сайте ТК СДЭК" )

"""Админская функция, используемая для ответа на обращение"""
async def otvobr(state):
    async with state.proxy() as data:
        ret = cur.execute(f"SELECT klient, text FROM obr WHERE ROWID == {data['number']}").fetchall()
        cur.execute(f"UPDATE obr SET otv == ? WHERE ROWID == {data['number']}", (f"{data['answer']}",))
        base.commit()
        await bot.send_message(ret[0][0], f"Ответ на Ваше обращение №{data['number']}:\n{data['answer']}" )

"""Админская функция, используемая для получения информации о необработанных обращениях"""
async def obrBezOtv(message):
    for ret in cur.execute(f"SELECT *, ROWID FROM obr WHERE otv IS NULL").fetchall():
        await bot.send_message(message.from_user.id, f"{ret}" )
    print("hui")

"Клиентская функция для добавления заказа"
async def zakaz_add(state, sender):
    async with state.proxy() as data:
        track = "Не отправлено"
        dt = str(date.today())
        cur.execute("INSERT INTO zakaz VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        cur.execute("INSERT INTO klient VALUES (?, ?, ?, ?, ?, ?, ?)", (sender, data["zak"], data["name"], data["adres"], data["tel"], dt, track))
        base.commit()

"""Клиентская функция, получающая информацию о товаре"""
async def sklad_read(message):
    for ret in cur.execute(f"SELECT * FROM sklad WHERE name == '{message.text[1:]}'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f"{ret[2]}\nЦена: {ret[-1]}")

"""Клиентская функция, получающая информацию о сделанных заказах"""
async def k_story(message):
    await bot.send_message(message.from_user.id, "--------Ваши заказы---------")
    for ret in cur.execute(f"SELECT *, ROWID FROM klient WHERE klient == '{message.from_user.id}'").fetchall():
        await bot.send_message(message.from_user.id, f"Заказ №{ret[7]}: Заказан товар: {spisokT[f'{ret[1]}']}\nна имя: {ret[2]}\nна адрес: {ret[3]}\nуказанный контакт получателя: {ret[4]}\nдата заказа: {ret[5]}\nстатус/трек: {ret[6]}")
    await bot.send_message(message.from_user.id, "----------------------------")

"""Клиентская функция, используемая для создания нового обращения в базе obr"""
async def obras(message, text):
    cur.execute("INSERT INTO obr VALUES (?, ?, ?)", (message.from_user.id, text, None))
    base.commit()
    nobr = cur.execute("SELECT MAX(ROWID) FROM obr").fetchall()
    tobr = cur.execute(f"SELECT text FROM obr WHERE ROWID == {nobr[0][0]} ").fetchall()
    await bot.send_message(message.from_user.id, f'Ваше обращение зарегистрировано за №{nobr[0][0]}. Ожидайте ответа.')
    await bot.send_message(sp_adm.admin, f'Новое обращение №"{nobr[0][0]}". Текст обращения: {tobr[0][0]}')

"""Клиентская функция, используемая для изменения данных получателя"""
async def izmzak(state):
    async with state.proxy() as data:
        ret = cur.execute(f"SELECT klient, time FROM klient WHERE ROWID == {data['number']}").fetchall()
        if int(data['user']) == int(ret[0][0]):
            date_zak = list(map(int, ret[0][1].split('-')))
            if int(str(date.today() - date(date_zak[0], date_zak[1], date_zak[2])).split()[0])  <= 20:
                cur.execute(f"UPDATE klient SET name == ? WHERE ROWID == {data['number']}", (f"{data['name']}",))
                cur.execute(f"UPDATE klient SET adres == ? WHERE ROWID == {data['number']}", (f"{data['adres']}",))
                cur.execute(f"UPDATE klient SET tel == ? WHERE ROWID == {data['number']}", (f"{data['tel']}",))
                base.commit()
                await bot.send_message(data['user'], f"Данные заказа №{data['number']} изменены." )
                await bot.send_message(sp_adm.admin, f"Данные заказа №{data['number']} изменены.")
            else:
                await bot.send_message(data['user'], f"20 дней, выделенных на изменение данных по заказу №{data['number']} истекли.")
        else:
            await bot.send_message(data['user'], f"Недопустимый номер заказа")

""" Клиентрася функция для получения ценников и товаров для платежки"""
async def test_load_price(gods):
    price = cur.execute(f"SELECT price FROM prices WHERE tov == '{gods}'").fetchall()[0][0]
    return price

"""нагибаем глобальную переменную, создаем товар в базе для дальнейшего использования"""
async def put_to_base(message):
    cur.execute("INSERT INTO  zakazaka VALUES (?, ?)", (message.from_user.id, message.text[9:-1]))
    base.commit()

"""нагибаем глобальную переменную ч.2, получение товара"""
async def get_from_base(message):
    tov = cur.execute(f"SELECT tovar FROM zakazaka WHERE id == {message.from_user.id} ORDER BY ROWID DESC LIMIT 1").fetchall()[0][0]
    return tov