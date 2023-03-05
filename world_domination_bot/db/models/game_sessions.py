""""""
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
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
    game_is_processing = Column(Boolean, nullable=False)
    max_rounds = Column(Integer, nullable=False)
    round_time = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False)

    users = relationship('User', back_populates='session')
    host_session = relationship('HostSession', back_populates='session')
    rounds = relationship('Round', back_populates='session')
    leaders = relationship('Leader', back_populates='session')
