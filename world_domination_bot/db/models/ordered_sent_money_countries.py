""""""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class OrderedSentMoneyCountry(Base):
    """"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    money_amount = Column(Integer, nullable=False)

    session_country_id = Column(Integer, ForeignKey('sessioncountry.id'))
    order_id = Column(Integer, ForeignKey('order.id'))

    session_country = relationship('SessionCountry', back_populates='ordered_sent_money_countries')
    order = relationship('Order', back_populates='ordered_sent_money_countries')
