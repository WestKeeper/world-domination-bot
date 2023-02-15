from aiogram.utils.callback_data import CallbackData


def get_bomb_countries_callback_data() -> CallbackData:
    """"""
    cb = CallbackData('bomb_countires', 'country_name')
    return cb
