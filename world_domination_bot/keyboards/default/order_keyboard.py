from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


def get_order_keyboard() -> ReplyKeyboardMarkup:
    """"""
    restart_button = KeyboardButton('/restart')
    status_button = KeyboardButton('/status')

    nuke_tech_button = KeyboardButton('/nuke_tech')
    nuke_tech_cancel_button = KeyboardButton('/nuke_tech_cancel')

    build_bomb_button = KeyboardButton('/build_bomb')
    build_bomb_cancel_button = KeyboardButton('/build_bomb_cancel')

    dev_city_button = KeyboardButton('/dev_city')
    dev_city_cancel_button = KeyboardButton('/dev_city_cancel')

    send_money_button = KeyboardButton('/send_money')
    send_money_cancel_button = KeyboardButton('/send_money_cancel')

    build_shield_button = KeyboardButton('/build_shield')
    build_shield_cancel_button = KeyboardButton('/build_shield_cancel')

    dev_eco_button = KeyboardButton('/dev_eco')
    dev_eco_cancel_button = KeyboardButton('/dev_eco_cancel')

    bomb_button = KeyboardButton('/bomb')
    bomb_cancel_button = KeyboardButton('/bomb_cancel')

    restore_order_button = KeyboardButton('/restore_order')
    send_order_button = KeyboardButton('/send_order')

    kb = ReplyKeyboardMarkup(keyboard=[
        [restart_button, status_button],
        [nuke_tech_button, nuke_tech_cancel_button],
        [build_bomb_button, build_bomb_cancel_button],
        [dev_city_button, dev_city_cancel_button],
        [send_money_button, send_money_cancel_button],
        [build_shield_button, build_shield_cancel_button],
        [dev_eco_button, dev_eco_cancel_button],
        [bomb_button, bomb_cancel_button],
        [restore_order_button, send_order_button]],
        resize_keyboard=True)

    return kb
