#pragma once

#include "./tools.h"

// ------------------------- INSERTION SORT ---------------------------- #
// In-Place: Do Not requires auxiliary memory space.
// Stable: does not change the relative order of elements with equal keys.
// Online: can sort a list as it receives it.
//
// Runtime T(n):
//   Best: T(n) ~ n
//   Average: T(n) ~ 1/4 * (n ^ 2)
//   Worst: T(n) ~ 1/4 * (n ^ 2)
//
// Asymptotically Analysis (Big O)
//   Best: T(n) = O(n)
//   Average: T(n) = O(n ^ 2)
//   Worst: T(n) = O(n ^ 2)
//
// -----------------------------------------------------------------------#
class Insertion
{
public:
    template <class T>
    static void sort(T &a, unsigned int low, unsigned int high);
};

template <class T>
void Insertion::sort(T &a, unsigned int low, unsigned int high)
{
    for (unsigned int i = low + 1; i < high + 1; i++)
    {
        for (unsigned int j = i; j > low && a[j] < a[j - 1]; j--)
        {
            tools::swap(a, j, j - 1);
        }
    }
}
