from coffee.fifi import greater_than

if __name__ == '__main__':
    n = int(input('Introduceti un numar:'))
    m = greater_than(7, 0)

    if n > m:
        print("You win")
    else:
        print("You lose")
