# Insertion Sorting Algorithm
def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left: list, right: list) -> list:
    merged = []

    try:
        while left[0] and right[0]:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
    except IndexError:
        return merged + left + right
