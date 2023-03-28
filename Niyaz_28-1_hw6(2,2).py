def bubble_sort(lst):

    for k in range(1, len(lst)):

        for i in range(1, len(lst) - k + 1):

            if lst[i] < lst[i - 1]:

                lst[i - 1], lst[i] = lst[i], lst[i - 1]

    return lst