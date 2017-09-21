class Fruit:
    """
    This is a fruit class.
    """
    variable = 5
    # self  - referinta catre obiectul curent

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print(f'This fruit is {self.color} and is named {self.name}')
        self._gigi()
        
    def _gigi(self):
        print('is private')

    @staticmethod
    def apd(a, b):
        return a + b

if __name__ == '__main__':
    plum = Fruit('plum', 'purple')
    apple = Fruit('iapple', 'red')

    plum._gigi()
    plum.show()
    apple.show()
    plum.apb(2, 4)
    print(Fruit.apb(2, 9))

    print(plum.__dict__)
    print(plum.__doc__)



