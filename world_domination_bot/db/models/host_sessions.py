""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from db.base_class import Base


class HostSession(Base):
    """"""
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey('user.user_id'))
    session_id = Column(Integer, ForeignKey('gamesession.id'))

    session = relationship('GameSession', back_populates='host_session')
    host_user = relationship('User', back_populates='host_sessions')
