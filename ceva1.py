l = []

# print(type(l))
#
# print(len(l))
l.append('abc')
l.append([1, 2])
l.append(6)
l.append(5)

l.extend([1,4,5,6])

p = l.pop()  # sterge ultimul element din lista

# print(l)
# print('marime', len(l))
#
# print('element 2:', l[1])
# print('de la el 4 pana la sf:', l[3:])
# print(l[-1])
# print(l[-2:])
# print(l[2:4])
#
# cuvant = 'gigi, are, prune'
#
# print(cuvant[-5:])
# print(cuvant.split(','))
#
# print(l.index(5))

# for item in l:
#     tipul = type(item)
#     print(f'{tipul.__name__}')

# if 'a' in l:
#     print('a')
# elif 5 in l:
#     print('b')
# else:
#     print('go home')
#
# new = []
# for item in l:
#     if type(item) == int:
#         new.append(item)
# print(new)
#
# new.reverse()
# print(new)
#
# while 6 in new:
#     print('yes')
#     break
#
# b = new[::-1]
# print(b)
#
# while 1 in l:
#     a = l.pop(2)
#     print(a)


new_list = []
for i in l:
    if type(i) == int:
        new_list.append(i)

int_list = [i for i in l if type(i) == int]
print(int_list)