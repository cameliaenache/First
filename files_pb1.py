content_out = []
with open('text.txt', 'r+') as f:
    content = f.readlines()
    for i in content:
        content_out.append(i.capitalize())
# print(content_out)
with open('text2.txt', 'r+') as f1:
    f1.read()
    f1.write('\n')
    f1.writelines(content_out)
    f1.seek(0)
    content = f1.read()
    print(content)
