from dataclasses import dataclass


@dataclass
class CityBaseShow:
    """"""
    name: str
    country_name: str
    init_has_shield: bool
    init_development: int
    init_life_level: int


@dataclass
class CityShow:
    """"""
    id: int
    has_shield: bool
    development: int
    development_number: int
    life_level: int
    is_alive: bool
    city_name: str
    session_country_id: int


@dataclass
class CityFullShow:
    """"""
    id: int
    has_shield: bool
    development: int
    development_number: int
    life_level: int
    is_alive: bool
    city_name: str
    session_country_id: int
