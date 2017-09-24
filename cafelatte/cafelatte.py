from coffee_time.coffee import Coffee
import math


class Cafelatte(Coffee):
    """
    This is a derived class of Coffee
    """

    def __init__(self, coffee_spoons, sugar, water, milk):
        self.coffee_spoons = coffee_spoons
        self.sugar = sugar
        self.water = water
        self.milk = milk

    def prepare_coffee(self):
        cantitate_totala_cafea = self.coffee_spoons + self.sugar + self.water + self.milk
        return cantitate_totala_cafea

    def prepare_time_coffee(self):
        time_to_prepare = math.pi*math.sin(self.coffee_spoons) + math.cos(self.sugar) + self.water + 2 * self.milk
        print(int(time_to_prepare))

    def energy(self):
        energy = self.milk + self.coffee_spoons ** 2
        return energy
