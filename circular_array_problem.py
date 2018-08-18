temp = input()
N, K = temp.split()
N = int(N)
key = int(K)
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])


# binary search
def binary_search(a, k, i):
    n = len(a)
    if a[int(n/2)] == k: return i + int(n/2)
    elif n == 1: return "OOPS! NOT FOUND"
    elif a[int(n/2)] > k: return binary_search(a[0:int(n/2)], k, i)
    else: return binary_search(a[int(n/2):n], k, i + int(n/2))


# finding index of pivot element
def pivot_index(a, i):
    n = len(a)
    if a[0] > a[1]: return i
    elif a[0] > a[int(n/2)]: return pivot_index(a[0:int(n / 2)], i)
    else: return pivot_index(a[int(n / 2): n], i + int(n / 2))



index = pivot_index(a, 0)
if key >= a[0]:
    print(binary_search(a[0:index+1], key, 0))
else:
    print(binary_search(a[index+1:len(a)], key, index + 1 ))




