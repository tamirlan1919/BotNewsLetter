import asyncio
from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ContentType
from configs.config import admin_list
from keyboards.inline import get_broadcast_keyboard
from states.state import Letter
from models import User, SessionLocal
from tasks.send_message import schedule_message

router = Router()

# Команда для администратора
@router.message(Command('admin'))
async def admin_cmd(message: Message):
    if message.chat.id in admin_list:
        await message.answer(
            "Добро пожаловать! Вот ваша клавиатура для управления рассылкой:",
            reply_markup=get_broadcast_keyboard()
        )
    else:
        await message.answer("У вас нет доступа к административным функциям.")
# Обработчик текстовых и медиа-сообщений в состоянии Letter.text
@router.message(Letter.text, F.content_type.in_({"text", "photo", "video", "document"}))
async def send_broadcast(message: Message, state: FSMContext, bot: Bot):
    session = SessionLocal()
    users = session.query(User).all()

    success = 0
    failed = 0

    for user in users:
        try:
            # Определяем тип контента
            if message.text:
                # Рассылка текста
                await bot.send_message(chat_id=int(user.chat_id), text=message.text)
            elif message.photo:
                # Рассылка фото
                await bot.send_photo(
                    chat_id=int(user.chat_id),
                    photo=message.photo[-1].file_id,
                    caption=message.caption if message.caption else None
                )
            elif message.video:
                # Рассылка видео
                await bot.send_video(
                    chat_id=int(user.chat_id),
                    video=message.video.file_id,
                    caption=message.caption if message.caption else None
                )
            elif message.document:
                # Рассылка документа
                await bot.send_document(
                    chat_id=int(user.chat_id),
                    document=message.document.file_id,
                    caption=message.caption if message.caption else None
                )
            else:
                failed += 1
                continue

            # Планируем отложенное сообщение
            schedule_message(chat_id=message.chat.id)
            success += 1
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user.chat_id}: {e}")
            failed += 1

    # Отправляем итог админу
    await message.answer(f"Рассылка завершена.\nУспешно: {success}\nНеудачно: {failed}")

    # Завершаем состояние
    await state.clear()
    session.close()


# Обработчик нажатия кнопки "broadcast_message"
@router.callback_query(F.data == "broadcast_message")
async def handle_broadcast_button(callback_query: CallbackQuery, state: FSMContext):
    # Переход в состояние ввода текста или медиа для рассылки
    await callback_query.message.answer("Введите текст или отправьте медиа для рассылки:")
    await state.set_state(Letter.text)
    await callback_query.answer()