from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
import random

from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import logging


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
     await message.answer(f"Добро пожаловать {message.from_user.username}")


@dp.message_handler(commands=["mem"])
async def mem(message: types.Message):
    photos =  (
        'media/mem1.jpg',
        'media/mem2.jpg',
        'media/mem3.jpg',
        'media/mem4.jpg',
        'media/mem5.jpg',
        'media/mem6.jpg',
    )
    photo = open(random.choice(photos), 'rb')
    # data = []
    # for mems in file:
    #     data.append(mems)
    #     r = random.choice(data)
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler(commands=["quiz"])
async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("Дальше", callback_data='button_call1')
    markup.add(button_call1)
    question = "Как зовут супермена?"
    answers = [
        "Владимир",
        "Брюс Вейн",
        "Калэл",
        "Чак Норис"]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=10,
        reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == 'button_call1')
async def quiz2(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call2 = InlineKeyboardButton("Дальше", callback_data='button_call2')
    markup.add(button_call2)
    question = "В каком году родился Манас?"
    answers = [
        "1900",
        "1890",
        "1906",
        "2020"]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques
    tion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=10,
        reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == 'button_call2')
async def quiz2(call: types.callback_query):
    question = "В каком году распался СССР?"
    answers = [
        "1900",
        "1991",
        "1897",
        "2000"]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=10
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)