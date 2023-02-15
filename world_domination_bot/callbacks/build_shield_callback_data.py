from aiogram.utils.callback_data import CallbackData


def get_build_shield_callback_data() -> CallbackData:
    """"""
    cb = CallbackData('build_shield', 'city_name')
    return cb
