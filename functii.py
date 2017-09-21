def nume(param):
    pass

def suma(a, b=2):
    s = a + b
    return s

s = suma(a=7)
s = suma(3, 5)

print(s)

# 1 func: citim de la tastatura si returnam int
# de la tastaura
# 2 func:
# 2 nr, le comparam
# daca n1 > n2 return true, daca nu
# cu output,
# func 3:
# daca este true atunci cerem de la tastaura altul
# func 4
# daca este false sa il inlocuiasca cu primul nr impar mai mic decat el


def numar():
    n = input('Introduceti numar:')
    return int(n)


def comparare(n1, n2):
    if n1 >= n2:
        return True
    else:
        return False

def impar(n):
    if n % 2 == 0:
        return n-1
    else:
        return n-2

n1 = numar()
n2 = numar()

if comparare(n1, n2):
    n1 = numar()
else:
    n1 = impar(n1)

print('Noile numere sunt: {} {}'.format(n1, n2))

#like
