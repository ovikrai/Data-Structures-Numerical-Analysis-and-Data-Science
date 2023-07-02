#pragma once
#include <algorithm>
#include "./tools.h"

// ------------------------- MERGE SORT ---------------------------- #
// Out-of-Place: requires O(n) of auxiliary memory space.
// Stable: does not change the relative order of elements with equal keys.
// Online: can sort a list as it receives it.
// Notes: divide-and-conquer approach
//
// Runtime T(n):
//   Best: T(n) ~ 1/2 * n * log(n)
//   Average: T(n) ~ n * log(n)
//   Worst: T(n) ~ n  * log(n)
//
// Asymptotically Analysis (Big O)
//   Best: T(n) = O(n * log(n))
//   Average: T(n) = O(n * log(n))
//   Worst: T(n) = O(n * log(n))
//
// -----------------------------------------------------------------------#
//------------- Mergesort Interface Definition---------------//
class Merge
{
private:
    template <class T>
    static void merge(T &a, T &aux, unsigned int low, unsigned int mid, unsigned int high);

public:
    template <class T>
    static void sortTopDown(T &a, T &aux, unsigned int low, unsigned int high);

    template <class T>
    static void sortButtonUp(T &a, unsigned int n);
};

//------------- Mergesort Implementation ---------------//
// stably merge a[lo .. mid] with a[mid+1 ..hi] using aux[lo .. hi]
template <class T>
void Merge::merge(T &a, T &aux, unsigned int low, unsigned int mid, unsigned int high)
{
    unsigned int k;
    // Copy array to auxilliar array
    for (k = low; k <= high; k++)
    {
        aux[k] = a[k];
    }

    unsigned int i = low;
    unsigned int j = mid + 1;
    // Merge back to main array
    for (k = low; k <= high; k++)
    {
        if (i > mid)
        {
            a[k] = aux[j++];
        }
        else if (j > high)
        {
            a[k] = aux[i++];
        }
        else if (aux[j] < aux[i])
        {
            a[k] = aux[j++];
        }
        else
        {
            a[k] = aux[i++];
        }
    }
}

template <class T>
void Merge::sortTopDown(T &a, T &aux, unsigned int low, unsigned int high)
{
    // Check if are in order and return null
    if (high <= low)
    {
        return;
    }

    // Calculate the midpoint
    unsigned int mid = low + ((high - low) / 2);

    // Sort low to mid then mid to high and merge
    sortTopDown(a, aux, low, mid);
    sortTopDown(a, aux, mid + 1, high);
    merge(a, aux, low, mid, high);
}

template <class T>
void Merge::sortButtonUp(T &a, unsigned int n)
{
    // Auxiliary Memory
    T aux;

    for (unsigned int len = 1; len < n + 1; len = len * 2)
    {
        for (unsigned int lo = 0; lo < n + 1 - len; lo = lo + len + len)
        {
            unsigned int mid = lo + len - 1;
            unsigned int hi = std::min(lo + len + len - 1, n);
            merge(a, aux, lo, mid, hi);
        }
    }
}
