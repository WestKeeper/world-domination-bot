from sqlalchemy.orm import Session

from db.services.session_cities import bomb_cities_from_user_id
from db.services.session_cities import build_shield_on_cities
from db.services.session_cities import develop_cities_by_city_names
from db.services.session_countries import decrease_country_budget_by_user_id
from db.services.session_countries import give_country_bomb_by_user_id
from db.services.session_countries import give_country_nuke_tech_by_user_id
from db.services.session_countries import send_money_to_country_from_user_id
from db.services.game_sessions import develop_ecology_by_user_id
from schemas.orders import OrderState


def execute_order(order: OrderState, user_id: int, db: Session):
    """"""
    decrease_country_budget_by_user_id(user_id, decreasing_amount=order.price, db=db)
    give_country_nuke_tech_by_user_id(user_id, is_nuke_developed=order.nuke_tech, db=db)
    give_country_bomb_by_user_id(user_id, bomb_num=order.build_bomb, db=db)
    develop_cities_by_city_names(city_names=order.dev_city, db=db)
    send_money_to_country_from_user_id(user_id, receivers_info=order.send_money, db=db)
    build_shield_on_cities(city_names=order.build_shield, db=db)
    develop_ecology_by_user_id(user_id, is_ecology_developed=order.dev_eco, db=db)
    bomb_cities_from_user_id(user_id, city_names=order.bomb_city, db=db)
