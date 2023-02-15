def calculate_ecology_level(
    build_bombs_num: int,
    nuke_tech_num: int,
    dev_eco_num: int,
) -> int:
    """"""
    calculated_eco_level = (0.9 - 0.012 * build_bombs_num - 0.02 * nuke_tech_num \
        + 0.05 * dev_eco_num) * 100
    result_eco_level = calculated_eco_level if calculated_eco_level > 0 else 0

    return result_eco_level
