from aiogram.types import Message
from sqlalchemy.orm import Session

from common.config import TEST_MODE
from db.session import get_db
from db.services.leaders import update_leader_by_name
from keyboards.default.init_keyboard import get_init_keyboard
from templates.templates import render_template


async def start_command(message: Message, db: Session = next(get_db())):
    """"""
    kb = get_init_keyboard()
    if TEST_MODE:
        update_leader_by_name('Си Цзиньпин', db, user_id=message.from_user.id)

    await message.answer(render_template('start/start.j2'), parse_mode='HTML', reply_markup=kb)
    await message.delete()
