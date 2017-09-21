# f = open('text.txt', 'r+')
# f.write('astazi este duminica\n')
# f.write('ieri a fost sambata')
# f.seek(0)
# lista = f.read()
# print(lista)


# with open('text2.txt', 'r+') as f1:
#     f1.write('14545121\nfjdhfj\nahfjjmn')
#     f1.seek(0)
#     content = f1.read()
#     print(content)
#     f1.seek(0)
#     content2 = f1.readlines()
#     print(content2)
    # f1.write('\n')
    # f1.writelines(content2)

txt = ['ada', 'asdhsa', 'akdj']

# to append at the end of the file
with open('text.txt', 'a') as f:
    f.writelines(txt)