from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup


class GameStatesGroup(StatesGroup):
    """"""
    session_connection = State()
    create_user = State()
    round = State()
    order = State()
