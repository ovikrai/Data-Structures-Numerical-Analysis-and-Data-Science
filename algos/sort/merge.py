from algos.utils import merge_sub


# ------------------------- MERGE SORT ---------------------------- #
# Out-of-Place: requires O(n) of auxiliary memory space.
# Stable: Does Not change the relative order of elements with equal keys.
# Online: can sort a list as it receives it.
# Notes: divide-and-conquer approach
#
# Runtime T(n):
#   Best: T(n) ~ 1/2 * n * log(n)
#   Average: T(n) ~ n * log(n)
#   Worst: T(n) ~ n  * log(n)
#
# Asymptotically Analysis (Big O)
#   Best: T(n) = O(n * log(n))
#   Average: T(n) = O(n * log(n))
#   Worst: T(n) = O(n * log(n))
#
# -----------------------------------------------------------------------#
def merge(a: list, left: int, right: int):
    if left < right:
        # Calculate middle element of the array
        # mid = (left + right) // 2
        # Avoids overflow for large left and right values
        mid = left + (right - left) // 2

        # Sort first and second halves
        merge(a, left, mid)
        merge(a, mid + 1, right)
        merge_sub(a, left, mid, right)
