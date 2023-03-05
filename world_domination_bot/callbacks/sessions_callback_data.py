from aiogram.utils.callback_data import CallbackData


def get_sessions_callback_data() -> CallbackData:
    """"""
    cb = CallbackData('sessions', 'session_id')
    return cb
