from aiogram.utils.callback_data import CallbackData


def get_bomb_cities_callback_data() -> CallbackData:
    """"""
    cb = CallbackData('bomb_cities', 'city_name')
    return cb
