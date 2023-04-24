import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from database.bot_db import sql_command_random, sql_command_all
from keyboards.clien_kb import direction_markup


async def pin_message(message: types.Message):
@@ -92,6 +94,15 @@ async def quiz1(message: types.Message):
        reply_markup=markup)


async def get_random_user(message: types.Message):
    # await message.answer("Какое направление?", reply_markup=direction_markup)
    await sql_command_random(message)


async def get_all_mentor(message: types.Message):
    await sql_command_all()


def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands=["quiz"])
    dp.register_message_handler(mem, commands=["mem"])
@@ -100,3 +111,5 @@ def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix='!')
    dp.register_message_handler(game, commands=["game"])
    dp.register_message_handler(dice_game, commands=["dice"])
    dp.register_message_handler(get_random_user, commands=["getmentor"])
    dp.register_message_handler(get_all_mentor, commands=["allmentor"])
    one_time_keyboard = True
    ).add(KeyboardButton('CANCEL'))
    direction_markup.add(direction_back, direction_front, direction_android).add(direction_uxui, direction_ios).add(
    cancel_markup)
    KeyboardButton("CANCEL"))
    submit_markup.add(submit_markup1, submit_markup2)
    from handlers import callback, client, extra, FSM_admin_mentors
    from handlers import callback, client, extra, FSM_admin_mentors, admin
    from aiogram.utils import executor

    from database.bot_db import sql_create
    from config import bot, dp
    import logging


    async

    def on_startup(_):
        sql_create()

    admin.register_message_admin(dp)
    client.register_client_handler(dp)
    callback.register_handler_callback(dp)
    FSM_admin_mentors.register_handlers_fsm_anketa(dp)
    extra.register_handlers_extra(dp)
    if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO)
        executor.start_polling(dp, skip_updates=True)
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)