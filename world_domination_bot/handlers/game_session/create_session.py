from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.game_sessions import connect_user_to_session
from db.services.game_sessions import create_session
from db.services.game_sessions import delete_sessions_by_host_user_id
from db.services.game_sessions import get_session_by_host_user_id
from db.session import get_db
from keyboards.default.host_session_keyboard import get_host_session_keyboard
from templates.templates import render_template


async def create_session_command(message: Message, db: Session = next(get_db())):
    """"""
    delete_sessions_by_host_user_id(host_user_id=message.from_user.id, db=db)
    create_session(host_user_id=message.from_user.id, db=db)
    session = get_session_by_host_user_id(host_user_id=message.from_user.id, db=db)
    connect_user_to_session(session_id=session.id, user_id=message.from_user.id, db=db)

    kb = get_host_session_keyboard()
    await message.answer(
        render_template('game_sessions/create_session.j2', {'session': session}),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()
