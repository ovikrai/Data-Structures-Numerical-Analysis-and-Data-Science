#pragma once

#include "./tools.h"
#include "./insertion_sort.h"

// ------------------------- QUICK SORT ---------------------------- #
// In-Place: requires O(1) of auxiliary memory space.
// Non-Stable: does not change the relative order of elements with equal keys.
// Offline: is given the whole list from the beginning
// Notes: divide-and-conquer approach, fastest in practice
//
// Runtime T(n):
//   Best: T(n) ~ n * log(n)
//   Average: T(n) ~ 2 * n * ln(n)
//   Worst: T(n) ~ 1/2 * n^2
//
// Asymptotically Analysis (Big O)
//   Best: T(n) = O(n * log(n))
//   Average: T(n) = O(n * ln(n))
//   Worst: T(n) = O(n^2)
//
// -----------------------------------------------------------------------#
//------------- Quicksort Interface Definition---------------//
class Quick
{
private:
    template <class T>
    static int partition(T &a, unsigned int low, unsigned int high);

public:
    template <class T>
    static void sort(T &a, unsigned int low, unsigned int high);

    template <class T>
    static void sortCutoff(T &a, unsigned int low, unsigned int high, unsigned int cut);

    template <class T>
    static void sort3Way(T &a, unsigned int low, unsigned int high);
};

//------------- Quicksort Implementation ---------------//
// partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi]
// and return the index j.
template <class T>
int Quick::partition(T &a, unsigned int low, unsigned int high)
{
    unsigned int i = low;
    unsigned int j = high + 1;
    auto v = a[low];

    while (true)
    {
        // Find item on low to swap
        while (a[++i] < v)
        {
            if (i == high)
            {
                break;
            }
        }

        // Find item on high to swap
        while (v < a[--j])
        {
            if (j == low)
            {
                break;
            }
        }

        // Check if pointers cross
        if (i >= j)
        {
            break;
        }

        // swap
        tools::swap(a, i, j);
    }

    // Put partitioning item v at a[j]
    tools::swap(a, low, j);

    // now, a[low ... j-1] <= a[j] <= a[j+1 ... high] partitioning.
    return j;
}

template <class T>
void Quick::sort(T &a, unsigned int low, unsigned int high)
{
    if (high <= low)
    {
        return;
    }

    // Make the partition of j
    int j = partition(a, low, high);

    // sort from low to j-1
    sort(a, low, j - 1);

    // sort from j+1 to high
    sort(a, j + 1, high);
}

template <class T>
void Quick::sortCutoff(T &a, unsigned int low, unsigned int high, unsigned int cut)
{
    if (high <= low + cut)
    {
        Insertion::sort(a, low, high);
        return;
    }

    // Make the partition of j
    int j = partition(a, low, high);

    // sort from low to j-1
    sortCutoff(a, low, j - 1, cut);

    // sort from j+1 to high
    sortCutoff(a, j + 1, high, cut);
}

// TODO: CHECK FOR WRONG SORTING BEHAVIOR
template <class T>
void Quick::sort3Way(T &a, unsigned int low, unsigned int high)
{
    if (high <= low)
    {
        return;
    }

    unsigned int lt = low;
    unsigned int gt = high;
    auto &v = a[low];

    unsigned int i = low + 1;

    while (i <= gt)
    {
        if (a[i] < v)
        {
            tools::swap(a, lt, i);
            lt = lt + 1;
            i = i + 1;
        }
        else if (a[i] > v)
        {
            tools::swap(a, i, gt);
            gt = gt - 1;
        }
        else if (a[i] == v)
        {
            i = i + 1;
        }
    }
    // sort from low to lt-1
    sort3Way(a, low, lt - 1);

    // sort from gt+1 to high
    sort3Way(a, gt + 1, high);
}
