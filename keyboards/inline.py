from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_broadcast_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Разослать сообщение 📨", callback_data="broadcast_message")
            ]
        ]
    )

def get_main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='⏪ Назад', callback_data='main_menu')]
        ]
    )


def choose_keyboard() ->InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard = [
            [InlineKeyboardButton(text="Сторис 🤳", callback_data="stories"),
             InlineKeyboardButton(text="Рилс 🎥", callback_data="reels")]

        ]
    )