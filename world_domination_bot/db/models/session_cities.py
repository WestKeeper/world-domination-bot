""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class SessionCity(Base):
    """"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    has_shield = Column(Boolean, nullable=False)
    development = Column(Integer, nullable=False)
    development_number = Column(Integer, nullable=False)
    life_level = Column(Integer, nullable=False)
    is_alive = Column(Boolean, nullable=False)

    city_name = Column(String, ForeignKey('city.name'))
    session_country_id = Column(String, ForeignKey('sessioncountry.id'))

    city = relationship('City', back_populates='session_cities')
    session_country = relationship('SessionCountry', back_populates='session_cities')
    ordered_bomb_cities = relationship('OrderedBombCity', back_populates='session_city')
    ordered_build_shield_cities = relationship(
        'OrderedBuildShieldCity', back_populates='session_city')
    ordered_dev_cities = relationship('OrderedDevCity', back_populates='session_city')
