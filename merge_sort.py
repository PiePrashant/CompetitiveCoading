def merge(left, right):
    pointer1, pointer2 = 0, 0
    array = []
    while pointer1 < len(left) and pointer2 <  len(right):
        if left[pointer1] < right[pointer2]:
            array.append(left[pointer1])
            pointer1 += 1
        else:
            array.append(right[pointer2])
            pointer2 += 1
    if pointer1 < pointer2:
        for i in range(pointer1,len(left)):
            array.append(left[pointer1])
            pointer1 += 1
    elif pointer1 > pointer2:
        for i in range(pointer2,len(right)):
            array.append(right[pointer2])
            pointer2 += 1
    else:
        if left[pointer1] > right[pointer2]: array.append(left[pointer1])
        else: array.append(right[pointer2])
    return array



def merge_sort(a):
    if len(a) == 0: return "OOPS You enterd an empty array"
    if len(a) == 1: return a
    else:
        half = len(a) // 2
        left = merge_sort(a[0:half])
        right = merge_sort(a[half:])
    return merge(left, right)

