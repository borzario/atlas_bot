@dp.message_handler(commands = ["FAQ"])
async def opt(message: types.Message):
    await bot.send_message(message.from_user.id, 'Тут будет раздел с автоответчиком и ссылкой на сайт')
    await message.delete()

    @dp.message_handler()
    async def salam(message: types.Message):
        uzer_text = message.text
        if {i.lower().translate(str.maketrans("", '', string.punctuation)) for i in uzer_text.split(' ')}.intersection(
                {i for i in
                 "салют, здорова, здорово, здоров, здравствуйте, привет, салам, здоров, хая, прив, хай".split(
                         ", ")}) != set():
            await bot.send_message(message.from_user.id, "await bot.send_message(466849086, f'Заказ от {message.from_user.id} -шлем мк0 черный ушанка бич-комплект 55 размер'")

"""


"""
