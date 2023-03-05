from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.game_sessions import get_session_by_user_id
from db.services.game_sessions import get_session_users
from db.session import get_db
from templates.templates import render_template


async def session_status_command(message: Message, db: Session = next(get_db())):
    """"""
    session = get_session_by_user_id(user_id=message.from_user.id, db=db)
    users = get_session_users(session_id=session.id, db=db)

    await message.answer(
        render_template('game_sessions/session_status.j2', {'session': session,
                                                            'users': users}),
                        parse_mode='HTML')
    await message.delete()
