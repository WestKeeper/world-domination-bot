from common.order_lib.constants import MAX_CITY_DEVELOPMENT_VALUE


def calculate_city_development(
    init_development: int,
    development_number: int,
    max_development_value: int = MAX_CITY_DEVELOPMENT_VALUE,
) -> int:
    """"""
    calculated_city_development = init_development + development_number * (
        0.05 / (init_development * 0.01))
    result_city_development = calculated_city_development \
        if calculated_city_development < max_development_value else max_development_value

    return result_city_development
