from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.enums import OrderAction
from db.services.countries import get_country_by_user_id
from db.services.order_actions import get_order_action_by_action_name
from db.session import get_db
from keyboards.default.order_keyboard import get_order_keyboard
from templates.templates import render_template


async def nuke_tech_command(message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.NUKE_TECH.value, db)
    user_country = get_country_by_user_id(message.from_user.id, db)
    async with state.proxy() as data:
        if user_country.nuke_tech:
            await message.answer(
                render_template('orders/country_has_already_nuke_tech.j2'),
                parse_mode='HTML', reply_markup=kb)
            await message.delete()
            return
        if data['order'].nuke_tech:
            await message.answer(
                render_template('orders/order_has_already_nuke_tech.j2'),
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
        data['order'].nuke_tech = True
        order_state = data['order']

    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()


async def nuke_tech_cancel_command(
    message: Message,
    state: FSMContext,
    db: Session = next(get_db())
):
    """"""
    kb = get_order_keyboard()

    order_state = None
    order_action = get_order_action_by_action_name(OrderAction.NUKE_TECH.value, db)
    user_country = get_country_by_user_id(message.from_user.id, db)
    async with state.proxy() as data:
        data['order'].price -= order_action.price
        data['order'].nuke_tech = False
        order_state = data['order']

    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()
