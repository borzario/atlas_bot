- МК0(БР1 + 9х19fmj) \ МК2(БР2 9х21 сп11)


"""запиливаем функцию отмены загрузки
#@dp.message_hendler(state = "*", commands = 'отмена')
#@dp.message_hendler(Text(equals = 'отмена', ignore_case = True), state = "*")
async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")

#первый ответ ловится, заполняется словарь
#@dp.message_hendler(content_types = ['photo'], state = FSMAdmin.photo)
async def load_photo(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMClient.next()
    await message.reply("Введи имя получателя")"""