"""Exercise for planning a tea party"""

__author__: str = "730671996"


def tea_bags(people: int) -> int:
    """The number of tea bags needed for the tea party"""
    return 2 * people


def treats(people: int) -> int:
    """The number of treats needed for the tea party"""
    return int(1.5 * tea_bags(people=people))

def cost(tea_count:int, treat_count:int) -> float:
    """Cost for the tea party"""
    return tea_bags(tea_count:people) * 0.5 +treats(treat_count:people)













