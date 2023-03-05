from typing import List
from sqlalchemy.orm import Session

from db.base import City
from schemas.cities import CityBaseShow


def create_city_if_not_exists(
    name: str,
    country_name: str,
    init_has_shield: bool,
    init_development: int,
    init_life_level: int,
    db: Session,
):
    """"""
    exists = db.query(City).filter(City.name == name).first()
    if exists:
        return

    city = City(
        name=name,
        country_name=country_name,
        init_has_shield=init_has_shield,
        init_development=init_development,
        init_life_level=init_life_level,
    )
    db.add(city)
    db.commit()


def get_city_by_name(
    name: str,
    db: Session,
) -> CityBaseShow:
    """"""
    city = db.query(City).filter(City.name == name).one()
    city_show = CityBaseShow(
        name=city.name,
        country_name=city.country_name,
        init_has_shield=city.init_has_shield,
        init_development=city.init_development,
        init_life_level=city.init_life_level,
    )

    return city_show


def get_country_cities(
    country_name: str,
    db: Session,
) -> List[CityBaseShow]:
    """"""
    cities = db.query(City).filter(City.country_name == country_name).all()
    city_shows = []
    for city in cities:
        city_show = CityBaseShow(
            name=city.name,
            country_name=city.country_name,
            init_has_shield=city.init_has_shield,
            init_development=city.init_development,
            init_life_level=city.init_life_level,
        )
        city_shows.append(city_show)

    return city_shows

