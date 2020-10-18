from random import randint


# Insertion Sorting Algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


# Test Driver
random_list = [randint(0, 100) for x in range(15)]
print(f'Random List: {random_list}')

sorted_list = insertion_sort(random_list)
print(f'Sorted List: {sorted_list}')
