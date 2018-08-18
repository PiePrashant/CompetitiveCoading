def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i
        while j > 0:
            if key < a[j-1]:
                a[j] = a[j-1]
                j = j - 1
            else:
                break
        a[j] = key
    return a



