with open('text.txt', 'w') as fdel:
    pass

with open('text2.txt', 'r+') as f:
    content = f.readlines()

cursor_in = int(input("Pozitia la care adaugam: "))
cursor = cursor_in - 1

while cursor > len(content):
    print('Pozitia maxima la care puteti insera este: {}\n'.format(len(content)+1))
    cursor_in = int(input("Reintroduceti pozitia la care adaugam:"))
    cursor = cursor_in - 1

text_in = input('Introduceti textul:')

if cursor == len(content):
    content.insert(cursor, '\n' + text_in)
else:
    content.insert(cursor, text_in + '\n')

with open('text.txt', 'r+') as f1:
    f1.writelines(content)

