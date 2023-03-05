from typing import Optional
from sqlalchemy.orm import Session

from db.base import GameSession
from db.base import HostSession
from db.base import User
from schemas.users import UserShow


def create_user(
    user_id: int,
    name: str,
    db: Session,
    *,
    session_id: Optional[int] = None,
):
    """"""
    exists = db.query(User).filter(User.user_id == user_id).first()

    if not exists:
        user = User(
            user_id=user_id,
            name=name,
            session_id=session_id,
        )
        db.add(user)
        db.commit()


def get_user_by_id(
    user_id: int,
    db: Session,
):
    """"""
    user = db.query(User).filter(User.user_id == user_id).first()

    user_show = UserShow(user_id=user.user_id, name=user.name, session_id=user.session_id) \
        if user is not None else None

    return user_show


def disconnect_user_from_session(
    user_id: int,
    db: Session,
):
    """"""
    user = db.query(User).filter(User.user_id == user_id).one()
    user.session_id = None
    db.commit()


def check_is_user_host(
    session_id: int,
    user_id: int,
    db: Session,
):
    """"""
    _, host_session = db.query(GameSession, HostSession) \
        .join(HostSession) \
        .filter(GameSession.id == session_id) \
        .one()

    return True if host_session.user_id == user_id else False
