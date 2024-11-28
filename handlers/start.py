import asyncio
from sqlalchemy.exc import IntegrityError
from models import User, SessionLocal
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from tasks.send_message import  schedule_message
from keyboards.inline import choose_keyboard
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Выберите', reply_markup=choose_keyboard())

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




