"""
ECE 590
Project 1
Fall 2022

Partner 1: Koushik Annareddy Sreenath (ka266)
Partner 2: Shravan Mysore Seetharam (sm952)
Date: 9-Nov-2022
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    size = range(0, len(listToSort) - 1)

    for i in size:
        min_index = i
        for j in range(i + 1, len(listToSort)):
            if listToSort[min_index] > listToSort[j]:
                min_index = j
        if min_index != i:
            listToSort[min_index], listToSort[i] = listToSort[i], listToSort[min_index]

    
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    size = range(1, len(listToSort))

    for i in size:
        curr = listToSort[i]
        while i > 0 and curr < listToSort[i - 1]:
            listToSort[i], listToSort[i - 1] = listToSort[i - 1], listToSort[i]
            i = i - 1

    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
