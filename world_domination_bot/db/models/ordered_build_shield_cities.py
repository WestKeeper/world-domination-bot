""""""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class OrderedBuildShieldCity(Base):
    """"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    session_city_id = Column(Integer, ForeignKey('sessioncity.id'))
    order_id = Column(Integer, ForeignKey('order.id'))

    session_city = relationship('SessionCity', back_populates='ordered_build_shield_cities')
    order = relationship('Order', back_populates='ordered_build_shield_cities')
