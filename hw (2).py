from aiogram import types, Dispatcher


async def delete_sticker(message: types.Message):
    await message.delete()


# @dp.message_handler()
async def bad_words_filter(message: types.Message):
    bad_words = ['html', 'js', 'css', 'жинди', 'дурак']
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.answer(f"Не матерись {message.from_user.full_name}, "
                                 f"сам ты {word}")
            await message.delete()
            # await bot.delete_message(message.chat.id, message.message_id)
            break

    if message.text.startswith('.'):
        # await bot.pin_chat_message(message.chat.id, message.message_id)
        await message.pin()

    if message.text == "dice":
        a = await message.answer_dice()
        # await bot.send_dice(message.chat.id, emoji="⚽️")
        # print(a.dice.value)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_words_filter, content_types=['text'])
    dp.register_message_handler(delete_sticker, content_types=['sticker', 'photo',
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

    start_markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        row_width=3
    )

    start_button = KeyboardButton("/start")
    quiz_button = KeyboardButton("/quiz")
    help_button = KeyboardButton("/help")

    start_markup.add(
        start_button,
        quiz_button,
        help_button,

    )
    'animation'])
from decouple import config
from aiogram import Bot,Dispatcher,types
from aiogram.utils import  executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
TOKEN = config('TOKEN')
from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin
import logging

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Кто лучший препод?"
    answer = [
        "Airas",
        "Bekbolot",
        "Esen",
        "igor",
        "Nurlan",
        "Aleksey",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Сколько областей в Кыргызстане?"
    answer = [
        "12",
        "3",
        "7",
        "0",
        "-10",
        "999",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
    )

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Hello bro!')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('Сам разбирайся брат!')

@dp.message_handler(commands=['mem'])
async def mem_command(message: types.Message):
    photos = (
        'media/mem1.jpg',
        'media/mem2.jpg',
        'media/mem3.jpg',
        'media/mem4.jpg',
        'media/mem5.jpg',
        'media/mem6.jpg',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id,photo)
@dp.message_handler()
async def echo_command(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text)**2)
    else:
        await message.answer(message.text)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)