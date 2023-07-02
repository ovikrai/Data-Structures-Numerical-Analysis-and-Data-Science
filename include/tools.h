#pragma once

#include <string>
#include <iostream>

namespace tools
{
    // PREFIX TYPE DEFINITION OF THIS NAMESPACE
    using Prefix = const std::string;

    // PREFIX CONSOLE STRINGS
    Prefix PREFIX_GENERIC = "#####| ";
    Prefix SEPARATOR = "############################################################";
    Prefix PREFIX_START_MAIN = "[=================== START MAIN PROCESS ===================]";
    Prefix PREFIX_END_MAIN = "[===================  END MAIN PROCESS  ===================]";

    Prefix PREFIX_START_PUBLIC = "#####|+START++++|+PUBLIC METHOD++ : ";
    Prefix PREFIX_START_PRIVATE = "#####| START    | PRIVATE METHOD  : ";
    Prefix PREFIX_START_FUNC = "#####| START    | FUNCTION        : ";
    Prefix PREFIX_START_CONSTRUC = "#####| START    | CONSTRUCTOR     : ";
    Prefix PREFIX_START_DESTRUC = "#####| START    | DESTRUCTOR      : ";
    Prefix PREFIX_END_PUBLIC = "#####|+END++++++|+PUBLIC METHOD++ : ";
    Prefix PREFIX_END_PRIVATE = "#####| END      | PRIVATE METHOD  : ";
    Prefix PREFIX_END_FUNC = "#####| END      | FUNCTION        : ";
    Prefix PREFIX_END_CONSTRUC = "#####| END      | CONSTRUCTOR     : ";
    Prefix PREFIX_END_DESTRUC = "#####| END      | DESTRUCTOR      : ";
    Prefix PREFIX_RETURN = "#####| RETURN   |=VALUE OUTPUT==> : ";
    Prefix PREFIX_RENDER = "#####| RENDER   |===============> : ";

    Prefix PREFIX_WARNING = "##!##| WARNING  | ";
    Prefix PREFIX_EXEPTION = "#!!!#| EXEPTION | ";
    Prefix PREFIX_ERROR = "!X!X!| ERROR    | ";

    // TOOL FUNCTION THAT RENDER TEXT
    void renderMessage(Prefix prefix, std::string message)
    {
        std::cout << prefix << message << std::endl;
    }

    void renderSentance(std::string sentance)
    {
        std::cout << sentance << std::endl;
    }

    void renderWord(std::string word)
    {
        std::cout << word;
    }

    void renderLinespace()
    {
        std::cout << std::endl;
    }

    void clearScreen()
    {
        std::cout << std::flush;
    }

    void renderPrefix(std::string title, std::string message)
    {
        if (title.length() <= 20)
        {
            std::cout << PREFIX_GENERIC << title << " : " << message << std::endl;
        }
        else
        {
            throw PREFIX_EXEPTION + "title length have to be 20 or less";
        }
    }

    //-------------------- Array utility funtions ---------------
    // Swap utility functions
    // exchange a[i] and a[j]
    template <class T>
    void swap(T &a, unsigned int i, unsigned int j)
    {
        auto swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

    // Printing Array
    template <class T>
    void show(T a, unsigned int low, unsigned int high)
    {
        unsigned int i;
        std::cout << "########## START: SHOW ARRAY" << std::endl;
        for (i = low; i <= high; i++)
        {
            // Print start bracket
            if (i == low)
            {
                std::cout << "< " << a[i] << ", ";
            }
            // Print end braket
            else if (i == high)
            {
                std::cout << a[i] << " >";
            }
            else
            {
                std::cout << a[i] << ", ";
            }
        }
        std::cout << std::endl;
        std::cout << "########## END: SHOW ARRAY" << std::endl;
    }

}