import math


class Coffee:
    """
    This is a new_coffee class.
    """

    def __init__(self, coffee_spoons, sugar, water):
        self.coffee_spoons = coffee_spoons
        self.sugar = sugar
        self.water = water

    def prepare_coffee(self):
        cantitate_totala_cafea = self.coffee_spoons + self.sugar + self.water
        return cantitate_totala_cafea

    def prepare_time_coffee(self):
        time_to_prepare = math.pi*math.sin(self.coffee_spoons) + math.cos(self.sugar) + self.water
        print(int(time_to_prepare))
