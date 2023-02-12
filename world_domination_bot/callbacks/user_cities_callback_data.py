from aiogram.utils.callback_data import CallbackData


def get_user_cities_callback_data() -> CallbackData:
    """"""
    cb = CallbackData('user_city', 'city_name')
    return cb
