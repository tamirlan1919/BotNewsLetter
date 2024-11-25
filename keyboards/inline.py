from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_broadcast_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Разослать сообщение", callback_data="broadcast_message")
            ]
        ]
    )