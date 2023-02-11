from dataclasses import dataclass
from typing import List

from schemas.cities import CityShow


@dataclass
class CountryShow:
    """"""
    name: str
    cities: List[CityShow]
