from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import Session

from common.order_lib.execute_order import execute_order
from db.session import get_db
from keyboards.default.init_keyboard import get_init_keyboard
from templates.templates import render_template


async def send_order_command(message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    kb = get_init_keyboard()

    order_state = None
    async with state.proxy() as data:
        order_state = data['order']

    execute_order(order_state, message.from_user.id, db)

    await message.answer(
        render_template('orders/send_order.j2'),parse_mode='HTML', reply_markup=kb)
    await message.delete()
    await state.finish()
