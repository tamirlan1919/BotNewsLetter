import asyncio

from aiogram import Bot, Dispatcher
import logging
from configs.config import TOKEN
from handlers import router
from models import init_db
from tasks.send_message import start_scheduler


async def main():
    init_db()
    start_scheduler()

    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())