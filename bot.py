from aiogram.utils import executor

import sp_adm
from create_bot import dp, bot, pay_token
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboard_main import *
from keyboard_helmet_mk0 import *
from keyboard_helmet_mk2 import *
import string
from keyboard_armor import *
from data_base import sklad
from admin import *
from client import *
from pay_test import *



async def on_startup(_):
    print("Папа в здании")
    sklad.sklad_bd_start()


@dp.message_handler(commands=['start'])
@dp.message_handler(Text(equals=['start', 'старт', "В Начало"]))
async def start_window(message: types.Message):
    if message.from_user.id == sp_adm.admin:
        await bot.send_message(message.from_user.id, 'Выберите интересующую вас категорию', reply_markup = kb_adm_main)
    else:
        await bot.send_message(message.from_user.id, 'Выберите интересующую вас категорию', reply_markup = kb_client_main)
    await sklad.user_add(message)
    await message.delete()

@dp.message_handler(Text(equals=["Условия заказа"]))
async def start_window(message: types.Message):
    await bot.send_message(message.from_user.id, 'Доставка осуществляется через офисы компании СДЭК по территории РФ. '
                                                 'Заказы на территорию ближнего зарубежья обсуждаются в отдельном порядке. Доставка на территорию недружественных государств не осуществляется. '
                                                 'Время доставки - 45 рабочих дней (реалии проведения СВО).')
    await message.delete()

@dp.message_handler(Text(equals=["Для оптовых заказов"]))
async def opt(message: types.Message):
    await bot.send_message(message.from_user.id, 'Оптовые заказы товаров компании АТЛАС осуществляются по номеру 89234127626')
    await message.delete()

@dp.message_handler(Text(equals=["О компании АТЛАС"]))
async def opt(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы разрабатываем из производим серийно:\n- Бронешлемы из СВМПЭ \
    и композитных материалов;\n- Анатомические СВМПЭ бронепластины и бронеплиты начиная с БР1 класса, а так же \
    повышенной бронестойкости Бр5, Бр6 на основе СВМПЭ с использованием керамики.\n\
    Благодаря собственному конструкторскому отделу и новым методам обработки материалов, вес снижен по сравнению \
    с аналогичными изделиями других производителей, что позволяет представить на отечественном рынке изделия мирового уровня. \n\
    Являемся официальными представителями RATNIK-TACTICAL и Ars Arma в Сибири! \n\
    Осуществляем пересыл продукции в любую точку СНГ и мира. \n\
    Контакты: https://vk.com/atlas_armor \n\
    Пискунов Никита - исполнительный директор \n\
    Сотрудничество \n\
    +7 923 412 76 26\n\
    https://vk.com/id113127385\n\
    client@atlas-gear.ru\n\
    Представитель в Москве по оптовым закзам:\n\
    Балясов Дмитрий Сергеевич\n\
    +7 925 514 71 87\n\
    5147187@mail.ru')
    await message.delete()

""" В данном разделе идет бок по товарам
________________________________________"""
@dp.message_handler(Text(equals=["Розница"]))
async def opt(message: types.Message):
    if message.from_user.id == sp_adm.admin:
        await bot.send_message(message.from_user.id, 'Братан, грузи, правь', reply_markup=kb_adm_zagr)
    else:
        await bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup = kb_client)
    await message.delete()


""" Шлемаки
_____________________________________________________________"""
@dp.message_handler(Text(equals=["Мои Заказы"]))
async def my_zaks(message: types.Message):
    await message.delete()
    await sklad.k_story(message)
    await bot.send_message(message.from_user.id, "В случаем необходимости изменения контактных данных получателя, \
    адреса получения заказа нажмите кнопку 'Изменить данные получателя' (доступно в течении 20 дней от даты создания заказа)", reply_markup=kb_client_izmzak)


