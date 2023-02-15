from sqlalchemy.orm import Session

from db.enums import OrderAction
from db.services.leaders import create_leader
from db.services.cities import create_city
from db.services.countries import create_country
from db.services.game_sessions import create_session
from db.services.order_actions import create_order_action


def create_pricelist(db: Session):
    """"""
    create_order_action(name=OrderAction.NUKE_TECH.value, price=500, db=db)
    create_order_action(name=OrderAction.BUILD_BOMB.value, price=150, db=db)
    create_order_action(name=OrderAction.DEV_CITY.value, price=150, db=db)
    create_order_action(name=OrderAction.SEND_MONEY.value, price=0, db=db)
    create_order_action(name=OrderAction.BUILD_SHIELD.value, price=300, db=db)
    create_order_action(name=OrderAction.DEV_ECO.value, price=200, db=db)
    create_order_action(name=OrderAction.BOMB.value, price=0, db=db)


def create_north_korea(session_id: int, user_id: int, db: Session):
    """"""
    create_country(
        name='Северная Корея',
        budget=1000,
        has_nuke_tech=False,
        bombs_number=0,
        drop_after_db_cleaned=True,
        db=db,
    )
    create_city(
        name='Пхеньян',
        country_name='Северная Корея',
        has_shield=True,
        init_development=80,
        development=80,
        development_number=0,
        life_level=72,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Кэсон',
        country_name='Северная Корея',
        has_shield=True,
        init_development=60,
        development=60,
        development_number=0,
        life_level=54,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Расон',
        country_name='Северная Корея',
        has_shield=False,
        init_development=60,
        development=60,
        development_number=0,
        life_level=54,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Пусан',
        country_name='Северная Корея',
        has_shield=False,
        init_development=40,
        development=40,
        development_number=0,
        life_level=36,
        is_alive=True,
        db=db,
    )
    create_leader(
        name='Ким Чен Ын',
        user_id=user_id,
        country_name='Северная Корея',
        session_id=session_id,
        db=db,
    )


def create_china(session_id: int, user_id: int, db: Session):
    """"""
    create_country(
        name='Китай',
        budget=1000,
        has_nuke_tech=False,
        bombs_number=0,
        drop_after_db_cleaned=True,
        db=db,
    )
    create_city(
        name='Пекин',
        country_name='Китай',
        has_shield=True,
        init_development=80,
        development=80,
        development_number=0,
        life_level=72,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Шанхай',
        country_name='Китай',
        has_shield=True,
        init_development=60,
        development=60,
        development_number=0,
        life_level=54,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Гуанчжоу',
        country_name='Китай',
        has_shield=False,
        init_development=60,
        development=60,
        development_number=0,
        life_level=54,
        is_alive=True,
        db=db,
    )
    create_city(
        name='Гонконг',
        country_name='Китай',
        has_shield=False,
        init_development=40,
        development=40,
        development_number=0,
        life_level=36,
        is_alive=True,
        db=db,
    )
    create_leader(
        name='Си Цзиньпин',
        user_id=user_id,
        country_name='Китай',
        session_id=session_id,
        db=db,
    )


def generate_test_session(db: Session):
    """"""
    create_pricelist(db)
    create_session(
        id=0,
        ecology_level=90,
        build_bombs_num=0,
        drop_bombs_num=0,
        nuke_tech_num=0,
        dev_eco_num=0,
        db=db,
    )
    create_north_korea(session_id=0, user_id=228228, db=db)
    create_china(session_id=0, user_id=1, db=db)
