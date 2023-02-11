from db.base import Base
from db.session import engine


def create_tables():
    """"""
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """"""
    for table in Base.metadata.sorted_tables:
        table.drop(engine, checkfirst=False)
