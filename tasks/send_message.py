from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from configs.config import TOKEN
API_TOKEN = TOKEN
CHANNEL_ID = "@dadaev_blog"  # Укажите ID или username канала

scheduler = AsyncIOScheduler()  # Инициализация планировщика


# Функция отправки сообщения
async def send_delayed_message_stories(chat_id: int):
    bot = Bot(token=API_TOKEN)
    try:
        await bot.send_message(
            chat_id= chat_id,
            text='Привет! Вот урок, как снимать сторис, чтобы охваты постоянно росли:\n'
            'https://www.youtube.com/watch?v=cD60phCue7o&ab_channel=%D0%90%D0%B1%D0%B4%D1%83%D0%BB-%D0%9C%D0%B0%D0%BB%D0%B8%D0%BA'
        )
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
        else:
            await bot.send_message(
                chat_id=chat_id,
                text='https://www.youtube.com/shorts/JtO1zS8W3dI'
            )
    except Exception as e:
        print(f"Ошибка отправки сообщения для пользователя {chat_id}: {e}")
    finally:
        await bot.session.close()

async def send_delayed_message_reels(chat_id: int):
    bot = Bot(token=API_TOKEN)
    try:
        await bot.send_message(
            chat_id=chat_id,
            text='Привет! Вот урок, как снимать рилс, чтобы охваты постоянно росли:\n'
                 'https://www.youtube.com/watch?v=Lvnt0mjNOmg&ab_channel=%D0%90%D0%B1%D0%B4%D1%83%D0%BB-%D0%9C%D0%B0%D0%BB%D0%B8%D0%BA'
        )
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
        else:
            await bot.send_message(
                chat_id=chat_id,
                text='https://www.youtube.com/shorts/JtO1zS8W3dI'
            )
    except Exception as e:
        print(f"Ошибка отправки сообщения для пользователя {chat_id}: {e}")
    finally:
        await bot.session.close()


# Функция добавления задачи в планировщик
def schedule_message(chat_id: int, option: str):
    # Уникальный идентификатор задачи
    job_id = f"{option}_{chat_id}"
    run_time = datetime.now() + timedelta(hours=3)  # Через 3 часа

    # Проверяем, существует ли уже задача с этим ID
    existing_job = scheduler.get_job(job_id)

    if existing_job:
        # Если задача уже существует, удаляем её
        print(f"Задача с ID {job_id} уже существует. Удаляем старую задачу.")
        scheduler.remove_job(job_id)

    # Добавляем новую задачу
    print(f"Добавляем новую задачу с ID {job_id}.")
    if option == 'reels':
        scheduler.add_job(send_delayed_message_reels, "date", run_date=run_time, args=[chat_id], id=job_id)
    else:
        scheduler.add_job(send_delayed_message_stories, "date", run_date=run_time, args=[chat_id], id=job_id)

# Запуск планировщика
def start_scheduler():
    scheduler.start()
