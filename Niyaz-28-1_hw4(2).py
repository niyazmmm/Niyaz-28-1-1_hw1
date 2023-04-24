from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from database.bot_db import sql_command_insert
from config import bot, ADMINS
from keyboards.clien_kb import direction_markup, submit_markup, cancel_markup

@@ -43,7 +43,7 @@ async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какое направление?", reply_markup=direction_markup)
    await bot.send_message(message.from_user.id, "Какое направление?", reply_markup=direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
@@ -55,35 +55,38 @@ async def load_direction(message: types.Message, state: FSMContext):

async def load_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Из какой группы?", reply_markup=cancel_markup)

        if 50 > int(message.text) > 12:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer("Из какой группы?", reply_markup=cancel_markup)
        else:
            await message.answer("возраст не подходит")
    except:
        await message.answer("Вводи только числа!")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, f"{data['id']}"
                                                     f"{data['name']}, {data['direction']}, {data['age']}, "
                                                     f"{data['group']}")
        await bot.send_message(message.from_user.id, f"id - {data['id']},\n"
                                                     f"имя - {data['name']},\nнаправление - {data['direction']},\nвозраст - {data['age']}, \n"
                                                     f"группа - {data['group']}")

    await FSMAdmin.next()
    await message.answer("Все правильно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        # Запись в БД
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Регистрация завершена")
    if message.text.lower() == 'нет':
        await bot.send_message(message.from_user.id, "Регистрация завершена")
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer('Не получилось!')


async def cancel_reg(message: types.Message, state: FSMContext):
    from database.bot_db import sql_command_all, sql_command_delete
    from config import bot, dp
    from aiogram import types
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    from aiogram import Bot, Dispatcher

    async def delete_data(message: types.Message):
        users = await sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id, f"id - {user['id']},\n"
                                                         f"имя - {user['name']},\nнаправление - {user['direction']},\n"
                                                         f"возраст - {user['age']}, \n "
                                                         f"группа - {user['group']}",
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f"Удалить {user[1]}", callback_data=f"delete {user[0]}")))

    async def delete_user(message: types.Message):
        users = await sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id,
                                   f"id - {user[0]},name - {user[1]},dir - {user[2]}, "
                                   f"age - {user[3]}, group - {user[4]}",
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f"Delete {user[1]}", callback_data=f"delete {user[0]}")
                                   ))

    async def complete_delete(call: types.CallbackQuery):
        await sql_command_delete(int(call.data.replace('delete ', '')))
        await call.answer(text="Стёрт с базы данных", show_alert=True)
        await bot.delete_message(call.message.chat.id, call.message.message_id)

    def register_message_admin(dp: Dispatcher):
        dp.register_message_handler(delete_user, commands=["del"])
        dp.register_callback_query_handler(
            complete_delete,
            lambda call: call.data and call.data.startswith("delete ")
        )