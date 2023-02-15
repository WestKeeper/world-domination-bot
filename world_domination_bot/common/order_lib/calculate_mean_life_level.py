from typing import List


from schemas.cities import CityShow


def calculate_mean_life_level(
    cities: List[CityShow],
) -> float:
    """"""
    life_level_sum = 0
    for city in cities:
        life_level_sum += city.life_level

    mean_life_level = life_level_sum / len(cities)

    return mean_life_level
