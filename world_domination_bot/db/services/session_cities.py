from typing import List

from sqlalchemy.orm import Session

from common.order_lib.calculate_city_development import calculate_city_development
from common.order_lib.calculate_city_life_level import calculate_city_life_level
from db.base import City
from db.base import Country
from db.base import GameSession
from db.base import Leader
from db.base import SessionCountry
from db.base import SessionCity
from schemas.cities import CityFullShow
from schemas.cities import CityShow


def create_session_city(
    has_shield: bool,
    development: int,
    development_number: int,
    life_level: int,
    is_alive: bool,
    city_name: str,
    session_country_id: int,
    db: Session,
):
    """"""
    session_country = SessionCity(
        has_shield=has_shield,
        development=development,
        development_number=development_number,
        life_level=life_level,
        is_alive=is_alive,
        city_name=city_name,
        session_country_id=session_country_id,
    )
    db.add(session_country)
    db.commit()


def get_cities_by_user_id(
    user_id: str,
    db: Session,
) -> List[CityShow]:
    """"""
    country = db.query(SessionCountry).join(Leader).filter(Leader.user_id == user_id).one()
    city_shows = get_cities_by_country_name(country.name, db)

    return city_shows


def get_cities_by_country_name_n_leader_id(
    country_name: str,
    leader_id: int,
    db: Session,
) -> List[CityShow]:
    """"""
    session_cities = db.query(SessionCity) \
        .join(SessionCountry) \
        .join(Leader) \
        .filter(SessionCountry.country_name == country_name, Leader.id == leader_id) \
        .all()

    session_cities_ids = [session_city.id for session_city in session_cities]

    session_cities_n_cities = db.query(SessionCity, City) \
        .join(City) \
        .where(SessionCity.id.in_(session_cities_ids)) \
        .all()

    city_shows = []
    for session_city, city in session_cities_n_cities:
        city_show = CityFullShow(
            id=session_city.id,
            has_shield=session_city.has_shield,
            development=round(session_city.development, 2),
            development_number=session_city.development_number,
            life_level=round(session_city.life_level, 2),
            is_alive=session_city.is_alive,
            city_name=city.name,
            session_country_id=session_city.session_country_id,
        )
        city_shows.append(city_show)

    return city_shows


def get_cities_by_country_name(
    country_name: str,
    db: Session,
) -> List[CityShow]:
    """"""
    session_cities = db.query(SessionCity) \
        .join(SessionCountry) \
        .join(Country) \
        .filter(Country.name == country_name) \
        .all()

    session_cities_ids = [session_city.id for session_city in session_cities]

    session_cities_n_cities = db.query(SessionCity, City) \
        .join(City) \
        .where(SessionCity.id.in_(session_cities_ids)) \
        .all()

    city_shows = []
    for session_city, city in session_cities_n_cities:
        city_show = CityFullShow(
            id=session_city.id,
            has_shield=session_city.has_shield,
            development=round(session_city.development, 2),
            development_number=session_city.development_number,
            life_level=round(session_city.life_level, 2),
            is_alive=session_city.is_alive,
            city_name=city.name,
            session_country_id=session_city.session_country_id,
        )
        city_shows.append(city_show)

    return city_shows


def get_cities_by_session_country_id(
    session_country_id: id,
    db: Session,
) -> List[CityShow]:
    """"""
    session_cities = db.query(SessionCity) \
        .filter(SessionCity.session_country_id == session_country_id) \
        .all()

    city_shows = []
    for session_city in session_cities:
        city_show = CityShow(
            id=session_city.id,
            has_shield=session_city.has_shield,
            development=round(session_city.development, 2),
            development_number=session_city.development_number,
            life_level=round(session_city.life_level, 2),
            is_alive=session_city.is_alive,
            city_name=session_city.city_name,
            session_country_id=session_city.session_country_id,
        )
        city_shows.append(city_show)

    return city_shows


def get_city_by_name(city_name: str, db: Session) -> CityShow:
    """"""
    city = db.query(SessionCity).filter(SessionCity.name == city_name).one()

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
        city, session = db.query(SessionCity, GameSession) \
            .join(SessionCountry) \
            .join(Leader) \
            .join(GameSession) \
            .filter(SessionCity.name == city_name) \
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
        city = db.query(SessionCity).filter(SessionCity.name == city_name).one()

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
        city = db.query(SessionCity).filter(SessionCity.name == city_name).one()
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
