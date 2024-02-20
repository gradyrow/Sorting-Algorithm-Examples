"""
Grady Rowedder
Assign 2: Sorting algorithms
February 13, 2024
Time Spent: 10+ Hours
"""

import time
import random
import sys
#  from math import ceil, log10

sys.setrecursionlimit(1000000)


def bubbleSort(alist):
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements,and swaps them if they are in the wrong order. The pass
    through the list is repeated until the list is sorted.

    :param alist:
    :return:
    """
    start_time = time.time()
    n = len(alist)
    for i in range(n):
        for j in range(0, n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    elapsed_time = time.time() - start_time
    return alist, elapsed_time


def insertionSort(alist):
    """
    Insertion sort is a simple sorting algorithm that builds the final sorted array one
    item at a time. It iterates through each element of the array, comparing it with the
    elements to its left and shifting them to the right until it finds the correct position
    for the current element.

    :param alist:
    :return:
    """
    start_time = time.time()
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key
    elapsed_time = time.time() - start_time
    return alist, elapsed_time


def mergeSort(alist):
    """
    Merge sort is a divide and conquer algorithm that divides the input array into two halves,
    sorts each half recursively, and then merges the sorted halves. It works by repeatedly merging
    sublists to produce new sorted sublists until there is only one sublist remaining, which is the sorted array.

    :param alist:
    :return:
    """
    start_time = time.time()
    if len(alist) > 1:
        mid = len(alist) // 2
        L = alist[:mid]
        R = alist[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                alist[k] = L[i]
                i += 1
            else:
                alist[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            alist[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            alist[k] = R[j]
            j += 1
            k += 1
    elapsed_time = time.time() - start_time
    return alist, elapsed_time


def hybridSort(alist):
    """
    Hybrid sort is a combination of insertion sort and merge sort algorithms. It uses
    insertion sort for small input sizes and merge sort for large input sizes. This
    approach leverages the efficiency of merge sort for large datasets while benefiting
    from the simplicity and efficiency of insertion sort for small datasets. The threshold
    for choosing between the two algorithms is typically determined based on the size of
    the input array.

    :param alist:
    :return:
    """
    start_time = time.time()
    if len(alist) < 100:
        insertionSort(alist)
    else:
        mergeSort(alist)
    elapsed_time = time.time() - start_time
    return alist, elapsed_time


def counting_sort(arr, exp):
    """
    Counting sort is an integer sorting algorithm that counts the occurrences of
    each unique integer in the input array and then places each element in the
    correct position in the output array based on its count. It assumes that
    each element in the input array is an integer within a specific range.

    :param arr:
    :param exp:
    :return:
    """
    start_time = time.time()
    output = [0] * len(arr)
    count = [0] * 10

    for i in range(len(arr)):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    alist = output
    elapsed_time = time.time() - start_time
    return alist, elapsed_time


'''
def quickSort(alist, pivot='first'):  # Attempt 1
    """
    Quick sort is a divide and conquer algorithm that selects a 'pivot' element
    from the list and partitions the other elements into two sublists according
    to whether they are less than or greater than the pivot. The sublists are then recursively sorted.
    :param pivot: Pivot selection method ('first', 'middle', 'last', or 'reverse')
    :param alist: Input list to be sorted
    :return: Sorted list and elapsed time
    """
    def partition(arr, low, high):
        """
        Partition function to select a pivot and partition the list around it.
        :param arr: Input list
        :param low: Lower index of the sub-array
        :param high: Higher index of the sub-array
        :return: Index of the pivot element after partitioning
        """
        if pivot == 'first':
            pivot_index = low
        elif pivot == 'middle':
            pivot_index = (low + high) // 2
        elif pivot == 'last':
            pivot_index = high
        else:  # 'reverse'
            arr[:] = arr[::-1]  # Reverse the entire list
            pivot_index = high

        pivot_value = arr[pivot_index]

        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot_value:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    start_time = time.time()

    stack = [(0, len(alist) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(alist, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

    elapsed_time = time.time() - start_time
    return alist, elapsed_time
def quick_Sort(alist, pivot='middle'):  # Attempt 2
    """
    Quick sort is a divide and conquer algorithm that selects a 'pivot' element
    from the list and partitions the other elements into two sublists according
    to whether they are less than or greater than the pivot. The sublists are then recursively sorted.
    :param pivot: Pivot selection method ('first', 'middle', 'last', or 'reverse')
    :param alist: Input list to be sorted
    :return: Sorted list and elapsed time
    """

    def partition(alist, low, high):
        if pivot == 'first':
            pivot_index = alist[low]
        elif pivot == 'middle':
            pivot_index = alist[high // 2]
        elif pivot == 'last':
            pivot_index = alist[high]
        else:
            pivot_index = alist[high]
        pivot_value = alist[pivot_index]
        i = low - 1
        for j in range(low, high):
            if alist[j] <= pivot_value:
                i += 1
                alist[i], alist[j] = alist[j], alist[i]
        alist[i + 1], alist[pivot_index] = alist[pivot_index], alist[i + 1]
        return i + 1

    def recursive_quicksort(alist):
        stack = [(0, len(alist) - 1)]

        while stack:
            low, high = stack.pop()
            if low < high:
                pi = partition(alist, low, high)
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))

    start_time = time.time()
    recursive_quicksort(alist)
    elapsed_time = time.time() - start_time
    return alist, elapsed_time
def quickSort(alist):  # Attempt 3
    """
    Quick sort is a divide and conquer algorithm that selects a 'pivot' element
    from the list and partitions the other elements into two sublists according
    to whether they are less than or greater than the pivot. The sublists are then recursively sorted.
    :param pivot: Pivot selection method ('first', 'middle', 'last', or 'reverse')
    :param alist: Input list to be sorted
    :return: Sorted list and elapsed time
    """
    left = 0
    right = len(alist) - 1

    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1

    def quickSort2(alist, left, right):
        if left < right:
            partition_pos = partition(alist, left, right)
            if left < partition_pos:  # Ensure left sublist has more than one element
                quickSort2(alist, left, partition_pos - 1)
            if right > partition_pos:  # Ensure right sublist has more than one element
                quickSort2(alist, partition_pos + 1, right)

    start_time = time.time()
    quickSort2(alist, left, right)
    elapsed_time = time.time() - start_time
    return alist, elapsed_time

'''


def quickSort(alist, pivot='first'):  # Attempt 4: Successful & doesnt break w/ 5000 list
    """
    Quick sort is a divide and conquer algorithm that selects a 'pivot' element
    from the list and partitions the other elements into two sublists according
    to whether they are less than or greater than the pivot. The sublists are then recursively sorted.

    :param alist: Input list to be sorted
    :param pivot: Pivot selection method ('first', 'middle', 'last', or 'reverse'). Default is 'first'.
    :return: Sorted list and elapsed time
    """

    def partition(alist, low, high, pivot):
        """
        Partition function to determine the position of the pivot element.

        :param alist: Input list
        :param low: Starting index of the sublist
        :param high: Ending index of the sublist
        :param pivot: Pivot selection method ('first', 'middle', 'last', or 'reverse')
        :return: Index of the pivot element after partitioning
        """
        if pivot == 'first':
            pivot_index = low
        elif pivot == 'middle':
            pivot_index = (low + high) // 2
        elif pivot == 'last':
            pivot_index = high
        else:
            pivot_index = high

        # Swap the pivot element (at pivot_index) with the last element
        alist[pivot_index], alist[high] = alist[high], alist[pivot_index]
        pivot_value = alist[high]

        i = low - 1
        for j in range(low, high):
            if alist[j] <= pivot_value:
                i += 1
                alist[i], alist[j] = alist[j], alist[i]
        alist[i + 1], alist[high] = alist[high], alist[i + 1]
        return i + 1

    def iterative_quicksort(alist):
        """
        Iterative implementation of quicksort algorithm.

        :param alist: Input list
        """
        stack = [(0, len(alist) - 1)]

        while stack:
            low, high = stack.pop()
            if low < high:
                pi = partition(alist, low, high, pivot)
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))

    start_time = time.time()
    iterative_quicksort(alist)
    elapsed_time = time.time() - start_time
    return alist, elapsed_time


def radixSort(alist):
    """
    Radix sort is a non-comparative integer sorting algorithm that sorts data
    with integer keys by grouping keys by the individual digits which share the
    same significant position and value. It processes the digits of the numbers
    by counting occurrences of each digit and then distributing the elements based on those counts.

    :param alist:
    :return:
    """
    start_time = time.time()
    max_num = max(alist)
    exp = 1
    while max_num // exp > 0:
        counting_sort(alist, exp)
        exp *= 10
    elapsed_time = time.time() - start_time
    return alist, elapsed_time


if __name__ == '__main__':
    """ Check if the program is being run directly (i.e. not being imported) """
    def testFunction(sort_function, alist):
        """ A test utility function. """
        alist2 = alist.copy()
        res = sort_function(list(alist))
        print(f"Using {sort_function.__name__} to sort list: {alist[:10]}... w/ {len(alist)} items")
        print(f"    sort time: {res[1]:.4f} seconds")
        alist2.sort()
        print(f"    sorted correctly?: {'y :)' if res[0] == alist2 else 'n :('}")
    list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]  # helpful for early testing
    testFunction(bubbleSort, list(list1))
    testFunction(insertionSort, list(list1))
    testFunction(mergeSort, list(list1))
    testFunction(hybridSort, list(list1))
    testFunction(quickSort, list(list1))
    testFunction(radixSort, list(list1))

    random.seed(1)
    list2 = list(range(5000))
    random.shuffle(list2)
    testFunction(bubbleSort, list(list2))
    testFunction(insertionSort, list(list2))
    testFunction(mergeSort, list(list2))
    testFunction(hybridSort, list(list2))
    testFunction(quickSort, list(list2))
    testFunction(radixSort, list(list2))

    list3 = list(range(6000, 1000, -1))
    testFunction(bubbleSort, list(list3))
    testFunction(insertionSort, list(list3))
    testFunction(mergeSort, list(list3))
    testFunction(hybridSort, list(list3))
    testFunction(quickSort, list(list3))
    testFunction(radixSort, list(list3))
