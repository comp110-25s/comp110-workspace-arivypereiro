"""File to define River class."""

__author__: str = "730671996"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Creating a class for River."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking for old age in Fish and Bear classes."""
        Surviving_list_fish: list[Fish] = self.fish
        Surviving_list_bears: list[Bear] = self.bears
        for fish in self.fish:
            if fish.age > 3:
                Surviving_list_fish.pop()
            fish = Surviving_list_fish
        for bears in self.bears:
            if bears.age > 5:
                Surviving_list_bears.pop()
            bears = Surviving_list_bears
        return None

    def remove_fish(self, amount: int):
        """Removing a certain amount of fish."""
        while amount > 0:
            self.fish.pop(0)
            amount -= 1
        return None

    def bears_eating(self):
        """Determining amount of fish bear eats based on number of fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Checking for bear hunger."""
        bears_list: list[Bear] = self.bears
        for bears in self.bears:
            if bears.hunger_score < 0:
                bears_list.pop()
            bears = bears_list
        return None

    def repopulate_fish(self):
        """Checking for reproduction in Fish class."""
        num_offspring: int = (len(self.fish) // 2) * 4
        while num_offspring > 0:
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Checking for reproduction in Bear class."""
        bears_list: list[Bear] = self.bears
        for bears in self.bears:
            if len(self.bears) % 2 == 0:
                num_offspring: int = len(self.bears) // 2
                for _ in range(0, num_offspring):
                    bears_list.append(bears)
        return None

    def view_river(self):
        """Viewing river attributes."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulating one week in river."""
        for _ in range(0, 7):
            self.one_river_day()
