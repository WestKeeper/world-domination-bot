""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class City(Base):
    """"""
    name = Column(String, primary_key=True, index=True)
    init_has_shield = Column(Boolean, nullable=False)
    init_development = Column(Integer, nullable=False)
    init_life_level = Column(Integer, nullable=False)

    country_name = Column(String, ForeignKey('country.name'))

    country = relationship('Country', back_populates='cities')
    session_cities = relationship('SessionCity', back_populates='city')
