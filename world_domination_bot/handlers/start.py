from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import Session

from common.config import TEST_MODE
from db.session import get_db
# from db.services.leaders import update_leader_by_name
from db.services.users import create_user
from db.services.users import get_user_by_id
from keyboards.default.empty_keyboard import get_empty_keyboard
from keyboards.default.init_keyboard import get_init_keyboard
from states.game_states_group import GameStatesGroup
from templates.templates import render_template


async def start_command(message: Message, db: Session = next(get_db())):
    """"""
    if TEST_MODE:
        update_leader_by_name('Си Цзиньпин', db=db, user_id=message.from_user.id)

    user = get_user_by_id(user_id=message.from_user.id, db=db)

    if user is not None:
        kb = get_init_keyboard()
        await GameStatesGroup.session_connection.set()
        await message.answer(
            render_template('start/start_with_user_name.j2',
                            data={'user': user}),
            parse_mode='HTML', reply_markup=kb)
        await message.delete()
        return

    kb = get_empty_keyboard()
    await GameStatesGroup.create_user.set()
    await message.answer(
        render_template('start/ask_user_name.j2'), parse_mode='HTML', reply_markup=kb)
    await message.delete()


async def create_user_command(message: Message, db: Session = next(get_db())):
    """"""
    await GameStatesGroup.session_connection.set()
    create_user(user_id=message.from_user.id, name=str(message.text), db=db)
    user = get_user_by_id(user_id=message.from_user.id, db=db)

    kb = get_init_keyboard()

    await message.answer(
        render_template('start/start_with_user_name.j2',
                        data={'user': user}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()
