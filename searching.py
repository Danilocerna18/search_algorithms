
def linear_search(arr, target):
    """
    Realiza una búsqueda lineal.
    Retorna el índice si encuentra el elemento, de lo contrario -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def binary_search(arr, target):
    """
    Realiza una búsqueda binaria (requiere lista ordenada).
    Retorna el índice si encuentra el elemento, de lo contrario -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1