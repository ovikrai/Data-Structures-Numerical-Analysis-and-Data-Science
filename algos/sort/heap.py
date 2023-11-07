from algos.utils import sink, swap


# ------------------------- HEAP SORT ---------------------------- #
# In-Place: Do Not requires auxiliary memory space.
# Stable: Does Not change the relative order of elements with equal keys.
# Online: can sort a list as it receives it.
#
# Runtime T(n):
#   Best: T(n) ~ n
#   Average: T(n) ~ 2 * n * log(n)
#   Worst: T(n) ~ 2 * n * log(n)
#
# Asymptotically Analysis (Big O)
#   Best: T(n) = O(n)
#   Average: T(n) = O(n * log(n))
#   Worst: T(n) = O(n * log(n))
#
# -----------------------------------------------------------------------#
def heap(a: list):
    n = len(a)

    k = n // 2
    for k in range(k, 1, -1):
        sink(a, k)

    while n > 1:
        swap(a, 1, n - 1)
        sink(a, 1)
