""""""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    """"""
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    session_id = Column(Integer, ForeignKey('gamesession.id'))

    session = relationship('GameSession', back_populates='users')
    host_sessions = relationship('HostSession', back_populates='host_user')
    orders = relationship('Order', back_populates='user')
    leaders = relationship('Leader', back_populates='user')
