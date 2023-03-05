from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


def get_init_keyboard() -> ReplyKeyboardMarkup:
    """"""
    restart_button = KeyboardButton('/restart')
    create_session_button = KeyboardButton('/create_session')
    connect_to_session_button = KeyboardButton('/connect_to_session')

    kb = ReplyKeyboardMarkup(keyboard=[
        [restart_button],
        [create_session_button, connect_to_session_button]],
        resize_keyboard=True)

    return kb
