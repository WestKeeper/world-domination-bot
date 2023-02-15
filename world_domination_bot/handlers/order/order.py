from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.countries import get_country_by_user_id
from db.session import get_db
from keyboards.default.order_keyboard import get_order_keyboard
from schemas.orders import OrderState
from states.game_states_group import GameStatesGroup
from templates.templates import render_template


async def order_command(message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    kb = get_order_keyboard()

    await GameStatesGroup.order.set()

    order_state = None
    user_country = get_country_by_user_id(message.from_user.id, db)
    async with state.proxy() as data:
        data['order'] = OrderState(
            price=0,
            nuke_tech=False,
            build_bomb=0,
            dev_city=set(),
            send_money={},
            build_shield=set(),
            dev_eco=False,
            bomb_city=set(),
        )
        order_state = data['order']

    await message.answer(
        render_template('orders/order.j2', data={'order': order_state,
                                                 'current_money': user_country.budget,
                                                 'bomb_number': user_country.bombs_number}),
        parse_mode='HTML', reply_markup=kb,
    )
    await message.delete()
