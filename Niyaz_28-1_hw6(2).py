def binary_search(val, lst):

    l = 0

    r = len(lst)

    found = False

    while l + 1 < r:

        m = int((l + r) / 2)

        if lst[m] == val:

            l = r = m

            found = True

        elif lst[m] > val:

            r = m

        else:

            l = m + 1

    if found:

        print(f'элемент по индексом: {l}')

    else:

        print('такого элемента нет')
