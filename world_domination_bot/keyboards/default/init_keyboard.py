from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


def get_init_keyboard() -> ReplyKeyboardMarkup:
    """"""
    restart_button = KeyboardButton('/restart')
    status_button = KeyboardButton('/status')
    # help_button = KeyboardButton('/help')
    # sticker_button = KeyboardButton('/sticker')
    # photo_button = KeyboardButton('/photo')
    # load_photo_button = KeyboardButton('/load_photo')

    kb = ReplyKeyboardMarkup(keyboard=[
        [restart_button, status_button] ],
        resize_keyboard=True)

    return kb
