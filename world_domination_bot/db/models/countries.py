""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Country(Base):
    name = Column(String, primary_key=True, index=True)
    budget = Column(Integer, nullable=False)
    has_nuke_tech = Column(Boolean, nullable=False)
    bombs_number = Column(Integer, nullable=False)
    drop_after_db_cleaned = Column(Boolean, nullable=False)
    cities = relationship('City', back_populates='country')
    leader = relationship('Leader', back_populates='country')
