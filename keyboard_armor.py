
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b_start = KeyboardButton("В Начало")
b_cancel = KeyboardButton("Отмена")
b_uslovia = KeyboardButton("Условия заказа")
""" Бронеплиты в модуль kebord_armor"""
""" Делим на классы"""
b_br_3 = KeyboardButton("БР3+")
b_br_4 = KeyboardButton("БР4")
b_br_5 = KeyboardButton("БР5")
k_br_kz = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz.add(b_br_3, b_br_4, b_br_5, b_start)

"""БР3+ делим на размеры"""
b_br_3_M = KeyboardButton("M(3+)")
b_br_3_L = KeyboardButton("L(3+)")
b_br_3_EL = KeyboardButton("EL(3+)")
k_br_kz_3 = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_3.add(b_br_3_M, b_br_3_L, b_br_3_EL, b_start)
#купить БР3+M
b_br_3_М_zak = KeyboardButton("Заказать(3+M)")
k_br_kz_3_M = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_3_M.add(b_br_3_М_zak, b_uslovia).add(b_cancel).add(b_start)
#купить БР3+L
b_br_3_L_zak = KeyboardButton("Заказать(3+L)")
k_br_kz_3_L = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_3_L.add(b_br_3_L_zak, b_uslovia).add(b_cancel).add(b_start)
#купить БР3+EL
b_br_3_EL_zak = KeyboardButton("Заказать(3+EL)")
k_br_kz_3_EL = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_3_EL.add(b_br_3_EL_zak, b_uslovia).add(b_cancel).add(b_start)

"""БР4 делим на размеры"""
b_br_4_M = KeyboardButton("M(4)")
b_br_4_L = KeyboardButton("L(4)")
b_br_4_EL = KeyboardButton("EL(4)")
k_br_kz_4 = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_4.add(b_br_4_M, b_br_4_L, b_br_4_EL, b_start)
#купить БР4M
b_br_4_М_zak = KeyboardButton("Заказать(4M)")
k_br_kz_4_M = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_4_M.add(b_br_4_М_zak, b_uslovia).add(b_cancel).add(b_start)
#купить БР4L
b_br_4_L_zak = KeyboardButton("Заказать(4L)")
k_br_kz_4_L = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_4_L.add(b_br_4_L_zak, b_uslovia).add(b_cancel).add(b_start)
#купить БР4EL
b_br_4_EL_zak = KeyboardButton("Заказать(4EL)")
k_br_kz_4_EL = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_4_EL.add(b_br_4_EL_zak, b_uslovia).add(b_cancel).add(b_start)

"""БР5 делим на размеры"""
b_br_5_M = KeyboardButton("M(5)")
b_br_5_L = KeyboardButton("L(5)")
b_br_5_EL = KeyboardButton("EL(5)")
k_br_kz_5 = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_5.add(b_br_5_M, b_br_5_L, b_br_5_EL, b_start)
#купить БР5M
b_br_5_М_zak = KeyboardButton("Заказать(5M)")
k_br_kz_5_M = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_5_M.add(b_br_5_М_zak, b_uslovia).add(b_cancel).add(b_start)
#купить БР5L
b_br_5_L_zak = KeyboardButton("Заказать(5L)")
k_br_kz_5_L = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_5_L.add(b_br_5_L_zak, b_uslovia).add(b_cancel).add(b_start)
#купить БР5EL
b_br_5_EL_zak = KeyboardButton("Заказать(5EL)")
k_br_kz_5_EL = ReplyKeyboardMarkup(resize_keyboard=True)
k_br_kz_5_EL.add(b_br_5_EL_zak, b_uslovia).add(b_cancel).add(b_start)

"""#делим защиту лица на цвет
b_mk0_uh_st_b = KeyboardButton("/Черный(0YS)")
b_mk0_uh_st_s = KeyboardButton("/Песочный(0YS)")
b_mk0_uh_st_o = KeyboardButton("/Олива(0YS)")
k_mk0_uh_st = ReplyKeyboardMarkup(resize_keyboard=True)
k_mk0_uh_st.add(b_mk0_uh_st_b, b_mk0_uh_st_s, b_mk0_uh_st_o, b_start)"""

""" Заказа защиты лица"""
b_dz = KeyboardButton("Заказать(ЗЛ)")
b_dz_chehol = KeyboardButton("Test(ЗЛ)")
kb_dz = ReplyKeyboardMarkup(resize_keyboard=True)
kb_dz.row(b_dz, b_uslovia).add(b_cancel).add(b_start)
