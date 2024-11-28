from aiogram import Router, F
from aiogram.filters.callback_data import CallbackQuery
from keyboards.inline import get_main_menu
from tasks.send_message import schedule_message

router = Router()

@router.callback_query(F.data == 'stories')
async def cmd_stories(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        'Привет! Вот урок, как снимать сторис, чтобы охваты постоянно росли:\n'
        'https://www.youtube.com/watch?v=cD60phCue7o&ab_channel=%D0%90%D0%B1%D0%B4%D1%83%D0%BB-%D0%9C%D0%B0%D0%BB%D0%B8%D0%BA'
    , reply_markup=get_main_menu())
    schedule_message(chat_id=callback_query.message.chat.id, option='reels')
