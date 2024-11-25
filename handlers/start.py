import asyncio
from sqlalchemy.exc import IntegrityError
from models import User, SessionLocal
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from tasks.send_message import send_delayed_message, schedule_message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    # Первое сообщение пользователю
    await message.answer(
        'Привет! Вот урок, как снимать сторис, чтобы охваты постоянно росли:\n'
        'https://www.youtube.com/watch?v=cD60phCue7o&ab_channel=%D0%90%D0%B1%D0%B4%D1%83%D0%BB-%D0%9C%D0%B0%D0%BB%D0%B8%D0%BA'
    )

    # Сохраняем пользователя в базу данных
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.chat_id == str(message.chat.id)).first()
        if not user:
            # Добавляем нового пользователя
            new_user = User(chat_id=str(message.chat.id))
            session.add(new_user)
            session.commit()
    except IntegrityError:
        session.rollback()
        await message.answer("Произошла ошибка при регистрации.")
    finally:
        session.close()

    # Запускаем отложенную отправку сообщения через 4 часа
    schedule_message(chat_id=message.chat.id)


