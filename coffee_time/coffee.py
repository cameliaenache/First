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
        cantitate_totala_cafea = 3*self.coffee_spoons + 2*self.sugar + 5*self.water
        return cantitate_totala_cafea

    def prepare_time_coffee(self):
        time_to_prepare = math.pi*math.sin(self.coffee_spoons) + math.cos(self.sugar) + self.water
        print(f'The time to prepare your coffee is: {time_to_prepare}')
