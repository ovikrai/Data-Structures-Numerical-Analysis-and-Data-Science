#include <iostream>

#include "./include/merge_sort.h"
#include "./include/quick_sort.h"
#include "./include/node.h"
#include "./include/binary_search_tree.h"
#include "./include/red_black_tree.h"
#include "./include/tools.h"
#include "./include/shell_sort.h"
#include "./include/insertion_sort.h"

int main(int argc, char const *argv[])
{
    tools::renderSentance(tools::PREFIX_START_MAIN);
    tools::renderLinespace();

    // ------------------- SORT ALGOS ---------------------//
    // Array and variables declarations
    // int a[] = {2, 6, 7, 4, -3, 24, 5, 245, 3, 1, 7, 32, 6, 2, -8, 6, 4, -2, 9};
    // int a_1[] = {2, 6, 7, 4, -3, 24, 5, 245, 3, 1, 7, 32, 6, 2, -8, 6, 4, -2, 9};

    int b_0[] = {2, 6, 7, 4, -3, 24, 5, 245, 3, 1, 7, 32, 6, 2, -8, 6, 4, -2, 9};
    int b_1[] = {2, 6, 7, 4, -3, 24, 5, 245, 3, 1, 7, 32, 6, 2, -8, 6, 4, -2, 9};
    int b_2[] = {2, 6, 7, 4, -3, 24, 5, 245, 3, 1, 7, 32, 6, 2, -8, 6, 4, -2, 9};

    // int c[] = {2, 6, 7, 4, -3, 24, 5, 245, 3, 1, 7, 32, 6, 2, -8, 6, 4, -2, 9};
    // int d[] = {2, 6, 7, 4, -3, 24, 5, 245, 3, 1, 7, 32, 6, 2, -8, 6, 4, -2, 9};

    // int aux[19];

    auto hi = 18;
    auto lo = 0;

    // MERGESORT TEST
    // std::cout << "########## START: MERGESORT: TOP-DOWN ##########" << std::endl;
    // tools::show(a, lo, hi);
    // Merge::sortTopDown(a, aux, lo, hi);
    // tools::show(a, lo, hi);
    // std::cout << "########## END: MERGESORT TOP-DOWN ##########" << std::endl;
    // tools::renderLinespace();

    // std::cout << "########## START: MERGESORT BUTTON-UP ##########" << std::endl;
    // tools::show(a_1, lo, hi);
    // Merge::sortButtonUp(a_1, hi);
    // tools::show(a_1, lo, hi);
    // std::cout << "########## END: MERGESORT BUTTON-UP ##########" << std::endl;
    // tools::renderLinespace();

    // QUICKSORT TEST
    std::cout << "########## START: QUICKSORT ##########" << std::endl;
    tools::show(b_0, lo, hi);
    Quick::sort(b_0, lo, hi);
    tools::show(b_0, lo, hi);
    std::cout << "########## END: QUICKSORT ##########" << std::endl;
    tools::renderLinespace();

    std::cout << "########## START: QUICKSORT CUTOFF ##########" << std::endl;
    tools::show(b_2, lo, hi);
    Quick::sortCutoff(b_2, lo, hi, 5);
    tools::show(b_2, lo, hi);
    std::cout << "########## END: QUICKSORT CUTOFF ##########" << std::endl;
    tools::renderLinespace();

    std::cout << "########## START: QUICKSORT 3 WAY ##########" << std::endl;
    tools::show(b_1, lo, hi);
    Quick::sort3Way(b_1, lo, hi);
    tools::show(b_1, lo, hi);
    std::cout << "########## END: QUICKSORT 3 WAY ##########" << std::endl;
    tools::renderLinespace();

    // SHELLSORT TEST
    // std::cout << "########## START: SHELLSORT ##########" << std::endl;
    // tools::show(c, lo, hi);
    // Shell::sort(c, lo, hi);
    // tools::show(c, lo, hi);
    // std::cout << "########## END: SHELLSORT ##########" << std::endl;
    // tools::renderLinespace();

    // INSERTION SORT
    // std::cout << "########## START: INSERTION ##########" << std::endl;
    // tools::show(d, lo, hi);
    // Insertion::sort(d, lo, hi);
    // tools::show(d, lo, hi);
    // std::cout << "########## END: INSERTION ##########" << std::endl;
    // tools::renderLinespace();

    // ------------------- TREE ALGOS ---------------------//
    auto treeBinary = new BinarySearchTree<int, char>();
    auto treeRedBlack = new RedBlackTree<int, char>();

    // BINARY TREE --------------- //
    // treeBinary->put(1, 'J');
    // treeBinary->put(2, 'L');
    // treeBinary->put(4, 'M');
    // treeBinary->put(5, 'N');

    // treeBinary->render();
    // treeBinary->renderMeta();

    // RED BLACK TREE --------------- //
    int treeSize = treeRedBlack->size();
    std::cout << "#####| TREE SIZE: " << treeSize << std::endl;

    // ------------------- END OF PROCESS MESSAGES ---------------------//
    tools::renderSentance(tools::PREFIX_END_MAIN);
    tools::renderLinespace();
    return 0;
}
