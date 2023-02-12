from typing import Any, Dict

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.enums import OrderAction
from db.services.cities import get_cities_by_user_id
from db.services.countries import get_country_by_user_id
from db.services.order_actions import get_order_action_by_action_name
from db.session import get_db
from templates.templates import render_template
from keyboards.default.order_keyboard import get_order_keyboard
from keyboards.default.user_cities_keyboard import get_user_cities_keyboard


async def dev_city_command(message: Message, db: Session = next(get_db())):
    """"""
    user_cities = get_cities_by_user_id(message.from_user.id, db)

    ikb = get_user_cities_keyboard(user_cities)
    await message.answer(
        render_template('orders/choose_city.j2'),
        parse_mode='HTML', reply_markup=ikb)
    await message.delete()


async def dev_city_cancel_command(
    message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.NUKE_TECH.value, db)
    user_country = get_country_by_user_id(message.from_user.id, db)
    async with state.proxy() as data:
        data['order'].price -= len(data['order'].dev_city) * order_action.price
        data['order'].dev_city = set()
        order_state = data['order']

    kb = get_order_keyboard()
    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()


async def dev_city_callback(
    callback: CallbackQuery,
    callback_data: Dict[str, Any],
    state: FSMContext,
    db: Session = next(get_db()),
):
    """"""
    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.DEV_CITY.value, db)
    user_country = get_country_by_user_id(callback.from_user.id, db)
    async with state.proxy() as data:
        data['order'].price += order_action.price
        data['order'].dev_city.add(callback_data['city_name'])
        order_state = data['order']

    kb = get_order_keyboard()
    await callback.message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget}),
        parse_mode='HTML', reply_markup=kb)
    await callback.answer(f'{callback_data["city_name"]} будет развит!')
