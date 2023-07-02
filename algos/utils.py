# ------------------------- UTILITY CONSTANTS ---------------------------- #
# Null Types for native data types
from typing import Any, List, Tuple

# Types Aliases

# Types Nulls
IntNull = 0
FloatNull = 0.00
StringNull = ''

ListNull = []
TupleNull = ()
SetNull: set = {None}
DictNull: dict = {None: None}
MatrixNull = []

# TODO: MAKE A DATA CLASS instead of a type...
Matrix = List[List[float]]
Curve = List[Tuple[float]]


# ------------------------- UTILITY FUNCTIONS ---------------------------- #
# ------------------------- Derivative of a function -------------- #
# Compute the difference formula for f'(a) with step size h.
# f : Vectorized function of one variable
# a : Compute derivative at x = a
# method : Difference formula: 'forward', 'backward' or 'central'
# h : Step size in difference formula
# TODO: TEST THIS IMPLEMENTATION
def delta(f, a: float, method='central', h=0.000001) -> float:
    if method == 'central':
        return (f(a + h) - f(a - h)) / (2 * h)
    elif method == 'forward':
        return (f(a + h) - f(a)) / h
    elif method == 'backward':
        return (f(a) - f(a - h)) / h


# ------------------------- BOOLEAN CHECKS ---------------------------- #
# Check if the list is sorted
def is_sorted(a: list, low: int, high: int) -> bool:
    print("########## START CHECK: List from", low, "to", high, "if is sorted")
    # Traverse all the list
    for i in range(low + 1, high):
        # Compare each one of the element
        if a[i] < a[i - 1]:
            print("########## END CHECK: List is NOT sorted")
            return False
    print("########## END CHECK: List is sorted")
    return True


# ------------------------- OPERATIONS ---------------------------- #
# Print list to standard output
def show(a: list) -> None:
    print("########## START: Show List")
    print(a)
    print("########## END: Show List")


# Exchange two elements of a list
def swap(a: list, i: int, j: int) -> None:
    print("########## START: Swap Elements", a[i], "<", a[j])
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    print("########## END: Swapped Elements", a[i], ">", a[j])


# LOW LEVEL API MIMICKING ALLOCATION BEHAVIOR
def allocate(null_type: Any, size: int) -> list:
    print("########## START: Allocate a Null-Typed List")
    if size < 0:
        raise Exception("########## ERROR: length is not a positive integer")
    else:
        print("########## | ALLOC: NULL-TYPE LIST")
        print("########## END: Allocate a Null-Typed List \n")
        return [null_type] * size


def deallocate(obj: object):
    print("########## START: Deallocate an Object")
    if obj is None:
        print("########## | DEALLOC: EMPTY OBJECT")
        print("########## END: Allocate a Null-Typed List \n")
        del obj
    else:
        print("########## | DEALLOC: NON-EMPTY OBJECT")
        print("########## END: Deallocate an Object \n")
        del obj
