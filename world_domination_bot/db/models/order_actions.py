""""""
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db.base_class import Base


class OrderAction(Base):
    name = Column(String, primary_key=True, index=True)
    price = Column(Integer, nullable=False)
