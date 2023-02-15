""""""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Leader(Base):
    name = Column(String, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, unique=True)
    country_name = Column(Integer, ForeignKey('country.name'))
    session_id = Column(Integer, ForeignKey('gamesession.id'))
    country = relationship('Country', back_populates='leader')
    session = relationship('GameSession', back_populates='leaders')
