""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class City(Base):
    name = Column(String, primary_key=True, index=True)
    country_name = Column(String, ForeignKey('country.name'))
    has_shield = Column(Boolean, nullable=False)
    init_development = Column(Integer, nullable=False)
    development = Column(Integer, nullable=False)
    development_number = Column(Integer, nullable=False)
    life_level = Column(Integer, nullable=False)
    is_alive = Column(Boolean, nullable=False)
    country = relationship('Country', back_populates='cities')
