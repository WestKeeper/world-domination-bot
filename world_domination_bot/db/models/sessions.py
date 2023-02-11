""""""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Session(Base):
    """"""
    id = Column(Integer, primary_key=True, index=True)
    leaders = relationship('Leader', back_populates='session')
