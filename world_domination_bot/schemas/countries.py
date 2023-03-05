from dataclasses import dataclass
from typing import List

from schemas.cities import CityShow


@dataclass
class CountryNameShow:
    """"""
    name: str

@dataclass
class CountryBaseShow:
    """"""
    name: str
    init_budget: int


@dataclass
class CountryCitiesShow:
    """"""
    name: str
    cities: List[CityShow]


@dataclass
class CountryUserCitiesShow:
    """"""
    name: str
    user_id: int
    cities: List[CityShow]


@dataclass
class CountryFullShow:
    """"""
    id: int
    budget: int
    has_nuke_tech: bool
    bombs_number: int
    name: str
    leader_id: int
    cities: List[CityShow]
