from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b_start = KeyboardButton("В Начало")
b_cancel = KeyboardButton("Отмена")
b_uslovia = KeyboardButton("Условия_заказа")
""" Главный экран после старта"""
bz = KeyboardButton("Розница")
bf = KeyboardButton("FAQ")
bo = KeyboardButton("Для оптовых заказов")
bok = KeyboardButton("О компании АТЛАС")
bovt = KeyboardButton("Обратиться в поддержку")
kb_client_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_main.row(bz, bf).add(bo).row(bovt).add(bok)

""" Раздел заказов"""
b1 = KeyboardButton("Шлемы")
b2 = KeyboardButton("Бронеплиты")
b3 = KeyboardButton("Дополнительная Защита")
b4 = KeyboardButton("Мои Заказы")
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b2).add(b3).row(b4, b_start)
b5 = KeyboardButton("Изменить Данные Получателя")
kb_client_izmzak = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_izmzak.row(b5).row(b_cancel).row(b_start)
"для админа"
b_adm_zagr = KeyboardButton("/загрузить")
b_adm_vs = KeyboardButton("/выгрузитьвсе")
b_adm_zbt = KeyboardButton("/безтрека")
b_adm_zpn = KeyboardButton("/заказпономеру")
b_adm_vtn = KeyboardButton("/вбитьтрекномер")
b_adm_obr = KeyboardButton("/обращения")
kb_adm_zagr = ReplyKeyboardMarkup(resize_keyboard=True)
kb_adm_zagr.row(b_adm_zagr, b_adm_zbt, b_adm_zpn).row(b_adm_vs).row(b_adm_vtn).row(b_start)
kb_adm_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_adm_main.row(bz).row(b_adm_obr).row(b_start)

b_adm_otvobr = KeyboardButton("/ответить_на_обращение")
b_adm_obrbn = KeyboardButton("/обращения_без_ответа")
kb_adm_obr = ReplyKeyboardMarkup(resize_keyboard=True)
kb_adm_obr.row(b_adm_otvobr).row(b_adm_obrbn).row(b_start)


b_start = KeyboardButton("В Начало")
k_c_obr = ReplyKeyboardMarkup(resize_keyboard=True)
k_c_obr.add(b_cancel).add(b_start)





