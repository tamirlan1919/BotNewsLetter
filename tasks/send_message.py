from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from configs.config import TOKEN
API_TOKEN = TOKEN
CHANNEL_ID = "@dadaev_blog"  # Укажите ID или username канала

scheduler = AsyncIOScheduler()  # Инициализация планировщика


# Функция отправки сообщения
async def send_delayed_message(chat_id: int):
    bot = Bot(token=API_TOKEN)
    try:
        # Проверяем, подписан ли пользователь
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=chat_id)
        if member.status not in {"member", "administrator", "creator"}:
            # Если не подписан, отправляем сообщение
            await bot.send_message(
                chat_id=chat_id,
                text="Подпишись на мой телеграмм канал. Там я делюсь новыми алгоритмами инстаграм, фишками, делаю бесплатные разборы аккаунтов🔥",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="Подписаться на канал",
                                url=f"https://t.me/{CHANNEL_ID.lstrip('@')}"
                            )
                        ]
                    ]
                )
            )
    except Exception as e:
        print(f"Ошибка отправки сообщения для пользователя {chat_id}: {e}")
    finally:
        await bot.session.close()


# Функция добавления задачи в планировщик
def schedule_message(chat_id: int):
    run_time = datetime.now() + timedelta(seconds=4)  # Через 4 часа
    scheduler.add_job(send_delayed_message, "date", run_date=run_time, args=[chat_id])


# Запуск планировщика
def start_scheduler():
    scheduler.start()
