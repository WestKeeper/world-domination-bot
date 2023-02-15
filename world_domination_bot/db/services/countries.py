from typing import Dict, List
from sqlalchemy.orm import Session

from common.order_lib.calculate_ecology_level import calculate_ecology_level
from db.models.countries import Country
from db.models.game_sessions import GameSession
from db.models.leaders import Leader
from db.services.cities import get_cities_by_country_name
from schemas.countries import CountryShow
from schemas.countries import CountryNameShow
from schemas.countries import CountryPriceShow
from schemas.countries import CountryUserShow


def create_country(
    name: str,
    budget: int,
    has_nuke_tech: bool,
    bombs_number: int,
    drop_after_db_cleaned: bool,
    db: Session,
):
    """"""
    country = Country(
        name=name,
        budget=budget,
        has_nuke_tech=has_nuke_tech,
        bombs_number=bombs_number,
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
    cities = get_cities_by_country_name(country_name=country.name, db=db)
    country_show = CountryPriceShow(
        name=country.name, user_id=user_id, budget=country.budget,
        nuke_tech=country.has_nuke_tech, bombs_number=country.bombs_number, cities=cities)

    return country_show


def get_not_user_countries(
    user_id: str,
    db: Session,
) -> List[CountryNameShow]:
    """"""
    countries = db.query(Country).join(Leader).filter(Leader.user_id != user_id).all()
    country_shows = []
    for country in countries:
        country_show = CountryNameShow(name=country.name)
        country_shows.append(country_show)

    return country_shows


def decrease_country_budget_by_user_id(
    user_id: int,
    decreasing_amount: int,
    db: Session,
):
    """"""
    country = db.query(Country).join(Leader).filter(Leader.user_id == user_id).one()
    if country.budget < decreasing_amount:
        raise ValueError(f'Country budget {country.budget} is less '
                         f'than decreasing amount {decreasing_amount}')
    country.budget -= decreasing_amount

    db.commit()


def give_country_nuke_tech_by_user_id(
    user_id: int,
    is_nuke_developed: bool,
    db: Session,
):
    """"""
    if not is_nuke_developed:
        return

    session = db.query(GameSession).join(Leader).filter(Leader.user_id == user_id).one()
    session.nuke_tech_num += 1
    session.ecology_level = calculate_ecology_level(
        session.build_bombs_num,
        session.nuke_tech_num,
        session.dev_eco_num,
    )

    country = db.query(Country).join(Leader).filter(Leader.user_id == user_id).one()
    if country.has_nuke_tech == True:
        raise ValueError(f'Nuke of a country {country.name} is already developed.')
    country.has_nuke_tech = is_nuke_developed

    db.commit()


def give_country_bomb_by_user_id(
    user_id: int,
    bomb_num: int,
    db: Session,
):
    """"""
    if bomb_num == 0:
        return

    session = db.query(GameSession).join(Leader).filter(Leader.user_id == user_id).one()
    session.build_bombs_num += 1
    session.ecology_level = calculate_ecology_level(
        session.build_bombs_num,
        session.nuke_tech_num,
        session.dev_eco_num,
    )

    country = db.query(Country).join(Leader).filter(Leader.user_id == user_id).one()
    country.bombs_number += bomb_num

    db.commit()


def send_money_to_country_from_user_id(
    user_id: int,
    receivers_info: Dict[str, int],
    db: Session,
):
    """"""
    for receiver_name, money_amount in receivers_info.items():
        country_receiver = db.query(Country).filter(Country.name == receiver_name).one()
        if country_receiver.budget < money_amount:
            raise ValueError(f'Receiver country {country_receiver.name} budget is less '
                             f'than sent money amount {money_amount}.')
        country_receiver.budget += money_amount
        db.commit()

