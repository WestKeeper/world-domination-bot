from aiogram.utils.callback_data import CallbackData


def get_dev_city_callback_data() -> CallbackData:
    """"""
    cb = CallbackData('dev_city', 'city_name')
    return cb
