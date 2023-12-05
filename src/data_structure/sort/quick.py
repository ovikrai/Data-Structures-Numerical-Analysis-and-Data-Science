from src.data_structure.utils import partition


# ------------------------- QUICK SORT ---------------------------- #
# In-Place: requires O(1) of auxiliary memory space.
# Non-Stable: Change the relative order of elements with equal keys.
# Offline: is given the whole list from the beginning
# Notes: divide-and-conquer approach, fastest in practice
#
# Runtime T(n):
#   Best: T(n) ~ n * log(n)
#   Average: T(n) ~ 2 * n * ln(n)
#   Worst: T(n) ~ 1/2 * n^2
#
# Asymptotically Analysis (Big O)
#   Best: T(n) = O(n * log(n))
#   Average: T(n) = O(n * ln(n))
#   Worst: T(n) = O(n^2)
#
# -----------------------------------------------------------------------#
def quick(a: list, low: int, high: int):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(a, low, high)

        # Recursive call on the left of pivot
        quick(a, low, pivot - 1)

        # Recursive call on the right of pivot
        quick(a, pivot + 1, high)
