from aiogram import types, Dispatcher
from config import ADMINS, bot
import random


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("ТЫ НЕ МОЙ БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")


async def game(message: types.Message):
    games = ['🏀', '🎲', '⚽️', '🎯', '🎳', '🎰']
    game = random.choice(games)
    if message.text.lower().startswith('game'):
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не админ!')
        else:
            await bot.send_dice(message.chat.id, emoji=f"{game}")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(game)