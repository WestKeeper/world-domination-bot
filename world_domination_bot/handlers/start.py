from aiogram.types import Message
from sqlalchemy.orm import Session

from db.session import get_db
from keyboards.default.init_keyboard import get_init_keyboard
from templates.templates import render_template


async def start_command(message: Message, db: Session = next(get_db())):
    """"""
    kb = get_init_keyboard()
    await message.answer(render_template('start/start.j2'), parse_mode='HTML', reply_markup=kb)
    await message.delete()
