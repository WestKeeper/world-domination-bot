from typing import Dict

from aiogram.utils.callback_data import CallbackData

from callbacks.callback_data_name import CallbackDataName
from callbacks.build_shield_callback_data import get_build_shield_callback_data
from callbacks.dev_city_callback_data import get_dev_city_callback_data


def get_callbacks() -> Dict[CallbackDataName, CallbackData]:
    """"""
    callbacks = {}
    user_cities_callback_data = get_dev_city_callback_data()
    build_shield_callback_data = get_build_shield_callback_data()
    callbacks = {
        CallbackDataName.DEV_CITY: user_cities_callback_data,
        CallbackDataName.BUILD_SHIELD: build_shield_callback_data,
    }
    return callbacks
