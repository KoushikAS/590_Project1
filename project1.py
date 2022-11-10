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
    return listToSort


"""
InsertionSort
"""


def InsertionSort(listToSort):
    return listToSort


"""
BubbleSort: is a sorting algorithm, which works on pushing the greatest element from unsortedlist to end every cycle. 
Best Case: Ω(n)
Average Case: θ(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
"""


def BubbleSort(listToSort):
    n = len(listToSort)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Swapping the elements if the element at j is greater than j+1
            if listToSort[j] > listToSort[j + 1]:
                tmp = listToSort[j]
                listToSort[j] = listToSort[j + 1]
                listToSort[j + 1] = tmp

    return listToSort


"""
MergeSort: is a recursive sorting algorithm, which works by dividing the list into smaller lists and then combines them 
in a sorted manner.
Best Case: Ω(n log(n))
Average Case: θ(n log(n))
Worst Case: O(n log(n))
Space Cmplexity: O(n)
"""


def MergeSort(listToSort):
    if len(listToSort) <= 1:
        return listToSort

    mid = len(listToSort) // 2
    list1 = MergeSort(listToSort[:mid])
    list2 = MergeSort(listToSort[mid:])
    index = 0

    while (len(list1) != 0) and (len(list2) != 0):
        if list1[0] < list2[0]:
            listToSort[index] = list1.pop(0)
        else:
            listToSort[index] = list2.pop(0)
        index += 1

    while len(list1) != 0:
        listToSort[index] = list1.pop(0)
        index += 1

    while len(list2) != 0:
        listToSort[index] = list2.pop(0)
        index += 1

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
    # print('Testing Selection Sort')
    # print()
    # testingSuite(SelectionSort)
    # print()
    # print('Testing Insertion Sort')
    # print()
    # testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    # print('Testing Quick Sort')
    # print()
    # testingSuite(QuickSort)
    # print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
