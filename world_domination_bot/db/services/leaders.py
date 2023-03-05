from sqlalchemy.orm import Session

from db.base import Leader
from schemas.leaders import LeaderShow


def create_leader(
    user_id: int,
    session_id: int,
    db: Session,
):
    """"""
    leader = Leader(
        user_id=user_id,
        session_id=session_id,
    )
    db.add(leader)
    db.commit()


def get_leader_by_user_id_n_session_id(
    user_id: int,
    session_id: int,
    db: Session,
):
    """"""
    leader = db.query(Leader) \
        .filter(Leader.user_id == user_id,
                Leader.session_id == session_id) \
        .one()

    leader_show = LeaderShow(leader.id, leader.user_id, leader.session_id)

    return leader_show
