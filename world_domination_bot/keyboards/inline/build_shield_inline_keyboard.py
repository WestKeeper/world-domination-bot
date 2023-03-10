from typing import List

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from callbacks.build_shield_callback_data import get_build_shield_callback_data
from schemas.cities import CityShow


def get_build_shield_inline_keyboard(
    user_cities: List[CityShow],
) -> InlineKeyboardMarkup:
    """"""
    buttons = []
    callback_data = get_build_shield_callback_data()
    for user_city in user_cities:
        button = InlineKeyboardButton(
            text=user_city.name, callback_data=callback_data.new(user_city.name))
        buttons.append(button)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [button for button in buttons]],
        resize_keyboard=True)

    return kb
