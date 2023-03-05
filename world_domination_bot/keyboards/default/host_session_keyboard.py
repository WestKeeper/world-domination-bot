from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


def get_host_session_keyboard() -> ReplyKeyboardMarkup:
    """"""
    restart_button = KeyboardButton('/restart')
    configure_session_button = KeyboardButton('/configure_session')
    game_button = KeyboardButton('/start_game')
    session_status_button = KeyboardButton('/session_status')
    disconnect_from_session_button = KeyboardButton('/disconnect_from_session')

    kb = ReplyKeyboardMarkup(keyboard=[
        [restart_button],
        [configure_session_button, session_status_button, game_button],
        [disconnect_from_session_button]],
        resize_keyboard=True)

    return kb
