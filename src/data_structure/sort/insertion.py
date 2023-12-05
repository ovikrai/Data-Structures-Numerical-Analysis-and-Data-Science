from src.data_structure.utils import swap


# ------------------------- INSERTION SORT ---------------------------- #
# In-Place: Do Not requires auxiliary memory space.
# Stable: does not change the relative order of elements with equal keys.
# Online: can sort a list as it receives it.
#
# Runtime T(n):
#   Best: T(n) ~ n
#   Average: T(n) ~ 1/4 * (n ^ 2)
#   Worst: T(n) ~ 1/4 * (n ^ 2)
#
# Asymptotically Analysis (Big O)
#   Best: T(n) = O(n)
#   Average: T(n) = O(n ^ 2)
#   Worst: T(n) = O(n ^ 2)
#
# https://en.wikipedia.org/wiki/Insertion_sort
# -----------------------------------------------------------------------#

# Iterative version
def iterative(a: list):
    n = len(a)
    i = 1

    while i < n:
        j = i
        # McCarthy's evaluation or Short-circuit evaluation
        # More info: https://en.wikipedia.org/wiki/Short-circuit_evaluation
        while j > 0 and a[j - 1] > a[j]:
            # Swap elements operation
            swap(a, j, j - 1)
            j = j - 1
        i = i + 1


# A slightly faster version can be produced that moves a[i]
# to its position in one go and only performs one assignment in the inner loop body
def inner_swap(a: list):
    n = len(a)
    i = 1
    while i < n:
        # Using the x variable to do the inner swap each pass
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = x
        i = i + 1


# Recursive version
def recursive(a: list, n: int):
    if n > 0:
        # recursive call
        recursive(a, n - 1)
        # Using the x variable to do the inner swap each pass
        x = a[n]
        j = n - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = x
