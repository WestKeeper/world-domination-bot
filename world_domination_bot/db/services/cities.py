from typing import List
from sqlalchemy.orm import Session

from db.models.cities import City
from schemas.cities import CityShow


def create_city(
    name: str,
    country_name: str,
    has_shield: bool,
    development: int,
    life_level: int,
    is_alive: bool,
    db: Session,
):
    """"""
    country = City(
        name=name,
        country_name=country_name,
        has_shield=has_shield,
        development=development,
        life_level=life_level,
        is_alive=is_alive,
    )
    db.add(country)
    db.commit()


def get_country_cities(
    country_name: str,
    db: Session,
) -> List[CityShow]:
    """"""
    cities = db.query(City).filter(City.country_name == country_name).all()
    cities_shows = []
    for city in cities:
        city_show = CityShow(
            name=city.name,
            has_shield=city.has_shield,
            development=city.development,
            life_level=city.life_level,
            is_alive=city.is_alive,
        )
        cities_shows.append(city_show)
    return cities_shows
