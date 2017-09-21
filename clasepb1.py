# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Hints: Use init method to construct some parameters


class Strings:

    def __init__(self, number):    # constructor
        self.number = number
        self.string_input = ''

    def get_string(self):
        for i in range(self.number):
            if i == self.number - 1:
                self.string_input += input('Introduceti cuvant:') + '.'
            else:
                self.string_input += input('Introduceti cuvant:') + ' '


    def print_string(self):
        print(self.string_input.upper())

if __name__ == '__main__':

    ts = Strings(5)

    ts.get_string()
    ts.print_string()

#Lista de 5 intrebari despre clase/obiecte

# 1. Which are the (two kinds of) operations supported by class objects?
# attribute references and instantiation
# 2.