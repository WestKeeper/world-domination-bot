from typing import List

from sqlalchemy.orm import Session

from db.base import Country
from schemas.countries import CountryBaseShow


def create_country_if_not_exists(
    name: str,
    init_budget: int,
    db: Session,
):
    """"""
    exists = db.query(Country).filter(Country.name == name).first()
    if exists:
        return

    country = Country(
        name=name,
        init_budget=init_budget,
    )
    db.add(country)
    db.commit()


def get_country_by_name(
    name: str,
    db: Session,
) -> CountryBaseShow:
    """"""
    country = db.query(Country).filter(Country.name == name).one()
    country_show = CountryBaseShow(country.name, country.init_budget)

    return country_show


def get_all_countries(
    db: Session,
) -> List[CountryBaseShow]:
    """"""
    countries = db.query(Country).all()
    country_shows = []
    for country in countries:
        country_show = CountryBaseShow(country.name, country.init_budget)
        country_shows.append(country_show)

    return country_shows
