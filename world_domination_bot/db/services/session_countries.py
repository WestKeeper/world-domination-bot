from typing import Dict, List
from sqlalchemy.orm import Session

from common.order_lib.calculate_ecology_level import calculate_ecology_level
from db.base import Country
from db.base import GameSession
from db.base import Leader
from db.base import SessionCountry
from db.services.session_cities import get_cities_by_country_name_n_leader_id
from db.services.session_cities import get_cities_by_session_country_id
from db.services.session_cities import get_cities_by_country_name
from schemas.countries import CountryCitiesShow
from schemas.countries import CountryNameShow
from schemas.countries import CountryFullShow
from schemas.countries import CountryUserCitiesShow


def create_session_country(
    budget: int,
    has_nuke_tech: bool,
    bombs_number: int,
    country_name: str,
    leader_id: int,
    db: Session,
):
    """"""
    session_country = SessionCountry(
        budget=budget,
        has_nuke_tech=has_nuke_tech,
        bombs_number=bombs_number,
        country_name=country_name,
        leader_id=leader_id,
    )
    db.add(session_country)
    db.commit()


def get_countries(
    db: Session,
) -> List[CountryCitiesShow]:
    """"""
    countries = db.query(SessionCountry).all()
    country_shows = []
    for country in countries:
        cities = get_cities_by_country_name(country_name=country.name, db=db)
        country_show = CountryCitiesShow(name=country.name, cities=cities)
        country_shows.append(country_show)
    return country_shows


def get_countries_with_leaders_by_session_id(
    session_id: int,
    db: Session,
) -> List[CountryUserCitiesShow]:
    """"""
    session_countries_with_countries_with_leaders = db.query(SessionCountry, Country, Leader) \
        .join(Country) \
        .join(Leader) \
        .filter(Leader.session_id == session_id) \
        .all()

    country_user_shows = []
    for session_country, country, leader in session_countries_with_countries_with_leaders:
        cities = get_cities_by_country_name_n_leader_id(
            country_name=country.name, leader_id=leader.id, db=db)
        country_user_show = CountryUserCitiesShow(
            name=country.name, user_id=leader.user_id, cities=cities)
        country_user_shows.append(country_user_show)

    return country_user_shows


def get_country_by_user_id_and_session_id(
    user_id: int,
    session_id: int,
    db: Session,
) -> CountryFullShow:
    """"""
    session_country = db.query(SessionCountry) \
        .join(Leader) \
        .filter(Leader.user_id == user_id,
                Leader.session_id == session_id) \
        .one()
    cities = get_cities_by_session_country_id(session_country_id=session_country.id, db=db)
    country_show = CountryFullShow(
        id=session_country.id,
        budget=session_country.budget,
        has_nuke_tech=session_country.has_nuke_tech,
        bombs_number=session_country.bombs_number,
        name=session_country.country_name,
        leader_id=session_country.leader_id,
        cities=cities,
    )

    return country_show


def get_session_country_by_leader_id(
    leader_id: int,
    db: Session,
) -> CountryFullShow:
    """"""
    session_country = db.query(SessionCountry).filter(SessionCountry.leader_id == leader_id).one()
    cities = get_cities_by_session_country_id(session_country_id=session_country.id, db=db)
    country_show = CountryFullShow(
        id=session_country.id,
        budget=session_country.budget,
        has_nuke_tech=session_country.has_nuke_tech,
        bombs_number=session_country.bombs_number,
        name=session_country.country_name,
        leader_id=session_country.leader_id,
        cities=cities,
    )

    return country_show


def get_not_user_countries(
    user_id: str,
    db: Session,
) -> List[CountryNameShow]:
    """"""
    countries = db.query(SessionCountry).join(Leader).filter(Leader.user_id != user_id).all()
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
    country = db.query(SessionCountry).join(Leader).filter(Leader.user_id == user_id).one()
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

    country = db.query(SessionCountry).join(Leader).filter(Leader.user_id == user_id).one()
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

    country = db.query(SessionCountry).join(Leader).filter(Leader.user_id == user_id).one()
    country.bombs_number += bomb_num

    db.commit()


def send_money_to_country_from_user_id(
    user_id: int,
    receivers_info: Dict[str, int],
    db: Session,
):
    """"""
    for receiver_name, money_amount in receivers_info.items():
        country_receiver = db.query(SessionCountry).filter(SessionCountry.name == receiver_name).one()
        if country_receiver.budget < money_amount:
            raise ValueError(f'Receiver country {country_receiver.name} budget is less '
                             f'than sent money amount {money_amount}.')
        country_receiver.budget += money_amount
        db.commit()

