from typing import List
from sqlalchemy.orm import Session

from db.base import Round
from schemas.rounds import RoundShow


def create_round(
    number: int,
    is_active: bool,
    session_id: int,
    db: Session,
):
    """"""
    round = Round(
        number=number,
        is_active=is_active,
        session_id=session_id,
    )
    db.add(round)
    db.commit()


def get_active_round(
    session_id: int,
    db: Session,
):
    """"""
    round = db.query(Round).filter(Round.session_id == session_id, Round.is_active == True).one()
    round_show = RoundShow(
        number=round.number,
        is_active=round.is_active,
        session_id=round.session_id,
    )

    return round_show


def activate_round(
    number: int,
    session_id: int,
    db: Session,
):
    """"""
    round = db.query(Round).filter(Round.session_id == session_id, Round.number == number).one()
    round.is_active = True
    db.commit()
