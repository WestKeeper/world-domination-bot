from sqlalchemy.orm import Session

from db.services.leaders import create_leader
from db.services.cities import create_city
from db.services.countries import create_country
from db.services.sessions import create_session


def generate_test_leader(db: Session):
    """"""
    create_session(
        id=0,
        db=db,
    )
    create_country(
        name='Северная Корея',
        budget=1000,
        drop_after_db_cleaned=True,
        db=db,
    )
    create_city(
        name='Пхеньян',
        country_name='Северная Корея',
        has_shield=True,
        development=80,
        life_level=72,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Кэсон',
        country_name='Северная Корея',
        has_shield=True,
        development=60,
        life_level=54,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Расон',
        country_name='Северная Корея',
        has_shield=False,
        development=60,
        life_level=54,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Пусан',
        country_name='Северная Корея',
        has_shield=False,
        development=40,
        life_level=36,
        is_alive=True,
        db=db,
    )
    create_leader(
        name='Ким Чен Ын',
        user_id=228228,
        country_name='Северная Корея',
        session_id=0,
        db=db,
    )
