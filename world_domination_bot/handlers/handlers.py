from aiogram import Dispatcher

from handlers.order.handler_order_lib import register_order_handlers
from handlers.start import start_command
from handlers.status import status_command


def register_handlers(dp: Dispatcher):
    """"""
    dp.register_message_handler(start_command, commands=['start', 'restart'], state='*')
    dp.register_message_handler(status_command, commands=['status'], state='*')
    register_order_handlers(dp)
