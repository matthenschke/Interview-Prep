# QUICK SORT WITH LAST ELEMENT AS PARTITION


def quick_sort(arr, l, r):
    if l <= r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot - 1)
        quick_sort(arr, pivot + 1, r)


def partition(arr, l, r):
    pivot = r
    i, j = l, l

    while j < pivot:
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


if __name__ == "__main__":
    arr = [10, 80, 30, 90, 40, 50, 70]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
