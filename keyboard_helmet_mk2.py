from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b_start = KeyboardButton("В Начало")
b_cancel = KeyboardButton("Отмена")
b_uslovia = KeyboardButton("Условия заказа")


""" Buttons for MK2"""
#разделение на ушастый \ безухий
b_mk2_uh = KeyboardButton("Ушастый(2)")
b_mk2_bu = KeyboardButton("Безухий(2)")
k_mk2 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2.add(b_mk2_uh, b_mk2_bu, b_start)

"Ушастый--------------------------------"
#делим ушастика на комплект
b_mk2_uh_st = KeyboardButton("Штатный(2Y)")
b_mk2_uh_pl = KeyboardButton("МОД+(2Y)")
k_mk2_uh = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh.add(b_mk2_uh_st, b_mk2_uh_pl, b_start)

#делим ушастика штат на цвет
b_mk2_uh_st_b = KeyboardButton("Черный(2YS)")
b_mk2_uh_st_s = KeyboardButton("Песочный(2YS)")
b_mk2_uh_st_o = KeyboardButton("Олива(2YS)")
k_mk2_uh_st = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_st.add(b_mk2_uh_st_b, b_mk2_uh_st_s, b_mk2_uh_st_o, b_start)

#делим ушастика штат черного на размер
b_mk2_uh_st_b_56 = KeyboardButton("56(2YSB)")
b_mk2_uh_st_b_58 = KeyboardButton("58(2YSB)")
b_mk2_uh_st_b_60 = KeyboardButton("60(2YSB)")
k_mk2_uh_st_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_st_b.add(b_mk2_uh_st_b_56, b_mk2_uh_st_b_58, b_mk2_uh_st_b_60, b_start)

