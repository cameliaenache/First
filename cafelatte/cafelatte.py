from coffee_time.coffee import Coffee
import math


class Cafelatte(Coffee):
    """
    This is a derived class of Coffee
    """

    def __init__(self, coffee_spoons, sugar, water, milk):
        super().__init__(coffee_spoons=coffee_spoons, sugar=sugar, water=water)
        self.milk = milk

    def prepare_coffee(self):
        cantitate_totala_cafea = 3*self.coffee_spoons + 2*self.sugar + 5*self.water + self.milk
        return cantitate_totala_cafea

    def prepare_time_coffee(self):
        time_to_prepare = math.pi*math.sin(self.coffee_spoons) + math.cos(self.sugar) + self.water + 2 * self.milk
        print(f'The time to prepare your cafelatte is: {time_to_prepare}')

    def energy(self):
        energy_drink = self.milk + self.coffee_spoons ** 2
        return energy_drink