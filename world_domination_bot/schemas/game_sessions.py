from dataclasses import dataclass


@dataclass
class GameSessionShow:
    """"""
    id: int
    host_user_id: int
    ecology_level: int
    is_active: bool
