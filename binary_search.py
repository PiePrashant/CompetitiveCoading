def binary_search(a, k,i):
    n = len(a)
    if a[int(n/2)] == k: return i + int(n/2)
    elif n == 1: return "OOPS! NOT FOUND"
    elif a[int(n/2)] > k: return binary_search(a[0:int(n/2)], k, i)
    else: return binary_search(a[int(n/2):n], k, i + int(n/2))
