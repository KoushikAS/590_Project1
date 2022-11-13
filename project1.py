"""
ECE 590
Project 1
Fall 2022

Partner 1: Koushik Annareddy Sreenath (ka266)
Partner 2: Shravan Mysore Seetharam (sm952)
Date: 9-Nov-2022
"""

"""
SelectionSort: is a sorting algorithm which works on pushing the lowest element from unsortedlist at the
                end of every cycle. 
Best Case: Ω(n^2)
Average Case: θ(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
"""


def SelectionSort(listToSort):
    for i in range(0, len(listToSort) - 1):
        # find out the index which contains the minimum element of the unsorted list
        min_index = i
        for j in range(i + 1, len(listToSort)):
            if listToSort[min_index] > listToSort[j]:
                min_index = j

        # swap if the min index is other than i
        if min_index != i:
            tmp = listToSort[i]
            listToSort[i] = listToSort[min_index]
            listToSort[min_index] = tmp

    return listToSort


"""
InsertionSort: is a sorting algorithm which sorts a subsection of a list every cycle.
Best Case: Ω(n)
Average Case: θ(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
"""


def InsertionSort(listToSort):
    for i in range(1, len(listToSort)):
        curr = listToSort[i]
        j = i
        # push the current element to the appropriate position in the sorted section of the list.
        while j > 0 and curr < listToSort[j - 1]:
            tmp = listToSort[j]
            listToSort[j] = listToSort[j - 1]
            listToSort[j - 1] = tmp
            j = j - 1

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
QuickSort: is a recursive sorting algorithm, which works by dividing the list based on a pivot (i.e smaller and 
            bigger elements than pivot) and then recursively sorts the sublists. 
Best Case: Ω(n*log(n))
Average Case: θ(n*log(n))
Worst Case: O(n^2)
Space Complexity: O(1)

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""


def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j is None or j > len(listToSort):
        j = len(listToSort)

    if i >= j:
        return listToSort

    # Choosing the last element of the list as the pivot element
    pivot = listToSort[j - 1]

    # A pivot index to maintain the point of pivot
    pivot_index = i

    for k in range(i, j - 1):
        # Swapping elements which are lesser than pivot at pivot index position.
        if listToSort[k] < pivot:
            tmp = listToSort[k]
            listToSort[k] = listToSort[pivot_index]
            listToSort[pivot_index] = tmp

            # incrementing the pivot index.
            pivot_index += 1

    # swapping the pivot to the appropriate place in the list (i.e. pivot index).
    tmp = listToSort[j - 1]
    listToSort[j - 1] = listToSort[pivot_index]
    listToSort[pivot_index] = tmp

    # sorting the lower portion of the list
    QuickSort(listToSort, i, pivot_index)
    # sorting the higher portion of the list
    QuickSort(listToSort, pivot_index + 1, j)
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
