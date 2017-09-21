d = {
    'key': 'val',
    'key2': 'val2',
    'a': 2
}

print(d)
d['key3'] = 'val'
# d.keys()
# d.items()

for k, v in d.items():
    print('{} > {}'.format(k, v))

d1 = {
    'a': 100,
    'b': 200,
    'c': 300
}

d2 = {
    'a': 50,
    'b': 35,
    'm': 36,
    'x': 555
}

df = {}

# for k1 in d1.keys():
#     for k2 in d2.keys():
#         df[k1] = d1[k1]
#         df[k2] = d2[k2]
# print(df)

df.update(d1)
print(df)
df.update(d2)
print(df)

for k1 in d1.keys():
    for k2 in d2.keys():
        if k1 == k2:
            df[k1] = d1[k1] + d2[k1]
print(df)


# sau

df = d2

for k in d2:
    if k in d1:
        df[k] = d1[k] + d2[k]
    else:
        df[k] = d2[k]

print(df)
