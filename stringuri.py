a = 7
b = 'jdshfsjdhnf'

m = 'sdghs {} valoare {}'.format(1, 4)
m1 = 'sdghs {0} valoare {1}'.format(a, b)
m2 = 'sdghs {y} valoare {x}'.format(x=1, y=4)
m3 = f'sdghs {a} valoare {b}'
m4 = 'dagsah %d valoare %s' % (a, b)

print(m)
print(m1)
print(m2)
print(m3)
print(m4)


t = (1, 5, '22')  # tuple

p, r, s = t  # p=1, r=5, ...
print(s)