from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b_start = KeyboardButton("/ВНачало")
b_cancel = KeyboardButton("Отмена")
b_uslovia = KeyboardButton("/Условия_заказа")
"""Экран Шлемаки разделение на две категории"""
b_mk0 = KeyboardButton("/MK0")
b_mk2 = KeyboardButton("/MK2")
kb_mk = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mk.row(b_mk0, b_mk2, b_start)

""" Buttons for MKO"""
#разделение на ушастый \ безухий
b_mk0_uh = KeyboardButton("/Ушастый(0)")
b_mk0_bu = KeyboardButton("/Безухий(0)")
k_mk0 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0.add(b_mk0_uh, b_mk0_bu, b_start)

"Ушастый--------------------------------"
#делим ушастика на комплект
b_mk0_uh_st = KeyboardButton("/Штатный(0Y)")
b_mk0_uh_pl = KeyboardButton("/МОД+(0Y)")
k_mk0_uh = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh.add(b_mk0_uh_st, b_mk0_uh_pl, b_start)

#делим ушастика штат на цвет
b_mk0_uh_st_b = KeyboardButton("/Черный(0YS)")
b_mk0_uh_st_s = KeyboardButton("/Песочный(0YS)")
b_mk0_uh_st_o = KeyboardButton("/Олива(0YS)")
k_mk0_uh_st = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_st.add(b_mk0_uh_st_b, b_mk0_uh_st_s, b_mk0_uh_st_o, b_start)

#делим ушастика штат черного на размер
b_mk0_uh_st_b_56 = KeyboardButton("/56(0YSB)")
b_mk0_uh_st_b_58 = KeyboardButton("/58(0YSB)")
b_mk0_uh_st_b_60 = KeyboardButton("/60(0YSB)")
k_mk0_uh_st_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_st_b.add(b_mk0_uh_st_b_56, b_mk0_uh_st_b_58, b_mk0_uh_st_b_60, b_start)

