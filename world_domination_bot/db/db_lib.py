from db.base import Base
from db.session import engine
from common.config import NOT_TO_DROP_TABLES
from common.config import TO_GENERATE_AND_DROP_DB


def create_tables():
    """"""
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """"""
    for table in Base.metadata.sorted_tables:
        if TO_GENERATE_AND_DROP_DB and table.name in NOT_TO_DROP_TABLES:
          table.drop(engine, checkfirst=False)
