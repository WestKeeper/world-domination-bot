from aiogram import Dispatcher

from handlers.round.start_game import start_game_command
from states.game_states_group import GameStatesGroup


def register_round_handlers(dp: Dispatcher):
    """"""
    dp.register_message_handler(
        start_game_command, commands=['start_game'], state=GameStatesGroup.session_connection)
