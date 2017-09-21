# Problem2
print('Write something:')
keyboard_input = input()

no_letters = 0
no_digits = 0

for i in keyboard_input:
    if i.isdigit():
        no_digits += 1
    elif i.isalpha():
        no_letters += 1

print(no_digits)
print(no_letters)