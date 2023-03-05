from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


def get_member_session_keyboard() -> ReplyKeyboardMarkup:
    """"""
    restart_button = KeyboardButton('/restart')
    disconnect_from_session_button = KeyboardButton('/disconnect_from_session')
    session_status_button = KeyboardButton('/session_status')

    kb = ReplyKeyboardMarkup(keyboard=[
        [restart_button],
        [session_status_button],
        [disconnect_from_session_button]],
        resize_keyboard=True)

    return kb
