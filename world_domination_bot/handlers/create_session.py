from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.game_sessions import create_session_by_user_id
from db.session import get_db
from templates.templates import render_template


async def create_session(message: Message, db: Session = next(get_db())):
    """"""
    # TODO(SemenyutaAV): mb better to create a leader previously?
    session = create_session_by_user_id(host_id=message.from_user.id, db=db)
    await message.answer(
        render_template('game_sessions/create_session.j2', {'session': session}), parse_mode='HTML')
    await message.delete()
