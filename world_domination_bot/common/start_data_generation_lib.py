from sqlalchemy.orm import Session

from db.enums import OrderAction
from db.services.countries import create_country_if_not_exists
from db.services.cities import create_city_if_not_exists
from db.services.order_actions import create_order_action_if_not_exists


def create_pricelist(db: Session):
    """"""
    create_order_action_if_not_exists(name=OrderAction.NUKE_TECH.value, price=500, db=db)
    create_order_action_if_not_exists(name=OrderAction.BUILD_BOMB.value, price=150, db=db)
    create_order_action_if_not_exists(name=OrderAction.DEV_CITY.value, price=150, db=db)
    create_order_action_if_not_exists(name=OrderAction.SEND_MONEY.value, price=0, db=db)
    create_order_action_if_not_exists(name=OrderAction.BUILD_SHIELD.value, price=300, db=db)
    create_order_action_if_not_exists(name=OrderAction.DEV_ECO.value, price=200, db=db)
    create_order_action_if_not_exists(name=OrderAction.BOMB.value, price=0, db=db)


def create_countries(db: Session):
    """"""
    create_country_if_not_exists(name='Северная Корея', init_budget=1000, db=db)
    create_country_if_not_exists(name='Китай', init_budget=1000, db=db)
    create_country_if_not_exists(name='Россия', init_budget=1000, db=db)
    create_country_if_not_exists(name='США', init_budget=1000, db=db)
    create_country_if_not_exists(name='Израиль', init_budget=1000, db=db)
    create_country_if_not_exists(name='Германия', init_budget=1000, db=db)
    create_country_if_not_exists(name='Франция', init_budget=1000, db=db)
    create_country_if_not_exists(name='Куба', init_budget=1000, db=db)


def create_cities(db: Session):
    """"""
    create_city_if_not_exists(
        name='Пхеньян',
        country_name='Северная Корея',
        init_has_shield=False,
        init_development=80,
        init_life_level=72,
        db=db,
    )
    create_city_if_not_exists(
        name='Кэсон',
        country_name='Северная Корея',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Расон',
        country_name='Северная Корея',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Пусан',
        country_name='Северная Корея',
        init_has_shield=False,
        init_development=40,
        init_life_level=36,
        db=db,
    )

    create_city_if_not_exists(
        name='Пекин',
        country_name='Китай',
        init_has_shield=False,
        init_development=80,
        init_life_level=72,
        db=db,
    )
    create_city_if_not_exists(
        name='Шанхай',
        country_name='Китай',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Гуанчжоу',
        country_name='Китай',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Гонконг',
        country_name='Китай',
        init_has_shield=False,
        init_development=40,
        init_life_level=36,
        db=db,
    )

    create_city_if_not_exists(
        name='Москва',
        country_name='Россия',
        init_has_shield=False,
        init_development=80,
        init_life_level=72,
        db=db,
    )
    create_city_if_not_exists(
        name='Санкт-Петербург',
        country_name='Россия',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Новосибирск',
        country_name='Россия',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Екатеринбург',
        country_name='Россия',
        init_has_shield=False,
        init_development=40,
        init_life_level=36,
        db=db,
    )

    create_city_if_not_exists(
        name='Вашингтон',
        country_name='США',
        init_has_shield=False,
        init_development=80,
        init_life_level=72,
        db=db,
    )
    create_city_if_not_exists(
        name='Нью-Йорк',
        country_name='США',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Чикаго',
        country_name='США',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Лос-Анджелес',
        country_name='США',
        init_has_shield=False,
        init_development=40,
        init_life_level=36,
        db=db,
    )

    create_city_if_not_exists(
        name='Иерусалим',
        country_name='Израиль',
        init_has_shield=False,
        init_development=80,
        init_life_level=72,
        db=db,
    )
    create_city_if_not_exists(
        name='Тель-Авив',
        country_name='Израиль',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Хайфа',
        country_name='Израиль',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Эйлат',
        country_name='Израиль',
        init_has_shield=False,
        init_development=40,
        init_life_level=36,
        db=db,
    )

    create_city_if_not_exists(
        name='Берлин',
        country_name='Германия',
        init_has_shield=False,
        init_development=80,
        init_life_level=72,
        db=db,
    )
    create_city_if_not_exists(
        name='Мюнхен',
        country_name='Германия',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Гамбург',
        country_name='Германия',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Франкфурт-на-Майне',
        country_name='Германия',
        init_has_shield=False,
        init_development=40,
        init_life_level=36,
        db=db,
    )

    create_city_if_not_exists(
        name='Париж',
        country_name='Франция',
        init_has_shield=False,
        init_development=80,
        init_life_level=72,
        db=db,
    )
    create_city_if_not_exists(
        name='Марсель',
        country_name='Франция',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Лион',
        country_name='Франция',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Тулуза',
        country_name='Франция',
        init_has_shield=False,
        init_development=40,
        init_life_level=36,
        db=db,
    )

    create_city_if_not_exists(
        name='Гавана',
        country_name='Куба',
        init_has_shield=False,
        init_development=80,
        init_life_level=72,
        db=db,
    )
    create_city_if_not_exists(
        name='Сантьяго-де-Куба',
        country_name='Куба',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Камагуэй',
        country_name='Куба',
        init_has_shield=False,
        init_development=60,
        init_life_level=54,
        db=db,
    )
    create_city_if_not_exists(
        name='Ольгин',
        country_name='Куба',
        init_has_shield=False,
        init_development=40,
        init_life_level=36,
        db=db,
    )


def generate_start_data(db: Session):
    """"""
    create_pricelist(db)
    create_countries(db)
    create_cities(db)
