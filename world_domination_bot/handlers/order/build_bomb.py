from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.enums import OrderAction
from db.services.game_sessions import get_active_session_by_user_id
from db.services.session_countries import get_country_by_user_id_and_session_id
from db.services.order_actions import get_order_action_by_action_name
from db.session import get_db
from keyboards.default.order_keyboard import get_order_keyboard
from templates.templates import render_template


async def build_bomb_command(message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.BUILD_BOMB.value, db)
    session = get_active_session_by_user_id(message.from_user.id, db)
    user_country = get_country_by_user_id_and_session_id(message.from_user.id, session.id, db=db)
    async with state.proxy() as data:
        if user_country.has_nuke_tech == False:
            await message.answer(
                render_template('orders/do_not_have_nuke_tech.j2'),
                parse_mode='HTML', reply_markup=kb)
            await message.delete()
            return
        if user_country.budget < data['order'].price + order_action.price:
            await message.answer(
                render_template('orders/not_enough_money.j2'),
                parse_mode='HTML', reply_markup=kb)
            await message.delete()
            return

        data['order'].price += order_action.price
        data['order'].build_bomb += 1
        order_state = data['order']

    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()


async def build_bomb_cancel_command(
    message: Message,
    state: FSMContext,
    db: Session = next(get_db())
):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.BUILD_BOMB.value, db)
    session = get_active_session_by_user_id(message.from_user.id, db)
    user_country = get_country_by_user_id_and_session_id(message.from_user.id, session.id, db=db)
    async with state.proxy() as data:
        data['order'].price -= data['order'].build_bomb * order_action.price
        data['order'].build_bomb = 0
        order_state = data['order']

    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()
