"""Exercise for planning tea party"""

__author__: str = "730671996"


def main_planner(guests: int) -> None:
    """Number of people that will attend the tea party"""
    print("A Cozy Tea Party for" + " " + str(guests) + " " + "people!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=guests, treat_count=guests) * 2.6))


def tea_bags(people: int) -> int:
    """The number of tea bags needed for the tea party"""
    return 2 * people


def treats(people: int) -> int:
    """The number of treats needed for the tea party"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """The cost of the tea party"""
    return (
        tea_bags(people=tea_count) * 0.5 * 0.5
        + treats(people=treat_count) * (1 / 3) * 0.75
    )


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
