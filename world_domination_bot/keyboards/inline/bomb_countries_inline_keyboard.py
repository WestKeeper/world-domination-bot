from typing import List

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from callbacks.bomb_countries_callback_data import get_bomb_countries_callback_data
from schemas.countries import CountryCitiesShow


def get_bomb_countries_inline_keyboard(
    countries: List[CountryCitiesShow],
) -> InlineKeyboardMarkup:
    """"""
    buttons = []
    callback_data = get_bomb_countries_callback_data()
    for country in countries:
        button = InlineKeyboardButton(
            text=country.name, callback_data=callback_data.new(country.name))
        buttons.append(button)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [button for button in buttons]],
        resize_keyboard=True)

    return kb
