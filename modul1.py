from coffee.fifi import greater_than
from dada.lala import concatenate_list

# import coffee
# from coffee import tea as t

def modul():
    gt = greater_than(4, 6)

    print('modul1 {}'.format(gt))

    l1 = []
    l2 = [6, 7]

    print('modul1 {}'.format(concatenate_list(l1, l2)))

if __name__ == '__main__':
    modul()
