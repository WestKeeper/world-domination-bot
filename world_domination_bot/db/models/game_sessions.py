""""""
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from db.base_class import Base


class GameSession(Base):
    """"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ecology_level = Column(Integer, nullable=False)
    build_bombs_num = Column(Integer, nullable=False)
    drop_bombs_num = Column(Integer, nullable=False)
    nuke_tech_num = Column(Integer, nullable=False)
    dev_eco_num = Column(Integer, nullable=False)
    leaders = relationship('Leader', back_populates='session')
