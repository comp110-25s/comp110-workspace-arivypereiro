"""File to define Bear class."""


class Bear:
    """Creating a class for Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulating one day in Bear class."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Determining the hunger score for Bear class from number of fish eaten."""
        self.hunger_score += num_fish
