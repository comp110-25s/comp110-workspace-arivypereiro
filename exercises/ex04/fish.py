"""File to define Fish class."""


class Fish:
    """Creating a class for Fish."""

    age: int

    def __init__(self):
        """Initializing Fish class."""
        self.age = 0
        return None

    def one_day(self):
        """Simulating one day in Fish class."""
        self.age += 1
        return None
