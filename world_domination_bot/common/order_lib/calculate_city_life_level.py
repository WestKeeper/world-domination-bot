from common.order_lib.constants import MAX_CITY_LIFE_LEVEL


def calculate_city_life_level(
    ecology_level: int,
    development: int,
    max_life_level_value: int = MAX_CITY_LIFE_LEVEL,
) -> int:
    """"""
    calculated_life_level = ecology_level * development * 0.01
    result_life_level = calculated_life_level \
        if calculated_life_level < max_life_level_value else max_life_level_value

    return result_life_level
