from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default.init_keyboard import get_init_keyboard
from schemas.orders import OrderState
from templates.templates import render_template


async def cancel_order_command(message: Message, state: FSMContext):
    """"""
    kb = get_init_keyboard()

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

    await message.answer(
        render_template('orders/cancel_order.j2'),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()
    await state.finish()
