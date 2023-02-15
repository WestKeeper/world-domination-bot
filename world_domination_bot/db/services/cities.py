from typing import List
from sqlalchemy.orm import Session

from common.order_lib.calculate_city_development import calculate_city_development
from common.order_lib.calculate_city_life_level import calculate_city_life_level
from db.models.countries import Country
from db.models.cities import City
from db.models.game_sessions import GameSession
from db.models.leaders import Leader
from schemas.cities import CityShow


def create_city(
    name: str,
    country_name: str,
    has_shield: bool,
    init_development: int,
    development: int,
    development_number: int,
    life_level: int,
    is_alive: bool,
    db: Session,
):
    """"""
    country = City(
        name=name,
        country_name=country_name,
        has_shield=has_shield,
        init_development=init_development,
        development=development,
        development_number=development_number,
        life_level=life_level,
        is_alive=is_alive,
    )
    db.add(country)
    db.commit()


def get_cities_by_user_id(
    user_id: str,
    db: Session,
) -> List[CityShow]:
    """"""
    country = db.query(Country).join(Leader).filter(Leader.user_id == user_id).one()
    city_shows = get_cities_by_country_name(country.name, db)

    return city_shows


def get_cities_by_country_name(
    country_name: str,
    db: Session,
) -> List[CityShow]:
    """"""
    cities = db.query(City).filter(City.country_name == country_name)

    city_shows = []
    for city in cities:
        city_show = CityShow(
            name=city.name,
            has_shield=city.has_shield,
            development=round(city.development, 2),
            life_level=round(city.life_level, 2),
            is_alive=city.is_alive,
        )
        city_shows.append(city_show)

    return city_shows


def get_city_by_name(city_name: str, db: Session) -> CityShow:
    """"""
    city = db.query(City).filter(City.name == city_name).one()

    city_show = CityShow(
        name=city.name,
        has_shield=city.has_shield,
        development=round(city.development, 2),
        life_level=round(city.life_level, 2),
        is_alive=city.is_alive,
    )

    return city_show


def develop_cities_by_city_names(
    city_names: set,
    db: Session,
):
    """"""
    for city_name in city_names:
        city, session = db.query(City, GameSession) \
            .join(Country) \
            .join(Leader) \
            .join(GameSession) \
            .filter(City.name == city_name) \
            .one()
        ecology_level = session.ecology_level
        city.development_number += 1
        city.development = calculate_city_development(
            city.init_development,
            city.development_number,
        )
        city.life_level = calculate_city_life_level(ecology_level, city.development)
        db.commit()


def build_shield_on_cities(
    city_names: List[str],
    db: Session,
):
    """"""
    for city_name in city_names:
        city = db.query(City).filter(City.name == city_name).one()

        if city.has_shield == True:
            raise ValueError(f'City {city_name} has already a shield.')

        city.has_shield = True
        db.commit()


def bomb_cities_from_user_id(
    user_id: int,
    city_names: List[str],
    db: Session,
):
    """"""
    session = db.query(GameSession).join(Leader).filter(Leader.user_id == user_id).one()
    for city_name in city_names:
        city = db.query(City).filter(City.name == city_name).one()
        if city.is_alive == False:
            raise ValueError(f'City {city_name} is already bombed.')
        if city.has_shield:
            city.has_shield = False
        else:
            city.development = 0
            city.life_level = 0
            city.is_alive = False
        session.drop_bombs_num += 1
        db.commit()
