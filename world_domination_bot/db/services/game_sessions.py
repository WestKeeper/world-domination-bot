from typing import List

from sqlalchemy.orm import Session

from common.config import GAME_IS_PROCESSING
from common.config import MAX_ROUNDS
from common.config import ROUND_TIME
from common.config import START_BUILD_BOMBS_NUM
from common.config import START_DEV_ECO_NUM
from common.config import START_DROP_BOMBS_NUM
from common.config import START_ECOLOGY_LEVEL
from common.config import START_NUKE_TECH_NUM
from common.order_lib.calculate_ecology_level import calculate_ecology_level
from db.base import GameSession
from db.base import HostSession
from db.base import Leader
from db.base import Round
from db.base import User
from schemas.game_sessions import GameSessionShow
from schemas.users import UserShow


def create_session(
    host_user_id: int,
    db: Session,
    *,
    ecology_level: int = START_ECOLOGY_LEVEL,
    build_bombs_num: int = START_BUILD_BOMBS_NUM,
    drop_bombs_num: int = START_DROP_BOMBS_NUM,
    nuke_tech_num: int = START_NUKE_TECH_NUM,
    dev_eco_num: int = START_DEV_ECO_NUM,
    game_is_processing: bool = GAME_IS_PROCESSING,
    max_rounds: int = MAX_ROUNDS,
    round_time: int = ROUND_TIME,
    is_active: bool = False,
):
    """"""
    host_session = HostSession(
        user_id=host_user_id,
        session=GameSession(
            ecology_level=ecology_level,
            build_bombs_num=build_bombs_num,
            drop_bombs_num=drop_bombs_num,
            nuke_tech_num=nuke_tech_num,
            dev_eco_num = dev_eco_num,
            game_is_processing=game_is_processing,
            max_rounds=max_rounds,
            round_time=round_time,
            is_active=is_active,
            rounds=[
                Round(
                    number=i + 1,
                    is_active=False,
                )
                for i in range(max_rounds)
            ],
        )
    )
    db.add(host_session)
    db.commit()


def get_sessions(
    db: Session,
):
    """"""
    game_n_host_sessions = db.query(GameSession, HostSession) \
        .join(HostSession) \
        .all()

    session_shows = []
    for session, host_session in game_n_host_sessions:
        session_show = GameSessionShow(
            id=session.id, host_user_id=host_session.user_id,
            ecology_level=session.ecology_level, is_active=session.is_active)
        session_shows.append(session_show)

    return session_shows


def activate_game_session_by_session_id(
    session_id: int,
    db: Session,
):
    """"""
    session = db.query(GameSession) \
        .filter(GameSession.id == session_id) \
        .one()

    session.is_active = True
    db.commit()


def get_session_by_id(
    session_id: int,
    db: Session,
):
    """"""
    session, host_session = db.query(GameSession, HostSession) \
        .join(HostSession) \
        .filter(GameSession.id == session_id) \
        .one()

    session_show = GameSessionShow(
        id=session.id,
        host_user_id=host_session.user_id,
        ecology_level=session.ecology_level,
        is_active=session.is_active,
    )

    return session_show


def get_active_session_by_user_id(
    user_id: int,
    db: Session,
):
    """"""
    game_session, host_session = db.query(GameSession, HostSession) \
        .join(HostSession) \
        .filter(HostSession.user_id == user_id, GameSession.is_active) \
        .one()
    session_show = GameSessionShow(
        id=host_session.id,
        host_user_id=HostSession.user_id,
        ecology_level=game_session.ecology_level,
        is_active=game_session.is_active,
    )

    return session_show


def get_session_host_user(
    session_id: int,
    db: Session,
) -> UserShow:
    """"""
    _, host_session = db.query(GameSession, HostSession) \
        .join(HostSession) \
        .filter(GameSession.id == session_id) \
        .one()
    host_user = db.query(User).filter(User.user_id == host_session.user_id).one()
    host_user_show = UserShow(
        user_id=host_user.user_id, name=host_user.name, session_id=host_user.session_id)

    return host_user_show


def get_session_by_leader_user_id(
    user_id: int,
    db: Session,
) -> GameSessionShow:
    """"""
    game_session, host_session = db.query(GameSession, HostSession) \
        .join(HostSession) \
        .join(Leader) \
        .filter(Leader.user_id == user_id) \
        .one()
    session_show = GameSessionShow(
        id=game_session.id,
        host_user_id=host_session.user_id,
        ecology_level=game_session.ecology_level,
        is_active=game_session.is_active,
    )

    return session_show


def get_session_users(
    session_id: int,
    db: Session,
) -> List[UserShow]:
    """"""
    users = db.query(User).filter(User.session_id == session_id).all()
    user_shows = []
    for user in users:
        user_show = UserShow(user_id=user.user_id, name=user.name, session_id=user.session_id)
        user_shows.append(user_show)
    return user_shows


def get_session_by_user_id(
    user_id: int,
    db: Session,
) -> List[UserShow]:
    """"""
    _, session = db.query(User, GameSession) \
        .join(GameSession) \
        .filter(User.user_id == user_id) \
        .one()

    _, host_session = db.query(GameSession, HostSession) \
        .join(HostSession) \
        .filter(GameSession.id == session.id) \
        .one()

    session_show = GameSessionShow(
        id=session.id,
        host_user_id=host_session.user_id,
        ecology_level=session.ecology_level,
    )

    return session_show


def get_session_by_host_user_id(
    host_user_id: int,
    db: Session,
) -> GameSessionShow:
    """"""
    session = db.query(GameSession) \
        .join(HostSession) \
        .filter(HostSession.user_id == host_user_id) \
        .one()

    session_show = GameSessionShow(
        id=session.id,
        host_user_id=host_user_id,
        ecology_level=session.ecology_level,
        is_active=session.is_active,
    )

    return session_show


def delete_sessions_by_host_user_id(
    host_user_id: int,
    db: Session,
) -> GameSessionShow:
    """"""
    sessions = db.query(GameSession) \
        .join(HostSession) \
        .filter(HostSession.user_id == host_user_id) \
        .all()

    for session in sessions:
        db.delete(session)

    db.commit()


def develop_ecology_by_user_id(
    user_id: int,
    is_ecology_developed: bool,
    db: Session,
):
    """"""
    if not is_ecology_developed:
        return

    session = db.query(GameSession).join(Leader).filter(Leader.user_id == user_id).one()
    session.dev_eco_num += 1
    session.ecology_level = calculate_ecology_level(
        session.build_bombs_num,
        session.nuke_tech_num,
        session.dev_eco_num,
    )
    db.commit()


def connect_user_to_session(
    session_id: int,
    user_id: int,
    db: Session,
):
    """"""
    user = db.query(User).filter(User.user_id == user_id).one()
    user.session_id = session_id
    db.commit()
