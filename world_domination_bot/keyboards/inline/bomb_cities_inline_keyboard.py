from typing import List

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from callbacks.bomb_cities_callback_data import get_bomb_cities_callback_data
from schemas.cities import CityShow


def get_bomb_cities_inline_keyboard(
    cities: List[CityShow],
) -> InlineKeyboardMarkup:
    """"""
    buttons = []
    callback_data = get_bomb_cities_callback_data()
    for city in cities:
        button = InlineKeyboardButton(
            text=city.name, callback_data=callback_data.new(city.name))
        buttons.append(button)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [button for button in buttons]],
        resize_keyboard=True)

    return kb
