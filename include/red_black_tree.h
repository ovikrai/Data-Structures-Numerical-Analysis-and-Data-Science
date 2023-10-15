#pragma once

#include "./node.h"
#include "./tools.h"

template <class K, class V>
class RedBlackTree
{
private:
    // ------------------- DATA --------------------- //
    ColoredNode<K, V> *root;
    constexpr static bool RED = true;
    constexpr static bool BLACK = false;

    // ------------------- PRIVATE METHODS --------------------- //
    bool isRed(ColoredNode<K, V> *node);
    int size(ColoredNode<K, V> *node);

    V *get(ColoredNode<K, V> *node, K key);
    ColoredNode<K, V> *put(ColoredNode<K, V> *node, K key, V value);
    ColoredNode<K, V> *deleteMin(ColoredNode<K, V> *node);
    ColoredNode<K, V> *deleteMax(ColoredNode<K, V> *node);
    ColoredNode<K, V> *deleteNode(ColoredNode<K, V> *node, K key);
    ColoredNode<K, V> *min(ColoredNode<K, V> *node);
    ColoredNode<K, V> *max(ColoredNode<K, V> *node);

public:
    // ------------------- CONSTRUCTORS --------------------- //
    // Default Root Node constructor
    RedBlackTree();

    // ------------------- METHODS --------------------- //
    bool isEmpty();
    int size();
    bool contains(K key);

    V *get(K key);
    void put(K key, V value);
    void deleteMin();
    void deleteMax();
    void deleteNode(K key);
    K *min();
    K *max();
};

// ----------------------------------------------------------------------------- //
// ----------------------------------------------------------------------------- //
// ----------------------------------------------------------------------------- //
// -------------------------- PRIVATE METHODS IMPLEMENTATION -------------------- //
// ----------------------------------------------------------------------------- //
// ----------------------------------------------------------------------------- //
// ----------------------------------------------------------------------------- //
// return number of key-value pairs in BST rooted at x
template <class K, class V>
int RedBlackTree<K, V>::size(ColoredNode<K, V> *node)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    if (node == nullptr)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "NODE SIZE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return 0;
    }
    else
    {
        tools::renderMessage(tools::PREFIX_RETURN, "NODE SIZE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return node->size;
    }
}

// is node x red; false if x is null ?
template <class K, class V>
bool RedBlackTree<K, V>::isRed(ColoredNode<K, V> *node)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    if (node == nullptr)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "FALSE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return false;
    }
    if (node->color == this->RED)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "TRUE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return true;
    }
    else
    {
        tools::renderMessage(tools::PREFIX_RETURN, "FALSE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return false;
    }
}

// ----------------------------------------------------------------------------- //
// ----------------------------------------------------------------------------- //
// ----------------------------------------------------------------------------- //
// -------------------------- PUBLIC METHODS IMPLEMENTATION -------------------- //
// ----------------------------------------------------------------------------- //
// ----------------------------------------------------------------------------- //
// ----------------------------------------------------------------------------- //
// Default Tree Constructor
template <class K, class V>
RedBlackTree<K, V>::RedBlackTree()
{
    tools::renderMessage(tools::PREFIX_START_CONSTRUC, __PRETTY_FUNCTION__);
    this->root = nullptr;
    tools::renderMessage(tools::PREFIX_END_CONSTRUC, __PRETTY_FUNCTION__);
}

// Returns true if this symbol table is empty.
template <class K, class V>
bool RedBlackTree<K, V>::isEmpty()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    if (this->size() == 0)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "TRUE");
        tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
        tools::renderLinespace();
        return true;
    }
    else
    {
        tools::renderMessage(tools::PREFIX_RETURN, "FALSE");
        tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
        tools::renderLinespace();
        return false;
    }
}

// Returns the number of key-value pairs in this symbol table.
template <class K, class V>
int RedBlackTree<K, V>::size()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderMessage(tools::PREFIX_RETURN, "STRUCTURE SIZE");
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
    return this->size(this->root);
}