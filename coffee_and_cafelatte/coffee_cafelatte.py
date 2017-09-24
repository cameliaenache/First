from coffee_time.coffee import Coffee
from cafelatte.cafelatte import Cafelatte


if __name__ == '__main__':

    espresso = Coffee(1, 0, 2)
    espresso_latte = Cafelatte(1, 0, 2, 2)

    espresso.prepare_time_coffee()
    print(espresso.prepare_coffee())
    espresso_latte.prepare_time_coffee()
    print(espresso_latte.prepare_coffee())
