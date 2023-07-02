#pragma once

#include "./tools.h"

// ----------- Node Structure -------------//
// elemental sub-structure For BinarySearchTree
template <class K, class V>
class Node
{
public:
    K key;             // sorted by key
    V value;           // Associated Data
    Node<K, V> *left;  // left subtree
    Node<K, V> *right; // right subtree
    int size;          // number of nodes in subtree

    // Methods
    Node(K key, V value, int size);
};

template <class K, class V>
Node<K, V>::Node(K key, V value, int size)
{
    tools::renderMessage(tools::PREFIX_START_CONSTRUC, __PRETTY_FUNCTION__);
    this->key = key;
    this->value = value;
    this->size = size;
    this->left = nullptr; // Make left and right node empty pointers
    this->right = nullptr;
    tools::renderMessage(tools::PREFIX_END_CONSTRUC, __PRETTY_FUNCTION__);
}

// ----------- COLORED Node Structure -------------//
// elemental sub-structure For BlackRedTree
template <class K, class V>
class ColoredNode
{
public:
    K key;             // sorted by key
    V value;           // Associated Data
    Node<K, V> *left;  // left subtree
    Node<K, V> *right; // right subtree
    bool color;        // color of parent link
    int size;          // number of nodes in subtree

    // Methods
    ColoredNode(K key, V value, bool color, int size);
};

template <class K, class V>
ColoredNode<K, V>::ColoredNode(K key, V value, bool color, int size)
{
    tools::renderMessage(tools::PREFIX_START_CONSTRUC, __PRETTY_FUNCTION__);
    this->key = key;
    this->value = value;
    this->color = color;
    this->size = size;
    this->left = nullptr; // Make left and right node empty pointers
    this->right = nullptr;
    tools::renderMessage(tools::PREFIX_END_CONSTRUC, __PRETTY_FUNCTION__);
}

// ----------- Height Node Structure -------------//
// Elemental SubStructure For AVLTree
template <class K, class V>
class HeightNode
{
public:
    K key;             // sorted by key
    V value;           // Associated Data
    Node<K, V> *left;  // left subtree
    Node<K, V> *right; // right subtree
    int height;        // height of the subtree
    int size;          // number of nodes in subtree

    // Methods
    HeightNode(K key, V value, int height, int size);
};

template <class K, class V>
HeightNode<K, V>::HeightNode(K key, V value, int height, int size)
{
    tools::renderMessage(tools::PREFIX_START_CONSTRUC, __PRETTY_FUNCTION__);
    this->key = key;
    this->value = value;
    this->height = height;
    this->size = size;
    this->left = nullptr; // Make left and right node empty pointers
    this->right = nullptr;
    tools::renderMessage(tools::PREFIX_END_CONSTRUC, __PRETTY_FUNCTION__);
}
