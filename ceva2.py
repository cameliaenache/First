# print('Type list:')
# var = input()
# cuv = var.split(',')
#
# cuv.sort()
# string = ','.join(cuv)
#
# print(string)


# print('Type list:')
# var = input()
#
# cuv = var.split(',')
# cuv.sort()
# string = ','.join(cuv)
# print(string.lower())


# print('Type list:')
#
# var = input()
# cuv = var.split(',')
# print(cuv)
# cuv.sort()
# string = ','.join(cuv)
#
# print(string.lower())
# cuv.reverse()
# string = ','.join(cuv)
#
# print(string.upper())

# Problem 1
result = ''

for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            result += ',' + str(i)

result = result.replace(',', '', 1)

print(result)

# Problem 1b

result1 = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result1.append(i)

print(result1)
