from aiogram import Dispatcher

from callbacks.user_cities_callback_data import get_user_cities_callback_data
from handlers.order.build_bomb import build_bomb_cancel_command
from handlers.order.build_bomb import build_bomb_command
from handlers.order.dev_eco import dev_eco_cancel_command
from handlers.order.dev_eco import dev_eco_command
from handlers.order.dev_city import dev_city_callback
from handlers.order.dev_city import dev_city_cancel_command
from handlers.order.dev_city import dev_city_command
from handlers.order.nuke_tech import nuke_tech_cancel_command
from handlers.order.nuke_tech import nuke_tech_command
from handlers.order.order import order_command
from states.game_states_group.game_states_group import GameStatesGroup


def register_order_handlers(dp: Dispatcher):
    """"""
    user_cities_callback_data = get_user_cities_callback_data()
    print('before order')
    dp.register_message_handler(order_command, commands=['order'], state='*')
    print('after order')
    dp.register_message_handler(
        nuke_tech_command, commands=['nuke_tech'], state=GameStatesGroup.order)
    dp.register_message_handler(
        nuke_tech_cancel_command, commands=['nuke_tech_cancel'], state=GameStatesGroup.order)
    dp.register_message_handler(
        build_bomb_command, commands=['build_bomb'], state=GameStatesGroup.order)
    dp.register_message_handler(
        build_bomb_cancel_command, commands=['build_bomb_cancel'], state=GameStatesGroup.order)
    dp.register_message_handler(
        dev_eco_command, commands=['dev_eco'], state=GameStatesGroup.order)
    dp.register_message_handler(
        dev_eco_cancel_command, commands=['dev_eco_cancel'], state=GameStatesGroup.order)
    dp.register_message_handler(
        dev_city_command, commands=['dev_city'], state=GameStatesGroup.order)
    dp.register_message_handler(
        dev_city_cancel_command, commands=['dev_city_cancel'], state=GameStatesGroup.order)

    dp.register_callback_query_handler(
        dev_city_callback, user_cities_callback_data.filter(), state=GameStatesGroup.order)
