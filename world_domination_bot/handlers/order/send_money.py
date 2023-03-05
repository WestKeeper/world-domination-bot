from typing import Any, Dict

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.enums import OrderAction
from db.services.game_sessions import get_active_session_by_user_id
from db.services.session_countries import get_not_user_countries
from db.services.session_countries import get_country_by_user_id_and_session_id
from db.services.order_actions import get_order_action_by_action_name
from db.session import get_db
from keyboards.default.order_keyboard import get_order_keyboard
from keyboards.inline.send_money_inline_keyboard import get_send_money_inline_keyboard
from states.game_states_group import GameStatesGroup
from states.order_states_group import OrderStatesGroup
from templates.templates import render_template


async def send_money_command(message: Message, db: Session = next(get_db())):
    """"""
    other_countries = get_not_user_countries(message.from_user.id, db)
    ikb = get_send_money_inline_keyboard(other_countries)

    await message.answer(
        render_template('orders/choose_country_for_send_money.j2'),
        parse_mode='HTML', reply_markup=ikb)
    await message.delete()


async def send_money_cancel_command(
    message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.SEND_MONEY.value, db)
    session = get_active_session_by_user_id(message.from_user.id, db)
    user_country = get_country_by_user_id_and_session_id(message.from_user.id, session.id, db=db)
    async with state.proxy() as data:
        data['order'].price -= len(data['order'].send_money) * order_action.price
        data['order'].send_money = {}
        order_state = data['order']

    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()


async def send_money_amount_callback(
    callback: CallbackQuery,
    callback_data: Dict[str, Any],
    state: FSMContext,
):
    """"""
    await OrderStatesGroup.money.set()
    async with state.proxy() as data:
        data['send_money'] = {'country_name': callback_data['country_name']}

    await callback.message.answer(
        render_template('orders/choose_send_money_amount.j2',
                        data={'country_name': callback_data['country_name']}),
        parse_mode='HTML')
    await callback.answer(f'Для отправки денег выбрана страна: {callback_data["country_name"]}!')


async def send_money_validate_command(message: Message):
    """"""
    await message.reply(
        render_template('orders/validate_send_money_amount.j2'),
        parse_mode='HTML')


async def send_money_amount_command(
    message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.SEND_MONEY.value, db)
    session = get_active_session_by_user_id(message.from_user.id, db)
    user_country = get_country_by_user_id_and_session_id(message.from_user.id, session.id, db=db)
    async with state.proxy() as data:
        if user_country.budget < data['order'].price + order_action.price:
            await message.answer(
                render_template('orders/not_enough_money.j2'),
                parse_mode='HTML', reply_markup=kb)
            await message.delete()
            await GameStatesGroup.order.set()
            return
        if user_country.budget < data['order'].price + order_action.price + int(message.text):
            await message.answer(
                render_template('orders/not_enough_money_to_send.j2'),
                parse_mode='HTML', reply_markup=kb)
            await message.delete()
            await GameStatesGroup.order.set()
            return
        if data['send_money']['country_name'] in data['order'].send_money:
            await message.answer(
                render_template('orders/order_has_already_send_money.j2',
                                data={'country_name': data['send_money']['country_name']}),
                parse_mode='HTML', reply_markup=kb)
            await GameStatesGroup.order.set()
            return

        data['order'].price += order_action.price + int(message.text)
        data['order'].send_money[data['send_money']['country_name']] = int(message.text)
        order_state = data['order']

    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()
    await GameStatesGroup.order.set()
