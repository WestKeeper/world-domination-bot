from typing import List
from sqlalchemy.orm import Session

from db.models.countries import Country
from db.models.leaders import Leader
from db.services.cities import get_cities_by_country_name
from schemas.countries import CountryShow
from schemas.countries import CountryPriceShow
from schemas.countries import CountryUserShow


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
        cities = get_cities_by_country_name(country_name=country.name, db=db)
        country_show = CountryShow(name=country.name, cities=cities)
        country_shows.append(country_show)
    return country_shows


def get_countries_with_leaders(
    db: Session,
) -> List[CountryUserShow]:
    """"""
    get_countries_with_leaders = db.query(Country, Leader).join(Leader).all()

    country_user_shows = []
    for country, leader in get_countries_with_leaders:
        cities = get_cities_by_country_name(country_name=country.name, db=db)
        country_user_show = CountryUserShow(
            name=country.name, user_id=leader.user_id, cities=cities)
        country_user_shows.append(country_user_show)

    return country_user_shows


def get_country_by_user_id(
    user_id: str,
    db: Session,
) -> CountryPriceShow:
    """"""
    country = db.query(Country).join(Leader).filter(Leader.user_id == user_id).one()
    country_show = CountryPriceShow(name=country.name, user_id=user_id, budget=country.budget)

    return country_show
