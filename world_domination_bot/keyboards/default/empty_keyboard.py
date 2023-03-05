from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


def get_empty_keyboard() -> ReplyKeyboardMarkup:
    """"""
    restart_button = KeyboardButton('/restart')

    kb = ReplyKeyboardMarkup(keyboard=[
        [restart_button]],
        resize_keyboard=True)

    return kb
