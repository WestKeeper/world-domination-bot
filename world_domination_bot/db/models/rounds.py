""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from db.base_class import Base


class Round(Base):
    """"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False)
    session_id = Column(Integer, ForeignKey('gamesession.id'))

    session = relationship('GameSession', back_populates='rounds')
    orders = relationship('Order', back_populates='round')
