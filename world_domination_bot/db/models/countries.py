""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Country(Base):
    """"""
    name = Column(String, primary_key=True, index=True)
    init_budget = Column(Integer, nullable=False)

    cities = relationship('City', back_populates='country')
    session_countries = relationship('SessionCountry', back_populates='country')
