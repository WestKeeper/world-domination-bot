from dataclasses import dataclass
from typing import List

from schemas.cities import CityShow


@dataclass
class CountryShow:
    """"""
    name: str
    cities: List[CityShow]


@dataclass
class CountryUserShow:
    """"""
    name: str
    user_id: int
    cities: List[CityShow]


@dataclass
class CountryPriceShow:
    """"""
    name: str
    user_id: int
    budget: int
