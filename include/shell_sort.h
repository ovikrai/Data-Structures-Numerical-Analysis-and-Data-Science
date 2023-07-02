#pragma once

#include "./tools.h"
#include <math.h>
// ------------------------- SHELL SORT ---------------------------- #
// In-Place: requires O(1) of auxiliary memory space.
// Non-Stable: does not change the relative order of elements with equal keys.
// Offline: is given the whole list from the beginning
// Notes: Runtime depends on the gap sequence
//
// Runtime T(n):
//   Best: T(n) ~ n * log_3(n)
//   Average: T(n) ~ (depends on gap sequence)
//   Worst: T(n) ~ c * n^3/2
//
// Asymptotically Analysis (Big O)
//   Best: T(n) = O(n * log3(n))
//   Average: T(n) = (depends on gap sequence)
//   Worst: T(n) = O(n^3/2)
//
// -----------------------------------------------------------------------#
//------------- Shell Sort Interface Definition---------------//
// TODO: CHECK FOR FINAL ITERATION AND SWAP
class Shell
{
private:
    static unsigned int gapIterator(unsigned int n, unsigned int m);

public:
    template <class T>
    static void sort(T &a, unsigned int low, unsigned int high, unsigned int gap_size = 3);
};

unsigned int Shell::gapIterator(unsigned int n, unsigned int m)
{
    int gap = 1;
    while (gap < std::floor(n / m))
    {
        gap = m * gap + 1;
    }
    return gap;
}

template <class T>
void Shell::sort(T &a, unsigned int low, unsigned int high, unsigned int gap_size)
{
    unsigned int i = 0;
    unsigned int j = 0;
    // Gap Sequence initialization
    unsigned int h = gapIterator(high + 1, gap_size);

    while (h >= 1)
    {
        // h-sort the array
        for (i = h; i < high + 1; i++)
        {
            for (j = i; j >= h && a[j] < a[j - h]; j = j - h)
            {
                tools::swap(a, j, j - h);
            }
        }
        // Iterator pass
        h = h / gap_size;
    }
}
