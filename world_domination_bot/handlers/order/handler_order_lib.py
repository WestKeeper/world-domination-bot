from aiogram import Dispatcher

from callbacks.bomb_cities_callback_data import get_bomb_cities_callback_data
from callbacks.bomb_countries_callback_data import get_bomb_countries_callback_data
from callbacks.build_shield_callback_data import get_build_shield_callback_data
from callbacks.dev_city_callback_data import get_dev_city_callback_data
from callbacks.send_money_callback_data import get_send_money_callback_data
from handlers.order.bomb import bomb_city_callback
from handlers.order.bomb import bomb_country_callback
from handlers.order.bomb import bomb_cancel_command
from handlers.order.bomb import bomb_command
from handlers.order.build_bomb import build_bomb_cancel_command
from handlers.order.build_bomb import build_bomb_command
from handlers.order.build_shield import build_shield_callback
from handlers.order.build_shield import build_shield_cancel_command
from handlers.order.build_shield import build_shield_command
from handlers.order.cancel_order import cancel_order_command
from handlers.order.dev_eco import dev_eco_cancel_command
from handlers.order.dev_eco import dev_eco_command
from handlers.order.dev_city import dev_city_callback
from handlers.order.dev_city import dev_city_cancel_command
from handlers.order.dev_city import dev_city_command
from handlers.order.nuke_tech import nuke_tech_cancel_command
from handlers.order.nuke_tech import nuke_tech_command
from handlers.order.order import order_command
from handlers.order.restore_order import restore_order_command
from handlers.order.send_money import send_money_amount_command
from handlers.order.send_money import send_money_validate_command
from handlers.order.send_money import send_money_amount_callback
from handlers.order.send_money import send_money_cancel_command
from handlers.order.send_money import send_money_command
from handlers.order.send_order import send_order_command
from states.game_states_group import GameStatesGroup
from states.order_states_group import OrderStatesGroup

def register_order_handlers(dp: Dispatcher):
    """"""
    dev_city_callback_data = get_dev_city_callback_data()
    build_shield_callback_data = get_build_shield_callback_data()
    bomb_countries_callback_data = get_bomb_countries_callback_data()
    bomb_cities_callback_data = get_bomb_cities_callback_data()
    send_money_callback_data = get_send_money_callback_data()

    dp.register_message_handler(order_command, commands=['order'], state='*')
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
    dp.register_message_handler(
        build_shield_command, commands=['build_shield'], state=GameStatesGroup.order)
    dp.register_message_handler(
        build_shield_cancel_command, commands=['build_shield_cancel'], state=GameStatesGroup.order)
    dp.register_message_handler(
        bomb_command, commands=['bomb'], state=GameStatesGroup.order)
    dp.register_message_handler(
        bomb_cancel_command, commands=['bomb_cancel'], state=GameStatesGroup.order)
    dp.register_message_handler(
        send_money_command, commands=['send_money'], state=GameStatesGroup.order)
    dp.register_message_handler(
        send_money_cancel_command, commands=['send_money_cancel'], state=GameStatesGroup.order)
    dp.register_message_handler(
        send_money_validate_command,
        lambda message: not message.text.isdigit() or int(message.text) <= 0,
        state=OrderStatesGroup.money)
    dp.register_message_handler(
        send_money_amount_command, lambda message: message.text.isdigit(),
        state=OrderStatesGroup.money)
    dp.register_message_handler(
        restore_order_command, commands=['restore_order'], state=GameStatesGroup.order)
    dp.register_message_handler(
        send_order_command, commands=['send_order'], state=GameStatesGroup.order)
    dp.register_message_handler(
        cancel_order_command, commands=['cancel_order'], state=GameStatesGroup.order)

    dp.register_callback_query_handler(
        dev_city_callback, dev_city_callback_data.filter(), state=GameStatesGroup.order)
    dp.register_callback_query_handler(
        build_shield_callback, build_shield_callback_data.filter(), state=GameStatesGroup.order)
    dp.register_callback_query_handler(
        bomb_country_callback, bomb_countries_callback_data.filter(), state=GameStatesGroup.order)
    dp.register_callback_query_handler(
        bomb_city_callback, bomb_cities_callback_data.filter(), state=GameStatesGroup.order)
    dp.register_callback_query_handler(
        send_money_amount_callback, send_money_callback_data.filter(), state=GameStatesGroup.order)
