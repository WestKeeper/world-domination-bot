from sqlalchemy.orm import Session

from db.models.sessions import Session


def create_session(
    id: int,
    db: Session,
):
    """"""
    country = Session(
        id=id,
    )
    db.add(country)
    db.commit()
