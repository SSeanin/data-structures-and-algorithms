def minimax_linear(arr: list) -> tuple:
    minimum = arr[0]
    maximum = arr[0]

    for item in arr:
        if item < minimum:
            minimum = item
        elif item > maximum:
            maximum = item

    return minimum, maximum


def minimax_recursive(arr: list) -> tuple:
    if len(arr) <= 2:
        try:
            return arr.pop(0) if arr[0] < arr[1] else arr.pop(), arr[0]
        except IndexError:
            return arr[0], arr[0]

    left_min, left_max = minimax_recursive(arr[:len(arr) // 2])
    right_min, right_max = minimax_recursive(arr[len(arr) // 2:])

    return left_min if left_min < right_min else right_min, left_max if left_max > right_max else right_max
