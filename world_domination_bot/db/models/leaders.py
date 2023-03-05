""""""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

from db.base_class import Base


class Leader(Base):
    """Presents a user in a session."""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('user.user_id'))
    session_id = Column(Integer, ForeignKey('gamesession.id'))

    user= relationship('User', back_populates='leaders')
    session_country = relationship('SessionCountry', back_populates='leader')
    session = relationship('GameSession', back_populates='leaders')

    __table_args__ = (
        UniqueConstraint('user_id', 'session_id', name='_user_session_uc'),
    )
