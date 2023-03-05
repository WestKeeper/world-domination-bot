from typing import Any, Dict

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.enums import OrderAction
from db.services.game_sessions import get_active_session_by_user_id
from db.services.session_cities import get_cities_by_user_id
from db.services.session_cities import get_city_by_name
from db.services.session_countries import get_country_by_user_id_and_session_id
from db.services.order_actions import get_order_action_by_action_name
from db.session import get_db
from keyboards.default.order_keyboard import get_order_keyboard
from keyboards.inline.build_shield_inline_keyboard import get_build_shield_inline_keyboard
from templates.templates import render_template


async def build_shield_command(message: Message, db: Session = next(get_db())):
    """"""
    kb = get_order_keyboard()

    user_cities = get_cities_by_user_id(message.from_user.id, db)
    ikb = get_build_shield_inline_keyboard(user_cities)
    cities_to_build_shields = []
    for user_city in user_cities:
        if not user_city.has_shield:
            cities_to_build_shields.append(user_city)

    if not cities_to_build_shields:
        await message.answer(
            render_template('orders/all_cities_have_shields.j2'),
            parse_mode='HTML', reply_markup=kb)
        await message.delete()
        return

    await message.answer(
        render_template('orders/choose_city_for_build_shield.j2'),
        parse_mode='HTML', reply_markup=ikb)
    await message.delete()


async def build_shield_cancel_command(
    message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.BUILD_SHIELD.value, db)
    session = get_active_session_by_user_id(message.from_user.id, db)
    user_country = get_country_by_user_id_and_session_id(message.from_user.id, session.id, db=db)
    async with state.proxy() as data:
        data['order'].price -= len(data['order'].build_shield) * order_action.price
        data['order'].build_shield = set()
        order_state = data['order']

    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()


async def build_shield_callback(
    callback: CallbackQuery,
    callback_data: Dict[str, Any],
    state: FSMContext,
    db: Session = next(get_db()),
):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.BUILD_SHIELD.value, db)
    session = get_active_session_by_user_id(message.from_user.id, db)
    user_country = get_country_by_user_id_and_session_id(message.from_user.id, session.id, db=db)
    shield_city = get_city_by_name(callback_data['city_name'], db=db)
    async with state.proxy() as data:
        if user_country.budget < data['order'].price + order_action.price:
            await callback.message.answer(
                render_template('orders/not_enough_money.j2'),
                parse_mode='HTML', reply_markup=kb)
            await callback.answer(f'Ошибка!')
            return
        if shield_city.has_shield:
            await callback.message.answer(
                render_template('orders/city_has_already_shield.j2',
                                data={'city_name': callback_data['city_name']}),
                parse_mode='HTML', reply_markup=kb)
            await callback.answer(f'Ошибка!')
            return
        if callback_data['city_name'] in data['order'].build_shield:
            await callback.message.answer(
                render_template('orders/order_has_already_shield.j2',
                                data={'city_name': callback_data['city_name']}),
                parse_mode='HTML', reply_markup=kb)
            await callback.answer(f'Ошибка!')
            return

        data['order'].price += order_action.price
        data['order'].build_shield.add(callback_data['city_name'])
        order_state = data['order']

    await callback.message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await callback.answer(f'В городе {callback_data["city_name"]} будет построен щит!')
