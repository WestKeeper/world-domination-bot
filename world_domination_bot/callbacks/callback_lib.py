from typing import Dict

from aiogram.utils.callback_data import CallbackData

from callbacks.callback_data_name import CallbackDataName
from callbacks.user_cities_callback_data import get_user_cities_callback_data


def get_callbacks() -> Dict[CallbackDataName, CallbackData]:
    """"""
    callbacks = {}
    user_cities_callback_data = get_user_cities_callback_data()
    callbacks = {
        CallbackDataName.USER_CITIES: user_cities_callback_data
    }
    return callbacks