@dp.message_handler(Text(equals=["Шлемы"]))
async def helmet(message: types.Message):
    await message.delete()
    await sklad.sklad_read(message)
    await bot.send_message(message.from_user.id, 'Выберите модель ', reply_markup = kb_mk)



    @dp.message_handler(Text(equals=["MK0"]))
    async def helmet(message: types.Message):
        await bot.send_message(message.from_user.id, 'Выберите форму ', reply_markup=k_mk0)
        await message.delete()

        @dp.message_handler(Text(equals=["Ушастый(0)"]))
        async def helmet(message: types.Message):
            await sklad.sklad_read(message)
            await bot.send_message(message.from_user.id, 'Выберите комплектацию ', reply_markup = k_mk0_uh)
            await message.delete()



            @dp.message_handler(Text(equals=["Штатный(0Y)"]))
            async def helmet(message: types.Message):
                await sklad.sklad_read(message)
                await bot.send_message(message.from_user.id, 'Выберите цвет', reply_markup=k_mk0_uh_st)
                await message.delete()


                @dp.message_handler(Text(equals=["Черный(0YS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_uh_st_b)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0YSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 черный Ушастый, штатная комплектация, 56 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_uh_b_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSB56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0YSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 черный Ушастый, штатная комплектация, 58 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_b_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSB58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                    @dp.message_handler(Text(equals=["60(0YSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 черный Ушастый, штатная комплектация, 60 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_b_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSB60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                @dp.message_handler(Text(equals=["Песочный(0YS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_uh_st_s)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0YSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 Песочный Ушастый, штатная комплектация, 56 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_uh_s_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSS56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0YSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Песочный Ушастый, штатная комплектация, 58 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_s_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSS58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0YSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Песочный Ушастый, штатная комплектация, 60 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_s_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSS60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Олива(0YS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_uh_st_o)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0YSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 Олива Ушастый, штатная комплектация, 56 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_uh_o_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSO56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0YSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Олива Ушастый, штатная комплектация, 58 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_o_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSO58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0YSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Олива Ушастый, штатная комплектация, 60 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_o_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YSO60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


            @dp.message_handler(Text(equals=["МОД+(0Y)"]))
            async def helmet(message: types.Message):
                await sklad.sklad_read(message)
                await bot.send_message(message.from_user.id, 'Выберите цвет', reply_markup=k_mk0_uh_mod)
                await message.delete()


                @dp.message_handler(Text(equals=["Черный(0YM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_uh_mod_b)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0YMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 черный Ушастый, МОД+ комплектация, 56 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_uh_b_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMB56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0YMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 черный Ушастый, МОД+ комплектация, 58 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_b_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMB58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                    @dp.message_handler(Text(equals=["60(0YMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 черный Ушастый, МОД+ комплектация, 60 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_b_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMB60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                @dp.message_handler(Text(equals=["Песочный(0YM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_uh_mod_s)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0YMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 Песочный Ушастый, МОД+ комплектация, 56 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_uh_s_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMS56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0YMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Песочный Ушастый, МОД+ комплектация, 58 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_s_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMS58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0YMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Песочный Ушастый, МОД+ комплектация, 60 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_s_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMS60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Олива(0YM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_uh_mod_o)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0YMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 Олива Ушастый, МОД+ комплектация, 56 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_uh_o_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMO56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0YMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Олива Ушастый, МОД+ комплектация, 58 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_o_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMO58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                    @dp.message_handler(Text(equals=["60(0YMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Олива Ушастый, МОД+ комплектация, 60 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_uh_o_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0YMO60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()



        @dp.message_handler(Text(equals=["Безухий(0)"]))
        async def helmet(message: types.Message):
            await sklad.sklad_read(message)
            await bot.send_message(message.from_user.id, 'Выберите комплектацию ', reply_markup = k_mk0_bu)
            await message.delete()


            @dp.message_handler(Text(equals=["Штатный(0B)"]))
            async def helmet(message: types.Message):
                await sklad.sklad_read(message)
                await bot.send_message(message.from_user.id, 'Выберите цвет', reply_markup=k_mk0_bu_st)
                await message.delete()


                @dp.message_handler(Text(equals=["Черный(0BS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_bu_st_b)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0BSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 черный безухий, штатная комплектация, 56 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_bu_b_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSB56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0BSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 черный безухий, штатная комплектация, 58 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_b_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSB58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0BSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 черный безухий, штатная комплектация, 60 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_b_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSB60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                @dp.message_handler(Text(equals=["Песочный(0BS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_bu_st_s)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0BSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 Песочный безухий, штатная комплектация, 56 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_bu_s_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSS56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0BSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Песочный безухий, штатная комплектация, 58 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_s_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSS58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0BSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Песочный безухий, штатная комплектация, 60 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_s_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSS60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Олива(0BS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_bu_st_o)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0BSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 Олива безухий, штатная комплектация, 56 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_bu_o_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSO56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0BSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Олива безухий, штатная комплектация, 58 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_o_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSO58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0BSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Олива безухий, штатная комплектация, 60 размер. Стоимость 47550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_o_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BSO60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


            @dp.message_handler(Text(equals=["МОД+(0B)"]))
            async def helmet(message: types.Message):
                await bot.send_message(message.from_user.id, 'Выберите цвет', reply_markup=k_mk0_bu_mod)
                await message.delete()
                await sklad.sklad_read(message)

                @dp.message_handler(Text(equals=["Черный(0BM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_bu_mod_b)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0BMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 черный безухий, МОД+ комплектация, 56 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_bu_b_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMB56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0BMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 черный безухий, МОД+ комплектация, 58 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_b_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMB58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0BMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 черный безухий, МОД+ комплектация, 60 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_b_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMB60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Песочный(0BM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_bu_mod_s)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0BMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 Песочный безухий, МОД+ комплектация, 56 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_bu_s_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMS56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0BMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Песочный безухий, МОД+ комплектация, 58 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_s_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMS58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0BMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Песочный безухий, МОД+ комплектация, 60 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_s_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMS60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Олива(0BM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk0_bu_mod_o)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(0BMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк0 Олива безухий, МОД+ комплектация, 56 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk0_bu_o_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMO56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(0BMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Олива безухий, МОД+ комплектация, 58 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_o_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMO58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(0BMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк0 Олива безухий, МОД+ комплектация, 60 размер. Стоимость 57250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk0_bu_o_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(0BMO60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

    @dp.message_handler(Text(equals=["MK2"]))
    async def helmet(message: types.Message):
        await bot.send_message(message.from_user.id, 'Выберите форму ', reply_markup=k_mk2)
        await message.delete()

        @dp.message_handler(Text(equals=["Ушастый(2)"]))
        async def helmet(message: types.Message):
            await sklad.sklad_read(message)
            await bot.send_message(message.from_user.id, 'Выберите комплектацию ', reply_markup = k_mk2_uh)
            await message.delete()



            @dp.message_handler(Text(equals=["Штатный(2Y)"]))
            async def helmet(message: types.Message):
                await sklad.sklad_read(message)
                await bot.send_message(message.from_user.id, 'Выберите цвет', reply_markup=k_mk2_uh_st)
                await message.delete()


                @dp.message_handler(Text(equals=["Черный(2YS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_uh_st_b)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2YSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 черный Ушастый, штатная комплектация, 56 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_uh_b_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSB56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2YSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 черный Ушастый, штатная комплектация, 58 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_b_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSB58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                    @dp.message_handler(Text(equals=["60(2YSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 черный Ушастый, штатная комплектация, 60 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_b_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSB60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                @dp.message_handler(Text(equals=["Песочный(2YS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_uh_st_s)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2YSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 Песочный Ушастый, штатная комплектация, 56 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_uh_s_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSS56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2YSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Песочный Ушастый, штатная комплектация, 58 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_s_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSS58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2YSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Песочный Ушастый, штатная комплектация, 60 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_s_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSS60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Олива(2YS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_uh_st_o)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2YSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 Олива Ушастый, штатная комплектация, 56 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_uh_o_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSO56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2YSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Олива Ушастый, штатная комплектация, 58 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_o_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSO58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2YSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Олива Ушастый, штатная комплектация, 60 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_o_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YSO60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


            @dp.message_handler(Text(equals=["МОД+(2Y)"]))
            async def helmet(message: types.Message):
                await sklad.sklad_read(message)
                await bot.send_message(message.from_user.id, 'Выберите цвет', reply_markup=k_mk2_uh_mod)
                await message.delete()


                @dp.message_handler(Text(equals=["Черный(2YM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_uh_mod_b)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2YMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 черный Ушастый, МОД+ комплектация, 56 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_uh_b_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMB56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2YMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 черный Ушастый, МОД+ комплектация, 58 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_b_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMB58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                    @dp.message_handler(Text(equals=["60(2YMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 черный Ушастый, МОД+ комплектация, 60 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_b_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMB60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                @dp.message_handler(Text(equals=["Песочный(2YM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_uh_mod_s)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2YMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 Песочный Ушастый, МОД+ комплектация, 56 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_uh_s_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMS56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2YMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Песочный Ушастый, МОД+ комплектация, 58 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_s_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMS58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2YMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Песочный Ушастый, МОД+ комплектация, 60 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_s_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMS60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Олива(2YM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_uh_mod_o)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2YMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 Олива Ушастый, МОД+ комплектация, 56 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_uh_o_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMO56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2YMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Олива Ушастый, МОД+ комплектация, 58 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_o_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMO58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                    @dp.message_handler(Text(equals=["60(2YMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Олива Ушастый, МОД+ комплектация, 60 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_uh_o_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2YMO60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()



        @dp.message_handler(Text(equals=["Безухий(2)"]))
        async def helmet(message: types.Message):
            await sklad.sklad_read(message)
            await bot.send_message(message.from_user.id, 'Выберите комплектацию ', reply_markup = k_mk2_bu)
            await message.delete()


            @dp.message_handler(Text(equals=["Штатный(2B)"]))
            async def helmet(message: types.Message):
                await sklad.sklad_read(message)
                await bot.send_message(message.from_user.id, 'Выберите цвет', reply_markup=k_mk2_bu_st)
                await message.delete()


                @dp.message_handler(Text(equals=["Черный(2BS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_bu_st_b)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2BSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 черный безухий, штатная комплектация, 56 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_bu_b_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSB56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2BSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 черный безухий, штатная комплектация, 58 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_b_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSB58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2BSB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 черный безухий, штатная комплектация, 60 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_b_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSB60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


                @dp.message_handler(Text(equals=["Песочный(2BS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_bu_st_s)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2BSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 Песочный безухий, штатная комплектация, 56 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_bu_s_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSS56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2BSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Песочный безухий, штатная комплектация, 58 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_s_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSS58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2BSS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Песочный безухий, штатная комплектация, 60 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_s_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSS60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Олива(2BS)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_bu_st_o)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2BSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 Олива безухий, штатная комплектация, 56 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_bu_o_st_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSO56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2BSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Олива безухий, штатная комплектация, 58 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_o_st_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSO58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2BSO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Олива безухий, штатная комплектация, 60 размер. Стоимость 49550 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_o_st_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BSO60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()


            @dp.message_handler(Text(equals=["МОД+(2B)"]))
            async def helmet(message: types.Message):
                await bot.send_message(message.from_user.id, 'Выберите цвет', reply_markup=k_mk2_bu_mod)
                await message.delete()
                await sklad.sklad_read(message)

                @dp.message_handler(Text(equals=["Черный(2BM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_bu_mod_b)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2BMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 черный безухий, МОД+ комплектация, 56 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_bu_b_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMB56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2BMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 черный безухий, МОД+ комплектация, 58 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_b_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMB58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2BMB)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 черный безухий, МОД+ комплектация, 60 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_b_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMB60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Песочный(2BM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_bu_mod_s)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2BMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 Песочный безухий, МОД+ комплектация, 56 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_bu_s_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMS56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2BMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Песочный безухий, МОД+ комплектация, 58 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_s_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMS58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2BMS)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Песочный безухий, МОД+ комплектация, 60 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_s_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMS60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                @dp.message_handler(Text(equals=["Олива(2BM)"]))
                async def helmet(message: types.Message):
                    await bot.send_message(message.from_user.id, 'Выберите размер', reply_markup = k_mk2_bu_mod_o)
                    await message.delete()


                    @dp.message_handler(Text(equals=["56(2BMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id, 'Ваш заказ - шлем мк2 Олива безухий, МОД+ комплектация, 56 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ', reply_markup = k_mk2_bu_o_mod_56)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMO56)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["58(2BMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Олива безухий, МОД+ комплектация, 58 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_o_mod_58)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMO58)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

                    @dp.message_handler(Text(equals=["60(2BMO)"]))
                    async def helmet(message: types.Message):
                        await bot.send_message(message.from_user.id,
                                               'Ваш заказ - шлем мк2 Олива безухий, МОД+ комплектация, 60 размер. Стоимость 58250 рублей. Нажмите кнопку заказать для оформления заказа ',
                                               reply_markup=k_mk2_bu_o_mod_60)
                        await message.delete()

                        @dp.message_handler(Text(equals=["Заказать(2BMO60)"]))
                        async def helmet(message: types.Message):
                            await message.delete()

""" Броня
_____________________________________________________________"""
@dp.message_handler(Text(equals=["Бронеплиты"]))
async def bron(message: types.Message):
    await sklad.sklad_read(message)
    await bot.send_message(message.from_user.id, 'Выберите соответствующий класс защиты', reply_markup = k_br_kz)
    await message.delete()

    @dp.message_handler(Text(equals=["БР3+"]))
    async def helmet(message: types.Message):
        await bot.send_message(message.from_user.id,
                               """Толщина 26 мм, Вес М - 1580 г., Вес L+10% - 2057 г., Вес ЕL+20% - 2500 г. Материал СВМПЭ
Отстрел:
1.два попадания из АК103 патрон ПС обр 43г. 10м. Пробитий нет.
2.одно попадание в центр из СВ-98 патрон 7Н1 10м. Пробитие плиты, но Пуля полностью застряла в Твароне не пробив ни одного слоя.
3.одно попадание Glock-17 патрон 7н21 10м Пробития нет
4.одно попадание Ак74м 7н6 10м Пробития нет.
5.одно попадание ВСС СП-5 10м. Пробития нет.
6.одно попадание ПКП Печенег ЛПС 10м пробитие плиты, но Пуля полностью
застряла в Твароне не пробив несколько первых слоев. (тварон был многократно до этого поврежден и прострелен насквозь при других испытаниях)
Выберите необходимый размер плиты""",
                               reply_markup=k_br_kz_3)
        await message.delete()

        @dp.message_handler(Text(equals=["M(3+)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР3+ размер M. Цена: 20060 рублей. ',
                                   reply_markup=k_br_kz_3_M)
            await message.delete()


        @dp.message_handler(Text(equals=["L(3+)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР3+ размер L. Цена: 21565 рублей. ',
                                   reply_markup=k_br_kz_3_L)
            await message.delete()


        @dp.message_handler(Text(equals=["EL(3+)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР3+ размер EL. Цена: 23950 рублей. ',
                                   reply_markup=k_br_kz_3_EL)
            await message.delete()


    @dp.message_handler(Text(equals=["БР4"]))
    async def helmet(message: types.Message):
        await bot.send_message(message.from_user.id,
                                """
                                Толщина 26 мм, Вес М - 2100 г., Вес L+10% - 2500 г., Вес ЕL+20% - 2800 г. Материал СВМПЭ + керамика.
    Отстрел по классу защиты БР4 (протокол отстрела размещен в официальной группе ВК)
    Выберите необходимый размер плиты""",
                               reply_markup=k_br_kz_4)
        await message.delete()

        @dp.message_handler(Text(equals=["M(4)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР4 размер M. цена 20250 рублей',
                                   reply_markup=k_br_kz_4_M)
            await message.delete()


        @dp.message_handler(Text(equals=["L(4)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР4 размер L. цена 21875 рублей',
                                   reply_markup=k_br_kz_4_L)
            await message.delete()


        @dp.message_handler(Text(equals=["EL(4)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР4 размер EL. цена 24000 рублей',
                                   reply_markup=k_br_kz_4_EL)
            await message.delete()


    @dp.message_handler(Text(equals=["БР5"]))
    async def helmet(message: types.Message):
        await bot.send_message(message.from_user.id,
                                """
                                Толщина 26 мм, Вес М - 2600 г., Вес L+10% - 2960 г., Вес ЕL+20% - 3320 г. Материал СВМПЭ + керамика.
    Отстрел по классу защиты БР5 (6а) (протокол отстрела размещен в официальной группе ВК)
    Выберите необходимый размер плиты""",
                               reply_markup=k_br_kz_5)
        await message.delete()

        @dp.message_handler(Text(equals=["M(5)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР5 размер M. цена 22 850 рублей',
                                   reply_markup=k_br_kz_5_M)
            await message.delete()


        @dp.message_handler(Text(equals=["L(5)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР5 размер L. цена 24850 рублей',
                                   reply_markup=k_br_kz_5_L)
            await message.delete()


        @dp.message_handler(Text(equals=["EL(5)"]))
        async def helmet(message: types.Message):
            await bot.send_message(message.from_user.id,
                                   'Ваш заказ: плита БР5 размер EL. цена 25350 рублей',
                                   reply_markup=k_br_kz_5_EL)
            await message.delete()

""" _______________________________________"""

""" Намордники
__________________________________________________________"""

@dp.message_handler(Text(equals=["Дополнительная Защита"]))
async def bron(message: types.Message):
    await bot.send_message(message.from_user.id, 'В настоящее время в линейке компании АТЛАС представлен один вариант защиты лица.', reply_markup = kb_dz)
    await sklad.sklad_read(message)




@dp.message_handler(Text(equals=["FAQ"]))
async def opt(message: types.Message):
    await bot.send_message(message.from_user.id, 'Полная информация по изделиям, их эксплуатации, контакты изготовителей представлены на официальной странице компании в социальной сети "ВКонтакте"  \
    https://vk.com/atlas_armor ')
    await message.delete()



registr_client(dp)
registr_admin(dp)
registr_test(dp)

executor.start_polling(dp, skip_updates = True, on_startup = on_startup)
