from typing import Any, Dict

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.enums import OrderAction
from db.services.cities import get_cities_by_country_name
from db.services.countries import get_not_user_countries
from db.services.countries import get_country_by_user_id
from db.services.order_actions import get_order_action_by_action_name
from db.session import get_db
from keyboards.default.order_keyboard import get_order_keyboard
from keyboards.inline.bomb_cities_inline_keyboard import get_bomb_cities_inline_keyboard
from keyboards.inline.bomb_countries_inline_keyboard import get_bomb_countries_inline_keyboard
from templates.templates import render_template


async def bomb_command(message: Message, db: Session = next(get_db())):
    """"""
    other_countries = get_not_user_countries(message.from_user.id, db)
    ikb = get_bomb_countries_inline_keyboard(other_countries)

    await message.answer(
        render_template('orders/choose_country_for_bomb.j2'),
        parse_mode='HTML', reply_markup=ikb)
    await message.delete()


async def bomb_cancel_command(
    message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.BOMB.value, db)
    user_country = get_country_by_user_id(message.from_user.id, db)
    async with state.proxy() as data:
        data['order'].price -= len(data['order'].bomb) * order_action.price
        data['order'].bomb_city = set()
        order_state = data['order']

    kb = get_order_keyboard()
    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()


async def bomb_country_callback(
    callback: CallbackQuery,
    callback_data: Dict[str, Any],
    db: Session = next(get_db()),
):
    """"""
    kb = get_order_keyboard()

    cities = get_cities_by_country_name(callback_data['country_name'], db)
    cities_to_bomb = []
    for city in cities:
        if city.is_alive:
            cities_to_bomb.append(city)

    if not cities_to_bomb:
        await callback.message.answer(
            render_template('orders/all_country_cities_are_bombed.j2'),
            parse_mode='HTML', reply_markup=kb)
        await callback.answer(f'Ошибка!')
        return

    ikb = get_bomb_cities_inline_keyboard(cities_to_bomb)

    await callback.message.answer(
        render_template('orders/choose_city_for_bomb.j2'),
        parse_mode='HTML', reply_markup=ikb)
    await callback.answer(f'Для бомбардировки выбрана страна: {callback_data["country_name"]}!')


async def bomb_city_callback(
    callback: CallbackQuery,
    callback_data: Dict[str, Any],
    state: FSMContext,
    db: Session = next(get_db()),
):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.BOMB.value, db)
    user_country = get_country_by_user_id(callback.from_user.id, db)
    async with state.proxy() as data:
        if user_country.budget < data['order'].price + order_action.price:
            await callback.message.answer(
                render_template('orders/not_enough_money.j2'),
                parse_mode='HTML', reply_markup=kb)
            await callback.answer(f'Ошибка!')
        if callback_data['city_name'] in data['order'].bomb_city:
            await callback.message.answer(
                render_template('orders/order_has_already_bomb.j2',
                                data={'city_name': callback_data['city_name']}),
                parse_mode='HTML', reply_markup=kb)
            await callback.answer(f'Ошибка!')
            return
        if len(data['order'].bomb_city) + 1 > user_country.bombs_number:
            await callback.message.answer(
                render_template('orders/not_enough_bombs.j2',
                                data={'city_name': callback_data['city_name']}),
                parse_mode='HTML', reply_markup=kb)
            await callback.answer(f'Ошибка!')
            return

        data['order'].price += order_action.price
        data['order'].bomb_city.add(callback_data['city_name'])
        order_state = data['order']

    await callback.message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await callback.answer(f'Для бомбардировки выбран город: {callback_data["city_name"]}!')
