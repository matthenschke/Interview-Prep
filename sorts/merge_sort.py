
def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    L = [0] * (mid - l + 1)
    R = [0] * (r - mid)

    for i in range(l, mid + 1):
        L[i - l] = arr[i]

    for j in range(mid + 1, r + 1):
        R[j - (mid + 1)] = arr[j]

    i = 0
    j = 0
    k = l

    m = len(L)
    n = len(R)

    while i < m and j < n:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < m:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n:
        arr[k] = R[j]
        j += 1
        k += 1
