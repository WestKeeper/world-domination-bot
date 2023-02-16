from sqlalchemy.orm import Session

from common.config import START_BUILD_BOMBS_NUM
from common.config import START_DEV_ECO_NUM
from common.config import START_DROP_BOMBS_NUM
from common.config import START_ECOLOGY_LEVEL
from common.config import START_NUKE_TECH_NUM
from common.order_lib.calculate_ecology_level import calculate_ecology_level
from db.models.game_sessions import GameSession
from db.models.leaders import Leader
from schemas.game_sessions import GameSessionShow


def create_session(
    host_user_id: int,
    db: Session,
    *,
    ecology_level: int = START_ECOLOGY_LEVEL,
    build_bombs_num: int = START_BUILD_BOMBS_NUM,
    drop_bombs_num: int = START_DROP_BOMBS_NUM,
    nuke_tech_num: int = START_NUKE_TECH_NUM,
    dev_eco_num: int = START_DEV_ECO_NUM,
):
    """"""
    session = GameSession(
        host_id=host_user_id,
        ecology_level=ecology_level,
        build_bombs_num=build_bombs_num,
        drop_bombs_num=drop_bombs_num,
        nuke_tech_num=nuke_tech_num,
        dev_eco_num = dev_eco_num,
    )

    session_show = GameSessionShow(
        id=session.id,
        ecology_level=session.ecology_level,
    )

    db.add(session)
    db.commit()

    return session_show


def get_session_by_user_id(
    user_id: int,
    db: Session,
) -> GameSessionShow:
    """"""
    session = db.query(GameSession).join(Leader).filter(Leader.user_id == user_id).one()
    session_show = GameSessionShow(id=session.id, ecology_level=session.ecology_level)

    return session_show


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
