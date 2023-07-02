#pragma once

#include <queue>
#include <iostream>
#include "./tools.h"
#include "./node.h"

template <class K, class V>
class BinarySearchTree
{
private:
    // ------------------- DATA --------------------- //
    Node<K, V> *root;

    // ------------------- PRIVATE METHODS --------------------- //
    int size(Node<K, V> *node);

    V *get(Node<K, V> *node, K key);
    Node<K, V> *put(Node<K, V> *node, K key, V value);
    Node<K, V> *deleteMin(Node<K, V> *node);
    Node<K, V> *deleteMax(Node<K, V> *node);
    Node<K, V> *deleteNode(Node<K, V> *node, K key);
    Node<K, V> *min(Node<K, V> *node);
    Node<K, V> *max(Node<K, V> *node);

public:
    // ------------------- CONSTRUCTORS --------------------- //
    // Default Root Node constructor
    BinarySearchTree();

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

    void render();
    void renderMeta();
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
int BinarySearchTree<K, V>::size(Node<K, V> *node)
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

// Returns the value associated with the given key.
template <class K, class V>
V *BinarySearchTree<K, V>::get(Node<K, V> *node, K key)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    // NULL CHECKS
    // It check if key is a nullpointer of the type K
    if (&key == nullptr)
    {
        throw tools::PREFIX_EXEPTION + "get() method, key parameter is equal to null pointer";
    }
    if (node == nullptr)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "NULL POINTER");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return nullptr;
    }

    // COMPARATIONS
    if (key < node->key)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "RECURSION CALL");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return this->get(node->left, key);
    }
    else if (key > node->key)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "RECURSION CALL");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return this->get(node->right, key);
    }
    else
    {
        tools::renderMessage(tools::PREFIX_RETURN, "NODE VALUE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return &node->value;
    }
    tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
}

/**
 * Inserts the specified key-value pair into the symbol table, overwriting the old
 * value with the new value if the symbol table already contains the specified key.
 * Deletes the specified key (and its associated value) from this symbol table
 * if the specified value is null pointer.
 */
template <class K, class V>
Node<K, V> *BinarySearchTree<K, V>::put(Node<K, V> *node, K key, V value)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    // Null Check
    if (node == nullptr)
    {
        auto newNode = new Node<K, V>(key, value, 1);

        tools::renderMessage(tools::PREFIX_RETURN, "NODE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return newNode;
    }

    // COMPARATIONS
    if (key < node->key)
    {
        node->left = this->put(node->left, key, value);
    }
    else if (key > node->key)
    {
        node->right = this->put(node->right, key, value);
    }
    else
    {
        node->value = value;
    }

    // Incrise size of node by one
    node->size = 1 + this->size(node->left) + this->size(node->right);

    tools::renderMessage(tools::PREFIX_RETURN, "NODE");
    tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
    return node;
}

// Removes the smallest key and associated value from the symbol table.
template <class K, class V>
Node<K, V> *BinarySearchTree<K, V>::deleteMin(Node<K, V> *node)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    if (node->left == nullptr)
    {
        return node->right;
    }
    node->left = this->deleteMin(node->left);
    node->size = this->size(node->left) + this->size(node->right) + 1;

    tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
    tools::renderMessage(tools::PREFIX_RETURN, "NODE");
    return node;
}

// Removes the largest key and associated value from the symbol table.
template <class K, class V>
Node<K, V> *BinarySearchTree<K, V>::deleteMax(Node<K, V> *node)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    if (node->right == nullptr)
    {
        return node->left;
    }
    node->right = this->deleteMax(node->right);
    node->size = this->size(node->left) + this->size(node->right) + 1;

    tools::renderMessage(tools::PREFIX_RETURN, "NODE");
    tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
    return node;
}

// Removes the specified key and its associated value from this symbol table
template <class K, class V>
Node<K, V> *BinarySearchTree<K, V>::deleteNode(Node<K, V> *node, K key)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    if (node == nullptr)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "NULL POINTER");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return nullptr;
    }

    if (key < node->key)
    {
        node->left = this->deleteNode(node->left, key);
    }
    else if (key > node->key)
    {
        node->right = this->deleteNode(node->right, key);
    }
    else
    {
        // check left and right for null pointer
        if (node->right == nullptr)
        {
            tools::renderMessage(tools::PREFIX_RETURN, "NODE");
            tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
            return node->left;
        }
        if (node->left == nullptr)
        {
            tools::renderMessage(tools::PREFIX_RETURN, "NODE");
            tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
            return node->right;
        }

        // Creating Auxiliary node
        Node<K, V> *temp_node = node;
        node = this->min(temp_node->right);
        node->right = this->deleteMin(temp_node->right);
        node->left = temp_node->left;
    }

    // Change size
    node->size = this->size(node->left) + this->size(node->right) + 1;

    tools::renderMessage(tools::PREFIX_RETURN, "NODE");
    tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
    return node;
}

// Returns the smallest key in the symbol table.
template <class K, class V>
Node<K, V> *BinarySearchTree<K, V>::min(Node<K, V> *node)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    if (node->left == nullptr)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "NODE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return node;
    }
    else
    {
        tools::renderMessage(tools::PREFIX_RETURN, "RECURSION CALL");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return this->min(node->left);
    }
}

