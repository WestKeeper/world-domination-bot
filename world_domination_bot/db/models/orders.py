""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from db.base_class import Base


class Order(Base):
    """For checking are all orders sent and for final analytics"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    price = Column(Integer, nullable=False)
    nuke_tech = Column(Boolean, nullable=False)
    build_bomb = Column(Integer, nullable=False)
    dev_eco = Column(Boolean, nullable=False)

    user_id = Column(Integer, ForeignKey('user.user_id'))
    round_id = Column(Integer, ForeignKey('round.id'))

    user = relationship('User', back_populates='orders')
    round = relationship('Round', back_populates='orders')
    ordered_bomb_cities = relationship('OrderedBombCity', back_populates='order')
    ordered_build_shield_cities = relationship('OrderedBuildShieldCity', back_populates='order')
    ordered_dev_cities = relationship('OrderedDevCity', back_populates='order')
    ordered_sent_money_countries = relationship('OrderedSentMoneyCountry', back_populates='order')
