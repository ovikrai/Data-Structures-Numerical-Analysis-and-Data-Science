import math


# ------------------------- Binary Search ---------------------------- #
# List need to be ordered to this search to work
#
# Runtime T(n):
#   Best: T(n) ~ c
#   Average: T(n) ~ 1/2 * log(n)
#   Worst: T(n) ~ log(n)
#
# Asymptotically Analysis (Big O):
#   Best: T(n) = O(1)
#   Average: T(n) = O(log(n))
#   Worst: T(n) = O(log(n))
#
# ----------------------------------------------------------------------- #
# Iterative binary search over a list
def binary(a: list, key, left: int, right: int) -> int:
    while left <= right:
        mid = math.floor((left + right) / 2)
        if a[mid] < key:
            left = mid + 1
        elif a[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1


# Alternative binary search over ordered list
# Created by Hermann Bottenbruch, 1962
def binary_ordered(a: list, key, left: int, right: int) -> int:
    while left != right:
        mid = math.ceil((left + right) / 2)
        if a[mid] > key:
            right = mid - 1
        else:
            left = mid
    if a[left] == key:
        return left
    return -1


# Leftmost binary search over linear structures
def binary_left(a: list, key, left: int, right: int) -> int:
    while left < right:
        mid = math.floor((left + right) / 2)
        if a[mid] < key:
            left = mid + 1
        else:
            right = mid
    if a[left] == key:
        return left
    return -1


# Rightmost binary search over linear structures
def binary_right(a: list, key, left: int, right: int) -> int:
    while left < right:
        mid = math.floor((left + right) / 2)
        if a[mid] > key:
            right = mid
        else:
            left = mid + 1
    if a[right - 1] == key:
        return right - 1
    return -1


# Recursive binary search over linear structures
def binary_recursive(a: list, key, left: int, right: int) -> int:
    if left <= right:
        mid = math.floor(left + (right - left) / 2)
        if a[mid] == key:
            return mid
        if a[mid] > key:
            return binary_recursive(a, key, left, mid - 1)
        return binary_recursive(a, key, mid + 1, right)
    return -1
