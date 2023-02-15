from aiogram.utils.callback_data import CallbackData


def get_send_money_callback_data() -> CallbackData:
    """"""
    cb = CallbackData('send_money', 'country_name')
    return cb
