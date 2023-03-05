from aiogram import Dispatcher

from common.config import TEST_MODE
from handlers.game_session.handler_order_lib import register_session_handlers
from handlers.order.handler_order_lib import register_order_handlers
from handlers.round.handler_round_lib import register_round_handlers
from handlers.restore_db import restore_db_command
from handlers.start import create_user_command
from handlers.start import start_command
from handlers.status import status_command
from states.game_states_group import GameStatesGroup


def register_handlers(dp: Dispatcher):
    """"""
    dp.register_message_handler(start_command, commands=['start', 'restart'], state='*')
    dp.register_message_handler(
        create_user_command, state=GameStatesGroup.create_user)
    dp.register_message_handler(status_command, commands=['status'], state='*')

    if TEST_MODE:
        dp.register_message_handler(restore_db_command, commands=['restore_db'], state='*')

    register_session_handlers(dp)
    register_round_handlers(dp)
    register_order_handlers(dp)
