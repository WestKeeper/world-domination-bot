from aiogram import Bot
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.game_sessions import get_session_by_user_id
from db.services.game_sessions import get_session_host_user
from db.services.users import check_is_user_host
from db.services.users import get_user_by_id
from db.services.users import disconnect_user_from_session
from db.session import get_db
from keyboards.default.init_keyboard import get_init_keyboard
from templates.templates import render_template


async def disconnect_from_session_command(message: Message, db: Session = next(get_db())):
    """"""
    session = get_session_by_user_id(user_id=message.from_user.id, db=db)
    is_user_host = check_is_user_host(
        session_id=session.id, user_id=message.from_user.id, db=db)

    kb = get_init_keyboard()
    disconnect_user_from_session(user_id=message.from_user.id, db=db)
    await message.answer(
        render_template('game_sessions/disconnect_from_session.j2'),
        parse_mode='HTML', reply_markup=kb)
    await message.delete()

    if not is_user_host:
        this_user = get_user_by_id(user_id=message.from_user.id, db=db)
        host_user = get_session_host_user(session_id=session.id, db=db)
        bot = Bot.get_current()
        await bot.send_message(host_user.user_id,
                               render_template('game_sessions/user_disconnected_from_session.j2',
                                               {'user': this_user,
                                                'session': session}),
                                                parse_mode='HTML')

