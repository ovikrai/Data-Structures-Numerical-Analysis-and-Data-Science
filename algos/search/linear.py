# ------------------------- Linear Search ---------------------------- #
# Search in a list
#
# Outputs:
#   Search successful: the index of the target key (i)
#   Search unsuccessful: negative one (-1)
#
# In-Place: requires O(1) of auxiliary memory space.
#
# Runtime T(n):
#   Best: T(n) ~ c
#   Average: T(n) ~ 1/2 * n
#   Worst: T(n) ~ n
#
# Asymptotically Analysis (Big O):
#   Best: T(n) = O(1)
#   Average: T(n) = O(n)
#   Worst: T(n) = O(n)
#
# ----------------------------------------------------------------------- #
# Basic implementations that
# Basic linear search in an unordered list
def linear(a: list, key, low: int, high: int) -> int:
    n = high
    i = low

    while True:
        if a[i] == key:
            return i

        i = i + 1

        if i < n:
            continue
        else:
            return -1


# Sentinel variation of linear search in an unordered list
def linear_sentinel(a: list, key, low: int, high: int) -> int:
    n = high
    i = low

    while True:
        if a[i] == key:
            if i < n:
                return i
            else:
                return -1
        i = i + 1


# Sentinel variation of linear search in an ordered list
# List need to be ordered to this search to work
def linear_ordered(a: list, key) -> int:
    i = 0
    while True:
        if a[i] >= key:
            if a[i] == key:
                return i
            else:
                return -1
        i = i + 1
