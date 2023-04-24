import datetime
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from config import bot, ADMINS


async def send_message_date(bot: Bot):
    await bot.send_message(ADMINS[0], "Хуппи бёздей!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')

    scheduler.add_job(
        send_message_date,
        trigger=DateTrigger(
            run_date=datetime.datetime(year=2023, month=9, day=14, hour=00, minute=1)
        ),
        kwargs={"bot": bot},
    )

    scheduler.start()
    from aiogram.utils import executor
    from config import dp
    from handlers import client, callback, extra, admin, FSM_Admin_mentors
    from handlers import client, callback, extra, admin, FSM_Admin_mentors, sheduler
    import logging
    from database.bot_db import sql_create
    async def on_startup(_)

    async def on_startup(_):
        sql_create()
        await sheduler.set_scheduler()

    client.register_handlers_client(dp)

    @ @-17

    , 4 + 20, 4 @ @

    async def on_startup(_)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
        executor.start_polling(dp, skip