// Returns the largest key in the symbol table.
template <class K, class V>
Node<K, V> *BinarySearchTree<K, V>::max(Node<K, V> *node)
{
    tools::renderMessage(tools::PREFIX_START_PRIVATE, __PRETTY_FUNCTION__);
    if (node->right == nullptr)
    {
        tools::renderMessage(tools::PREFIX_RETURN, "NODE");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return node;
    }
    else
    {
        tools::renderMessage(tools::PREFIX_RETURN, "RECURSION CALL");
        tools::renderMessage(tools::PREFIX_END_PRIVATE, __PRETTY_FUNCTION__);
        return this->max(node->right);
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
BinarySearchTree<K, V>::BinarySearchTree()
{
    tools::renderMessage(tools::PREFIX_START_CONSTRUC, __PRETTY_FUNCTION__);
    this->root = nullptr;
    tools::renderMessage(tools::PREFIX_END_CONSTRUC, __PRETTY_FUNCTION__);
}

// Returns true if this symbol table is empty.
template <class K, class V>
bool BinarySearchTree<K, V>::isEmpty()
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
int BinarySearchTree<K, V>::size()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderMessage(tools::PREFIX_RETURN, "STRUCTURE SIZE");
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
    return this->size(this->root);
}

// Does this symbol table contain the given key?
template <class K, class V>
bool BinarySearchTree<K, V>::contains(K key)
{

    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    if (&key == nullptr)
    {
        throw tools::PREFIX_EXEPTION + "argument to contains() is null";
    }

    if (this->get(key) != nullptr)
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

// Returns the value associated with the given key.
template <class K, class V>
V *BinarySearchTree<K, V>::get(K key)
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderMessage(tools::PREFIX_RETURN, "NODE VALUE");
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
    return this->get(this->root, key);
}

/**
 * Inserts the specified key-value pair into the symbol table, overwriting the old
 * value with the new value if the symbol table already contains the specified key.
 * Deletes the specified key (and its associated value) from this symbol table
 * if the specified value is null pointer.
 */
template <class K, class V>
void BinarySearchTree<K, V>::put(K key, V value)
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    // NULL CHECK
    if (&key == nullptr)
    {
        throw tools::PREFIX_EXEPTION + "calls put() with a null pointer key";
    }
    if (&value == nullptr)
    {
        this->deleteNode(key);
        tools::renderMessage(tools::PREFIX_RETURN, "VOID");
        tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
        tools::renderLinespace();
        return;
    }
    this->root = this->put(this->root, key, value);
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
}

// Removes the smallest key and associated value from the symbol table.
template <class K, class V>
void BinarySearchTree<K, V>::deleteMin()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    if (this->isEmpty())
    {
        throw tools::PREFIX_EXEPTION + "Element dont exist, symbol table underflow";
    }
    this->root = this->deleteMin(this->root);
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
}

// Removes the largest key and associated value from the symbol table.
template <class K, class V>
void BinarySearchTree<K, V>::deleteMax()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    if (this->isEmpty())
    {
        throw tools::PREFIX_EXEPTION + "Symbol table underflow";
    }
    root = this->deleteMax(this->root);
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
}

// Removes the specified key and its associated value from this symbol table
template <class K, class V>
void BinarySearchTree<K, V>::deleteNode(K key)
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    if (&key == nullptr)
    {
        throw tools::PREFIX_EXEPTION + "calls delete() with a null key";
    }
    this->root = this->deleteNode(this->root, key);
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
}

// Returns the smallest key in the symbol table.
template <class K, class V>
K *BinarySearchTree<K, V>::min()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    if (this->isEmpty())
    {
        throw tools::PREFIX_EXEPTION + "calls min() with empty symbol table";
    }

    auto min = this->min(this->root);
    tools::renderMessage(tools::PREFIX_RETURN, "NODE KEY");
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
    return &min->key;
}

// Returns the largest key in the symbol table.
template <class K, class V>
K *BinarySearchTree<K, V>::max()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    if (this->isEmpty())
    {
        throw tools::PREFIX_EXEPTION + "calls max() with empty symbol table";
    }
    auto max = this->max(this->root);
    tools::renderMessage(tools::PREFIX_RETURN, "NODE KEY");
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
    return &max->key;
}

template <class K, class V>
void BinarySearchTree<K, V>::render()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);
    auto max = this->max(this->root);

    for (int i = 0; i <= max->key; i++)
    {
        auto value = this->get(this->root, i);
        if (value == nullptr)
        {
            std::cout << tools::PREFIX_RENDER
                      << "NODE: KEY = " << i << ", "
                      << "VALUE = NULL POINTER" << std::endl;
        }
        else
        {
            std::cout << tools::PREFIX_RENDER
                      << "NODE: KEY = " << i << ", "
                      << "VALUE = " << value << std::endl;
        }
    }
    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
}

template <class K, class V>
void BinarySearchTree<K, V>::renderMeta()
{
    tools::renderMessage(tools::PREFIX_START_PUBLIC, __PRETTY_FUNCTION__);

    int size = this->size(this->root);
    Node<K, V> *maxNode = this->max(this->root);
    Node<K, V> *minNode = this->min(this->root);

    std::cout << tools::PREFIX_RENDER
              << "STRUCTURE SIZE: " << size << std::endl;

    std::cout << tools::PREFIX_RENDER
              << "MINIMUN NODE: KEY = " << minNode->key << ", "
              << "VALUE = " << minNode->value << std::endl;

    std::cout << tools::PREFIX_RENDER
              << "MAXIMUN NODE: KEY = " << maxNode->key << ", "
              << "VALUE = " << maxNode->value << std::endl;

    tools::renderMessage(tools::PREFIX_END_PUBLIC, __PRETTY_FUNCTION__);
    tools::renderLinespace();
}