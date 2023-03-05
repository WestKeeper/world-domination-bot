""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class SessionCountry(Base):
    """Linked with Session by Leader"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    budget = Column(Integer, nullable=False)
    has_nuke_tech = Column(Boolean, nullable=False)
    bombs_number = Column(Integer, nullable=False)

    country_name = Column(String, ForeignKey('country.name'))
    leader_id = Column(Integer, ForeignKey('leader.id'))

    country = relationship('Country', back_populates='session_countries')
    session_cities = relationship('SessionCity', back_populates='session_country')
    ordered_sent_money_countries = relationship(
        'OrderedSentMoneyCountry', back_populates='session_country')
    leader = relationship('Leader', back_populates='session_country')
