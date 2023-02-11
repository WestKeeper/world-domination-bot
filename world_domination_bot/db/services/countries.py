from typing import List
from sqlalchemy.orm import Session

from db.models.countries import Country
from db.services.cities import get_country_cities
from schemas.countries import CountryShow


def create_country(
    name: str,
    budget: int,
    drop_after_db_cleaned: bool,
    db: Session,
):
    """"""
    country = Country(
        name=name,
        budget=budget,
        drop_after_db_cleaned=drop_after_db_cleaned,
    )
    db.add(country)
    db.commit()


def get_countries(
    db: Session,
) -> List[CountryShow]:
    """"""
    countries = db.query(Country).all()
    country_shows = []
    for country in countries:
        cities = get_country_cities(country_name=country.name, db=db)
        country_show = CountryShow(name=country.name, cities=cities)
        country_shows.append(country_show)
    return country_shows
