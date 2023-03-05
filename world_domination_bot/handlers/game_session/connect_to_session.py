from typing import Any, Dict

from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.game_sessions import connect_user_to_session
from db.services.game_sessions import get_session_host_user
from db.services.game_sessions import get_session_by_id
from db.services.game_sessions import get_session_users
from db.services.game_sessions import get_sessions
from db.services.users import check_is_user_host
from db.services.users import get_user_by_id
from db.session import get_db
from keyboards.default.host_session_keyboard import get_host_session_keyboard
from keyboards.default.member_session_keyboard import get_member_session_keyboard
from keyboards.inline.sessions_inline_keyboard import get_sessions_inline_keyboard
from templates.templates import render_template


async def connect_to_session_command(message: Message, db: Session = next(get_db())):
    """"""
    sessions = get_sessions(db=db)
    not_active_sessions = [session for session in sessions if not session.is_active]
    if not sessions:
        await message.answer(render_template('game_sessions/no_sessions.j2'), parse_mode='HTML')
        await message.delete()
        return

    ikb = get_sessions_inline_keyboard(not_active_sessions)

    await message.answer(
        render_template('game_sessions/choose_sessions.j2'),
        parse_mode='HTML', reply_markup=ikb)
    await message.delete()


async def connect_to_session_callback(
    callback: CallbackQuery,
    callback_data: Dict[str, Any],
    db: Session = next(get_db()),
):
    """"""
    is_user_host = check_is_user_host(
        session_id=callback_data['session_id'], user_id=callback.from_user.id, db=db)
    kb = get_host_session_keyboard() if is_user_host else get_member_session_keyboard()

    connect_user_to_session(
        session_id=callback_data['session_id'], user_id=callback.from_user.id, db=db)
    session = get_session_by_id(session_id=callback_data['session_id'], db=db)
    users = get_session_users(session_id=callback_data['session_id'], db=db)

    await callback.message.answer(
        render_template('game_sessions/connected_to_session.j2', {'session': session,
                                                                  'users': users}),
                        parse_mode='HTML', reply_markup=kb)
    await callback.answer(f'Подключились к сессии {callback_data["session_id"]}!')

    if not is_user_host:
        this_user = get_user_by_id(user_id=callback.from_user.id, db=db)
        host_user = get_session_host_user(session_id=callback_data['session_id'], db=db)
        bot = Bot.get_current()
        await bot.send_message(host_user.user_id,
                               render_template('game_sessions/user_connected_to_session.j2',
                                               {'user': this_user,
                                                'session': session}),
                                                parse_mode='HTML')