#кнопка заказа черного ушастика штатного 56
b_mk2_uh_b_st_56_zak = KeyboardButton("Заказать(2YSB56)")
k_mk2_uh_b_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_b_st_56.add(b_mk2_uh_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика штатного 58
b_mk2_uh_b_st_58_zak = KeyboardButton("Заказать(2YSB58)")
k_mk2_uh_b_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_b_st_58.add(b_mk2_uh_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика штатного 60
b_mk2_uh_b_st_60_zak = KeyboardButton("Заказать(2YSB60)")
k_mk2_uh_b_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_b_st_60.add(b_mk2_uh_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат песочного на размер
b_mk2_uh_st_s_56 = KeyboardButton("56(2YSS)")
b_mk2_uh_st_s_58 = KeyboardButton("58(2YSS)")
b_mk2_uh_st_s_60 = KeyboardButton("60(2YSS)")
k_mk2_uh_st_s = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_st_s.add(b_mk2_uh_st_s_56, b_mk2_uh_st_s_58, b_mk2_uh_st_s_60, b_start)

#кнопка заказа песочного ушастика штатного 56
b_mk2_uh_s_st_56_zak = KeyboardButton("Заказать(2YSS56)")
k_mk2_uh_s_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_s_st_56.add(b_mk2_uh_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика штатного 58
b_mk2_uh_s_st_58_zak = KeyboardButton("Заказать(2YSS58)")
k_mk2_uh_s_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_s_st_58.add(b_mk2_uh_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика штатного 60
b_mk2_uh_s_st_60_zak = KeyboardButton("Заказать(2YSS60)")
k_mk2_uh_s_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_s_st_60.add(b_mk2_uh_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат оливкого на размер
b_mk2_uh_st_o_56 = KeyboardButton("56(2YSO)")
b_mk2_uh_st_o_58 = KeyboardButton("58(2YSO)")
b_mk2_uh_st_o_60 = KeyboardButton("60(2YSO)")
k_mk2_uh_st_o = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_st_o.add(b_mk2_uh_st_o_56, b_mk2_uh_st_o_58, b_mk2_uh_st_o_60, b_start)

#кнопка заказа оливкого ушастика штатного 56
b_mk2_uh_o_st_56_zak = KeyboardButton("Заказать(2YSO56)")
k_mk2_uh_o_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_o_st_56.add(b_mk2_uh_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика штатного 58
b_mk2_uh_o_st_58_zak = KeyboardButton("Заказать(2YSO58)")
k_mk2_uh_o_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_o_st_58.add(b_mk2_uh_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика штатного 60
b_mk2_uh_o_st_60_zak = KeyboardButton("Заказать(2YSO60)")
k_mk2_uh_o_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_o_st_60.add(b_mk2_uh_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат на цвет
b_mk2_uh_mod_b = KeyboardButton("Черный(2YM)")
b_mk2_uh_mod_s = KeyboardButton("Песочный(2YM)")
b_mk2_uh_mod_o = KeyboardButton("Олива(2YM)")
k_mk2_uh_mod = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_mod.add(b_mk2_uh_mod_b, b_mk2_uh_mod_s, b_mk2_uh_mod_o, b_start)

#делим ушастика штат черного на размер
b_mk2_uh_mod_b_56 = KeyboardButton("56(2YMB)")
b_mk2_uh_mod_b_58 = KeyboardButton("58(2YMB)")
b_mk2_uh_mod_b_60 = KeyboardButton("60(2YMB)")
k_mk2_uh_mod_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_mod_b.add(b_mk2_uh_mod_b_56, b_mk2_uh_mod_b_58, b_mk2_uh_mod_b_60, b_start)

#кнопка заказа черного ушастика МОД+ого 56
b_mk2_uh_b_mod_56_zak = KeyboardButton("Заказать(2YMB56)")
k_mk2_uh_b_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_b_mod_56.add(b_mk2_uh_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика МОД+ого 58
b_mk2_uh_b_mod_58_zak = KeyboardButton("Заказать(2YMB58)")
k_mk2_uh_b_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_b_mod_58.add(b_mk2_uh_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика МОД+ого 60
b_mk2_uh_b_mod_60_zak = KeyboardButton("Заказать(2YMB60)")
k_mk2_uh_b_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_b_mod_60.add(b_mk2_uh_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат песочного на размер
b_mk2_uh_mod_s_56 = KeyboardButton("56(2YMS)")
b_mk2_uh_mod_s_58 = KeyboardButton("58(2YMS)")
b_mk2_uh_mod_s_60 = KeyboardButton("60(2YMS)")
k_mk2_uh_mod_s = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_mod_s.add(b_mk2_uh_mod_s_56, b_mk2_uh_mod_s_58, b_mk2_uh_mod_s_60, b_start)

#кнопка заказа песочного ушастика МОД+ого 56
b_mk2_uh_s_mod_56_zak = KeyboardButton("Заказать(2YMS56)")
k_mk2_uh_s_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_s_mod_56.add(b_mk2_uh_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика МОД+ого 58
b_mk2_uh_s_mod_58_zak = KeyboardButton("Заказать(2YMS58)")
k_mk2_uh_s_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_s_mod_58.add(b_mk2_uh_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика МОД+ого 60
b_mk2_uh_s_mod_60_zak = KeyboardButton("Заказать(2YMS60)")
k_mk2_uh_s_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_s_mod_60.add(b_mk2_uh_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат оливкого на размер
b_mk2_uh_mod_o_56 = KeyboardButton("56(2YMO)")
b_mk2_uh_mod_o_58 = KeyboardButton("58(2YMO)")
b_mk2_uh_mod_o_60 = KeyboardButton("60(2YMO)")
k_mk2_uh_mod_o = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_mod_o.add(b_mk2_uh_mod_o_56, b_mk2_uh_mod_o_58, b_mk2_uh_mod_o_60, b_start)

#кнопка заказа оливкого ушастика МОД+ого 56
b_mk2_uh_o_mod_56_zak = KeyboardButton("Заказать(2YMO56)")
k_mk2_uh_o_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_o_mod_56.add(b_mk2_uh_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика МОД+ого 58
b_mk2_uh_o_mod_58_zak = KeyboardButton("Заказать(2YMO58)")
k_mk2_uh_o_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_o_mod_58.add(b_mk2_uh_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика МОД+ого 60
b_mk2_uh_o_mod_60_zak = KeyboardButton("Заказать(2YMO60)")
k_mk2_uh_o_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_uh_o_mod_60.add(b_mk2_uh_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

"Безушастый--------------------------------"
#делим ушастика на комплект
b_mk2_bu_st = KeyboardButton("Штатный(2B)")
b_mk2_bu_pl = KeyboardButton("МОД+(2B)")
k_mk2_bu = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu.add(b_mk2_bu_st, b_mk2_bu_pl, b_start)

#делим ушастика штат на цвет
b_mk2_bu_st_b = KeyboardButton("Черный(2BS)")
b_mk2_bu_st_s = KeyboardButton("Песочный(2BS)")
b_mk2_bu_st_o = KeyboardButton("Олива(2BS)")
k_mk2_bu_st = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_st.add(b_mk2_bu_st_b, b_mk2_bu_st_s, b_mk2_bu_st_o, b_start)

#делим ушастика штат черного на размер
b_mk2_bu_st_b_56 = KeyboardButton("56(2BSB)")
b_mk2_bu_st_b_58 = KeyboardButton("58(2BSB)")
b_mk2_bu_st_b_60 = KeyboardButton("60(2BSB)")
k_mk2_bu_st_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_st_b.add(b_mk2_bu_st_b_56, b_mk2_bu_st_b_58, b_mk2_bu_st_b_60, b_start)

#кнопка заказа черного ушастика штатного 56
b_mk2_bu_b_st_56_zak = KeyboardButton("Заказать(2BSB56)")
k_mk2_bu_b_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_b_st_56.add(b_mk2_bu_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика штатного 58
b_mk2_bu_b_st_58_zak = KeyboardButton("Заказать(2BSB58)")
k_mk2_bu_b_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_b_st_58.add(b_mk2_bu_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика штатного 60
b_mk2_bu_b_st_60_zak = KeyboardButton("Заказать(2BSB60)")
k_mk2_bu_b_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_b_st_60.add(b_mk2_bu_b_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат песочного на размер
b_mk2_bu_st_s_56 = KeyboardButton("56(2BSS)")
b_mk2_bu_st_s_58 = KeyboardButton("58(2BSS)")
b_mk2_bu_st_s_60 = KeyboardButton("60(2BSS)")
k_mk2_bu_st_s = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_st_s.add(b_mk2_bu_st_s_56, b_mk2_bu_st_s_58, b_mk2_bu_st_s_60, b_start)

#кнопка заказа песочного ушастика штатного 56
b_mk2_bu_s_st_56_zak = KeyboardButton("Заказать(2BSS56)")
k_mk2_bu_s_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_s_st_56.add(b_mk2_bu_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика штатного 58
b_mk2_bu_s_st_58_zak = KeyboardButton("Заказать(2BSS58)")
k_mk2_bu_s_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_s_st_58.add(b_mk2_bu_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика штатного 60
b_mk2_bu_s_st_60_zak = KeyboardButton("Заказать(2BSS60)")
k_mk2_bu_s_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_s_st_60.add(b_mk2_bu_s_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат оливкого на размер
b_mk2_bu_st_o_56 = KeyboardButton("56(2BSO)")
b_mk2_bu_st_o_58 = KeyboardButton("58(2BSO)")
b_mk2_bu_st_o_60 = KeyboardButton("60(2BSO)")
k_mk2_bu_st_o = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_st_o.add(b_mk2_bu_st_o_56, b_mk2_bu_st_o_58, b_mk2_bu_st_o_60, b_start)

#кнопка заказа оливкого ушастика штатного 56
b_mk2_bu_o_st_56_zak = KeyboardButton("Заказать(2BSO56)")
k_mk2_bu_o_st_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_o_st_56.add(b_mk2_bu_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика штатного 58
b_mk2_bu_o_st_58_zak = KeyboardButton("Заказать(2BSO58)")
k_mk2_bu_o_st_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_o_st_58.add(b_mk2_bu_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика штатного 60
b_mk2_bu_o_st_60_zak = KeyboardButton("Заказать(2BSO60)")
k_mk2_bu_o_st_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_o_st_60.add(b_mk2_bu_o_st_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат на цвет
b_mk2_bu_mod_b = KeyboardButton("Черный(2BM)")
b_mk2_bu_mod_s = KeyboardButton("Песочный(2BM)")
b_mk2_bu_mod_o = KeyboardButton("Олива(2BM)")
k_mk2_bu_mod = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_mod.add(b_mk2_bu_mod_b, b_mk2_bu_mod_s, b_mk2_bu_mod_o, b_start)

#делим ушастика штат черного на размер
b_mk2_bu_mod_b_56 = KeyboardButton("56(2BMB)")
b_mk2_bu_mod_b_58 = KeyboardButton("58(2BMB)")
b_mk2_bu_mod_b_60 = KeyboardButton("60(2BMB)")
k_mk2_bu_mod_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_mod_b.add(b_mk2_bu_mod_b_56, b_mk2_bu_mod_b_58, b_mk2_bu_mod_b_60, b_start)

#кнопка заказа черного ушастика МОД+ого 56
b_mk2_bu_b_mod_56_zak = KeyboardButton("Заказать(2BMB56)")
k_mk2_bu_b_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_b_mod_56.add(b_mk2_bu_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика МОД+ого 58
b_mk2_bu_b_mod_58_zak = KeyboardButton("Заказать(2BMB58)")
k_mk2_bu_b_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_b_mod_58.add(b_mk2_bu_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа черного ушастика МОД+ого 60
b_mk2_bu_b_mod_60_zak = KeyboardButton("Заказать(2BMB60)")
k_mk2_bu_b_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_b_mod_60.add(b_mk2_bu_b_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат песочного на размер
b_mk2_bu_mod_s_56 = KeyboardButton("56(2BMS)")
b_mk2_bu_mod_s_58 = KeyboardButton("58(2BMS)")
b_mk2_bu_mod_s_60 = KeyboardButton("60(2BMS)")
k_mk2_bu_mod_s = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_mod_s.add(b_mk2_bu_mod_s_56, b_mk2_bu_mod_s_58, b_mk2_bu_mod_s_60, b_start)

#кнопка заказа песочного ушастика МОД+ого 56
b_mk2_bu_s_mod_56_zak = KeyboardButton("Заказать(2BMS56)")
k_mk2_bu_s_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_s_mod_56.add(b_mk2_bu_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика МОД+ого 58
b_mk2_bu_s_mod_58_zak = KeyboardButton("Заказать(2BMS58)")
k_mk2_bu_s_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_s_mod_58.add(b_mk2_bu_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа песочного ушастика МОД+ого 60
b_mk2_bu_s_mod_60_zak = KeyboardButton("Заказать(2BMS60)")
k_mk2_bu_s_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_s_mod_60.add(b_mk2_bu_s_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)

#делим ушастика штат оливкого на размер
b_mk2_bu_mod_o_56 = KeyboardButton("56(2BMO)")
b_mk2_bu_mod_o_58 = KeyboardButton("58(2BMO)")
b_mk2_bu_mod_o_60 = KeyboardButton("60(2BMO)")
k_mk2_bu_mod_o = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_mod_o.add(b_mk2_bu_mod_o_56, b_mk2_bu_mod_o_58, b_mk2_bu_mod_o_60, b_start)

#кнопка заказа оливкого ушастика МОД+ого 56
b_mk2_bu_o_mod_56_zak = KeyboardButton("Заказать(2BMO56)")
k_mk2_bu_o_mod_56 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_o_mod_56.add(b_mk2_bu_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика МОД+ого 58
b_mk2_bu_o_mod_58_zak = KeyboardButton("Заказать(2BMO58)")
k_mk2_bu_o_mod_58 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_o_mod_58.add(b_mk2_bu_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
#кнопка заказа оливкого ушастика МОД+ого 60
b_mk2_bu_o_mod_60_zak = KeyboardButton("Заказать(2BMO60)")
k_mk2_bu_o_mod_60 = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk2_bu_o_mod_60.add(b_mk2_bu_o_mod_56_zak, b_uslovia).add(b_cancel).add(b_start)
