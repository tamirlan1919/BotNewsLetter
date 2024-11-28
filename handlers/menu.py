from aiogram import Router, F
from aiogram.filters.callback_data import CallbackQuery
from keyboards.inline import choose_keyboard
router = Router()

@router.callback_query(F.data == 'main_menu')
async def cmd_stories(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        'Выберите'
    , reply_markup=choose_keyboard())
