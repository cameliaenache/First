def concatenate_list(a, b):
    """
    concatenates to lists
    """
    a.extend(b)
    return a

if __name__ == '__main__':
    l1 = [4, 3, 2]
    l2 = [4, 6, 7]

    nl = concatenate_list(l1, l2)

    print('lala = {}'.format(nl))