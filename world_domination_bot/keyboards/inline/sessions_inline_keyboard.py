from typing import List

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from callbacks.sessions_callback_data import get_sessions_callback_data
from schemas.game_sessions import GameSessionShow


def get_sessions_inline_keyboard(
    sessions: List[GameSessionShow],
) -> InlineKeyboardMarkup:
    """"""
    buttons = []
    callback_data = get_sessions_callback_data()
    for session in sessions:
        button = InlineKeyboardButton(
            text=session.id, callback_data=callback_data.new(session.id))
        buttons.append(button)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [button for button in buttons]],
        resize_keyboard=True)

    return kb
