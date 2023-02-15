from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


def get_init_keyboard() -> ReplyKeyboardMarkup:
    """"""
    restart_button = KeyboardButton('/restart')
    status_button = KeyboardButton('/status')
    order_button = KeyboardButton('/order')
    restore_db_button = KeyboardButton('/restore_db')

    kb = ReplyKeyboardMarkup(keyboard=[
        [restart_button, restore_db_button],
        [status_button, order_button]],
        resize_keyboard=True)

    return kb
