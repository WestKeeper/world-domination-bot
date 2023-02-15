from sqlalchemy.orm import Session

from db.models.order_actions import OrderAction
from schemas.order_actions import OrderActionShow


def create_order_action(
    name: str,
    price: int,
    db: Session,
):
    """"""
    order_action = OrderAction(
        name=name,
        price=price,
    )
    db.add(order_action)
    db.commit()


def get_order_action_by_action_name(
    name: str,
    db: Session,
) -> OrderActionShow:
    """"""
    order_action = db.query(OrderAction).filter(OrderAction.name == name).one()
    order_action_show = OrderActionShow(order_action.name, order_action.price)

    return order_action_show