#кнопка заказа черного ушастика штатного 56
b_mk0_uh_b_st_56_zak = KeyboardButton("/Заказать(0YSB56)")
k_mk0_uh_b_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_b_st_56.add(b_mk0_uh_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика штатного 58
b_mk0_uh_b_st_58_zak = KeyboardButton("/Заказать(0YSB58)")
k_mk0_uh_b_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_b_st_58.add(b_mk0_uh_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика штатного 60
b_mk0_uh_b_st_60_zak = KeyboardButton("/Заказать(0YSB60)")
k_mk0_uh_b_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_b_st_60.add(b_mk0_uh_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат песочного на размер
b_mk0_uh_st_s_56 = KeyboardButton("/56(0YSS)")
b_mk0_uh_st_s_58 = KeyboardButton("/58(0YSS)")
b_mk0_uh_st_s_60 = KeyboardButton("/60(0YSS)")
k_mk0_uh_st_s = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_st_s.add(b_mk0_uh_st_s_56, b_mk0_uh_st_s_58, b_mk0_uh_st_s_60, b_start)

#кнопка заказа песочного ушастика штатного 56
b_mk0_uh_s_st_56_zak = KeyboardButton("/Заказать(0YSS56)")
k_mk0_uh_s_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_s_st_56.add(b_mk0_uh_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика штатного 58
b_mk0_uh_s_st_58_zak = KeyboardButton("/Заказать(0YSS58)")
k_mk0_uh_s_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_s_st_58.add(b_mk0_uh_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика штатного 60
b_mk0_uh_s_st_60_zak = KeyboardButton("/Заказать(0YSS60)")
k_mk0_uh_s_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_s_st_60.add(b_mk0_uh_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат оливкого на размер
b_mk0_uh_st_o_56 = KeyboardButton("/56(0YSO)")
b_mk0_uh_st_o_58 = KeyboardButton("/58(0YSO)")
b_mk0_uh_st_o_60 = KeyboardButton("/60(0YSO)")
k_mk0_uh_st_o = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_st_o.add(b_mk0_uh_st_o_56, b_mk0_uh_st_o_58, b_mk0_uh_st_o_60, b_start)

#кнопка заказа оливкого ушастика штатного 56
b_mk0_uh_o_st_56_zak = KeyboardButton("/Заказать(0YSO56)")
k_mk0_uh_o_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_o_st_56.add(b_mk0_uh_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика штатного 58
b_mk0_uh_o_st_58_zak = KeyboardButton("/Заказать(0YSO58)")
k_mk0_uh_o_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_o_st_58.add(b_mk0_uh_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика штатного 60
b_mk0_uh_o_st_60_zak = KeyboardButton("/Заказать(0YSO60)")
k_mk0_uh_o_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_o_st_60.add(b_mk0_uh_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат на цвет
b_mk0_uh_mod_b = KeyboardButton("/Черный(0YM)")
b_mk0_uh_mod_s = KeyboardButton("/Песочный(0YM)")
b_mk0_uh_mod_o = KeyboardButton("/Олива(0YM)")
k_mk0_uh_mod = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_mod.add(b_mk0_uh_mod_b, b_mk0_uh_mod_s, b_mk0_uh_mod_o, b_start)

#делим ушастика штат черного на размер
b_mk0_uh_mod_b_56 = KeyboardButton("/56(0YMB)")
b_mk0_uh_mod_b_58 = KeyboardButton("/58(0YMB)")
b_mk0_uh_mod_b_60 = KeyboardButton("/60(0YMB)")
k_mk0_uh_mod_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_mod_b.add(b_mk0_uh_mod_b_56, b_mk0_uh_mod_b_58, b_mk0_uh_mod_b_60, b_start)

#кнопка заказа черного ушастика МОД+ого 56
b_mk0_uh_b_mod_56_zak = KeyboardButton("/Заказать(0YMB56)")
k_mk0_uh_b_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_b_mod_56.add(b_mk0_uh_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика МОД+ого 58
b_mk0_uh_b_mod_58_zak = KeyboardButton("/Заказать(0YMB58)")
k_mk0_uh_b_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_b_mod_58.add(b_mk0_uh_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика МОД+ого 60
b_mk0_uh_b_mod_60_zak = KeyboardButton("/Заказать(0YMB60)")
k_mk0_uh_b_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_b_mod_60.add(b_mk0_uh_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат песочного на размер
b_mk0_uh_mod_s_56 = KeyboardButton("/56(0YMS)")
b_mk0_uh_mod_s_58 = KeyboardButton("/58(0YMS)")
b_mk0_uh_mod_s_60 = KeyboardButton("/60(0YMS)")
k_mk0_uh_mod_s = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_mod_s.add(b_mk0_uh_mod_s_56, b_mk0_uh_mod_s_58, b_mk0_uh_mod_s_60, b_start)

#кнопка заказа песочного ушастика МОД+ого 56
b_mk0_uh_s_mod_56_zak = KeyboardButton("/Заказать(0YMS56)")
k_mk0_uh_s_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_s_mod_56.add(b_mk0_uh_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика МОД+ого 58
b_mk0_uh_s_mod_58_zak = KeyboardButton("/Заказать(0YMS58)")
k_mk0_uh_s_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_s_mod_58.add(b_mk0_uh_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика МОД+ого 60
b_mk0_uh_s_mod_60_zak = KeyboardButton("/Заказать(0YMS60)")
k_mk0_uh_s_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_s_mod_60.add(b_mk0_uh_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат оливкого на размер
b_mk0_uh_mod_o_56 = KeyboardButton("/56(0YMO)")
b_mk0_uh_mod_o_58 = KeyboardButton("/58(0YMO)")
b_mk0_uh_mod_o_60 = KeyboardButton("/60(0YMO)")
k_mk0_uh_mod_o = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_mod_o.add(b_mk0_uh_mod_o_56, b_mk0_uh_mod_o_58, b_mk0_uh_mod_o_60, b_start)

#кнопка заказа оливкого ушастика МОД+ого 56
b_mk0_uh_o_mod_56_zak = KeyboardButton("/Заказать(0YMO56)")
k_mk0_uh_o_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_o_mod_56.add(b_mk0_uh_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика МОД+ого 58
b_mk0_uh_o_mod_58_zak = KeyboardButton("/Заказать(0YMO58)")
k_mk0_uh_o_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_o_mod_58.add(b_mk0_uh_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика МОД+ого 60
b_mk0_uh_o_mod_60_zak = KeyboardButton("/Заказать(0YMO60)")
k_mk0_uh_o_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_o_mod_60.add(b_mk0_uh_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

"Безушастый--------------------------------"
#делим ушастика на комплект
b_mk0_bu_st = KeyboardButton("/Штатный(0B)")
b_mk0_bu_pl = KeyboardButton("/МОД+(0B)")
k_mk0_bu = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu.add(b_mk0_bu_st, b_mk0_bu_pl, b_start)

#делим ушастика штат на цвет
b_mk0_bu_st_b = KeyboardButton("/Черный(0BS)")
b_mk0_bu_st_s = KeyboardButton("/Песочный(0BS)")
b_mk0_bu_st_o = KeyboardButton("/Олива(0BS)")
k_mk0_bu_st = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_st.add(b_mk0_bu_st_b, b_mk0_bu_st_s, b_mk0_bu_st_o, b_start)

#делим ушастика штат черного на размер
b_mk0_bu_st_b_56 = KeyboardButton("/56(0BSB)")
b_mk0_bu_st_b_58 = KeyboardButton("/58(0BSB)")
b_mk0_bu_st_b_60 = KeyboardButton("/60(0BSB)")
k_mk0_bu_st_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_st_b.add(b_mk0_bu_st_b_56, b_mk0_bu_st_b_58, b_mk0_bu_st_b_60, b_start)

#кнопка заказа черного ушастика штатного 56
b_mk0_bu_b_st_56_zak = KeyboardButton("/Заказать(0BSB56)")
k_mk0_bu_b_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_b_st_56.add(b_mk0_bu_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика штатного 58
b_mk0_bu_b_st_58_zak = KeyboardButton("/Заказать(0BSB58)")
k_mk0_bu_b_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_b_st_58.add(b_mk0_bu_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика штатного 60
b_mk0_bu_b_st_60_zak = KeyboardButton("/Заказать(0BSB60)")
k_mk0_bu_b_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_b_st_60.add(b_mk0_bu_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат песочного на размер
b_mk0_bu_st_s_56 = KeyboardButton("/56(0BSS)")
b_mk0_bu_st_s_58 = KeyboardButton("/58(0BSS)")
b_mk0_bu_st_s_60 = KeyboardButton("/60(0BSS)")
k_mk0_bu_st_s = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_st_s.add(b_mk0_bu_st_s_56, b_mk0_bu_st_s_58, b_mk0_bu_st_s_60, b_start)

#кнопка заказа песочного ушастика штатного 56
b_mk0_bu_s_st_56_zak = KeyboardButton("/Заказать(0BSS56)")
k_mk0_bu_s_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_s_st_56.add(b_mk0_bu_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика штатного 58
b_mk0_bu_s_st_58_zak = KeyboardButton("/Заказать(0BSS58)")
k_mk0_bu_s_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_s_st_58.add(b_mk0_bu_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика штатного 60
b_mk0_bu_s_st_60_zak = KeyboardButton("/Заказать(0BSS60)")
k_mk0_bu_s_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_s_st_60.add(b_mk0_bu_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат оливкого на размер
b_mk0_bu_st_o_56 = KeyboardButton("/56(0BSO)")
b_mk0_bu_st_o_58 = KeyboardButton("/58(0BSO)")
b_mk0_bu_st_o_60 = KeyboardButton("/60(0BSO)")
k_mk0_bu_st_o = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_st_o.add(b_mk0_bu_st_o_56, b_mk0_bu_st_o_58, b_mk0_bu_st_o_60, b_start)

#кнопка заказа оливкого ушастика штатного 56
b_mk0_bu_o_st_56_zak = KeyboardButton("/Заказать(0BSO56)")
k_mk0_bu_o_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_o_st_56.add(b_mk0_bu_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика штатного 58
b_mk0_bu_o_st_58_zak = KeyboardButton("/Заказать(0BSO58)")
k_mk0_bu_o_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_o_st_58.add(b_mk0_bu_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика штатного 60
b_mk0_bu_o_st_60_zak = KeyboardButton("/Заказать(0BSO60)")
k_mk0_bu_o_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_o_st_60.add(b_mk0_bu_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат на цвет
b_mk0_bu_mod_b = KeyboardButton("/Черный(0BM)")
b_mk0_bu_mod_s = KeyboardButton("/Песочный(0BM)")
b_mk0_bu_mod_o = KeyboardButton("/Олива(0BM)")
k_mk0_bu_mod = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_mod.add(b_mk0_bu_mod_b, b_mk0_bu_mod_s, b_mk0_bu_mod_o, b_start)

#делим ушастика штат черного на размер
b_mk0_bu_mod_b_56 = KeyboardButton("/56(0BMB)")
b_mk0_bu_mod_b_58 = KeyboardButton("/58(0BMB)")
b_mk0_bu_mod_b_60 = KeyboardButton("/60(0BMB)")
k_mk0_bu_mod_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_mod_b.add(b_mk0_bu_mod_b_56, b_mk0_bu_mod_b_58, b_mk0_bu_mod_b_60, b_start)

#кнопка заказа черного ушастика МОД+ого 56
b_mk0_bu_b_mod_56_zak = KeyboardButton("/Заказать(0BMB56)")
k_mk0_bu_b_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_b_mod_56.add(b_mk0_bu_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика МОД+ого 58
b_mk0_bu_b_mod_58_zak = KeyboardButton("/Заказать(0BMB58)")
k_mk0_bu_b_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_b_mod_58.add(b_mk0_bu_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика МОД+ого 60
b_mk0_bu_b_mod_60_zak = KeyboardButton("/Заказать(0BMB60)")
k_mk0_bu_b_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_b_mod_60.add(b_mk0_bu_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат песочного на размер
b_mk0_bu_mod_s_56 = KeyboardButton("/56(0BMS)")
b_mk0_bu_mod_s_58 = KeyboardButton("/58(0BMS)")
b_mk0_bu_mod_s_60 = KeyboardButton("/60(0BMS)")
k_mk0_bu_mod_s = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_mod_s.add(b_mk0_bu_mod_s_56, b_mk0_bu_mod_s_58, b_mk0_bu_mod_s_60, b_start)

#кнопка заказа песочного ушастика МОД+ого 56
b_mk0_bu_s_mod_56_zak = KeyboardButton("/Заказать(0BMS56)")
k_mk0_bu_s_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_s_mod_56.add(b_mk0_bu_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика МОД+ого 58
b_mk0_bu_s_mod_58_zak = KeyboardButton("/Заказать(0BMS58)")
k_mk0_bu_s_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_s_mod_58.add(b_mk0_bu_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика МОД+ого 60
b_mk0_bu_s_mod_60_zak = KeyboardButton("/Заказать(0BMS60)")
k_mk0_bu_s_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_s_mod_60.add(b_mk0_bu_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат оливкого на размер
b_mk0_bu_mod_o_56 = KeyboardButton("/56(0BMO)")
b_mk0_bu_mod_o_58 = KeyboardButton("/58(0BMO)")
b_mk0_bu_mod_o_60 = KeyboardButton("/60(0BMO)")
k_mk0_bu_mod_o = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_mod_o.add(b_mk0_bu_mod_o_56, b_mk0_bu_mod_o_58, b_mk0_bu_mod_o_60, b_start)

#кнопка заказа оливкого ушастика МОД+ого 56
b_mk0_bu_o_mod_56_zak = KeyboardButton("/Заказать(0BMO56)")
k_mk0_bu_o_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_o_mod_56.add(b_mk0_bu_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика МОД+ого 58
b_mk0_bu_o_mod_58_zak = KeyboardButton("/Заказать(0BMO58)")
k_mk0_bu_o_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_o_mod_58.add(b_mk0_bu_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика МОД+ого 60
b_mk0_bu_o_mod_60_zak = KeyboardButton("/Заказать(0BMO60)")
k_mk0_bu_o_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_bu_o_mod_60.add(b_mk0_bu_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
