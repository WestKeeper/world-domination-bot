from aiogram import Dispatcher

from common.config import TEST_MODE
from handlers.order.handler_order_lib import register_order_handlers
from handlers.restore_db import restore_db_command
from handlers.start import start_command
from handlers.status import status_command


def register_handlers(dp: Dispatcher):
    """"""
    dp.register_message_handler(start_command, commands=['start', 'restart'], state='*')
    dp.register_message_handler(status_command, commands=['status'], state='*')
    if TEST_MODE:
        dp.register_message_handler(restore_db_command, commands=['restore_db'], state='*')
    register_order_handlers(dp)
