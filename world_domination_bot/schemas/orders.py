from dataclasses import dataclass
from typing import List


@dataclass
class SendMoneyOrder:
    """"""
    receiver: str
    money_num: int


@dataclass
class OrderState:
    """"""
    price: int
    nuke_tech: bool
    build_bomb: int
    dev_city: List[str]
    send_money: List[SendMoneyOrder]
    build_shield: List[str]
    dev_eco: bool
    bomb_city: List[str]
