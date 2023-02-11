from sqlalchemy.orm import Session

from db.models.leaders import Leader


def create_leader(
    name: str,
    user_id: int,
    country_name: str,
    session_id: int,
    db: Session,
):
    """"""
    leader = Leader(
        name=name,
        user_id=user_id,
        country_name=country_name,
        session_id=session_id,
    )
    db.add(leader)
    db.commit()
