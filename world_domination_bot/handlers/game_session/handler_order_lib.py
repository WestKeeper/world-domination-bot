from aiogram import Dispatcher

from callbacks.sessions_callback_data import get_sessions_callback_data
from handlers.game_session.connect_to_session import connect_to_session_command
from handlers.game_session.connect_to_session import connect_to_session_callback
from handlers.game_session.create_session import create_session_command
from handlers.game_session.disconnect_from_session import disconnect_from_session_command
from handlers.game_session.session_status import session_status_command
from states.game_states_group import GameStatesGroup

def register_session_handlers(dp: Dispatcher):
    """"""
    sessions_callback_data = get_sessions_callback_data()

    dp.register_message_handler(
        create_session_command, commands=['create_session'],
        state=GameStatesGroup.session_connection)
    dp.register_message_handler(
        connect_to_session_command, commands=['connect_to_session'],
        state=GameStatesGroup.session_connection)
    dp.register_message_handler(
        session_status_command, commands=['session_status'],
        state=GameStatesGroup.session_connection)
    dp.register_message_handler(
        disconnect_from_session_command, commands=['disconnect_from_session'],
        state=GameStatesGroup.session_connection)

    dp.register_callback_query_handler(
        connect_to_session_callback, sessions_callback_data.filter(),
        state=GameStatesGroup.session_connection)
