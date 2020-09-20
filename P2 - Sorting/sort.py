"""
This is a module that contains implementations of
four main sorting methods.
Project 2 CS2420
Mike Hollingshaus
"""
import time
import random
import math
from recursioncounter import RecursionCounter

#------ START SORT FUNCTIONS -------#

def quicksort(lyst):
    """
    Implementation of quicksort, recurses using 2 helpers.
    Work is offloaded to quicksort_helper
    """
    test_is_lyst_and_contains_int(lyst)
    quicksort_helper(lyst, 0, len(lyst) - 1)
    return lyst

def mergesort(lyst):
    """
    Implementation of mergesort. recurses to divide
    list into left and right sub arrays and sorts each
    by dividing into more left and right sub arrays.
    Debugging was a bit of a pain, NGL.
    Worst: O(nlogn)
    """
    test_is_lyst_and_contains_int(lyst)
    RecursionCounter()
    if len(lyst) < 2:
        return lyst
    mid_index = math.floor(len(lyst) / 2)
    left_sub_list = lyst[0:mid_index]
    right_sub_list = lyst[mid_index: len(lyst)]
    mergesort(left_sub_list)
    mergesort(right_sub_list)
    lyst = merge(left_sub_list, right_sub_list, lyst)
    return lyst

def insertion_sort(lyst):
    """
    Implementation of Insertionsort. Improved
    variation of Bubble Sort. Splits array into sorted
    and non-sorted, then iterates through non-sorted
    and sorts 0th index into sorted in correct order.
    """
    test_is_lyst_and_contains_int(lyst)
    itr_unsorted = 1
    while itr_unsorted < len(lyst):
        insertion_data = lyst[itr_unsorted]
        itr_sorted = itr_unsorted - 1
        while itr_sorted >= 0:
            if insertion_data < lyst[itr_sorted]:
                lyst[itr_sorted + 1] = lyst[itr_sorted]
                itr_sorted -= 1
            else:
                break
        lyst[itr_sorted + 1] = insertion_data
        itr_unsorted += 1
    return lyst

def selection_sort(lyst):
    """
    Implementation of selectionsort. searches entire list for
    smallest. If it's not in the first position, it swaps them.
    Does this for the duration of the list.
    """
    test_is_lyst_and_contains_int(lyst)
    itr = 0
    while itr < len(lyst) - 1:
        low_index = itr
        itr_next = low_index + 1
        while itr_next < len(lyst):
            if lyst[itr_next] < lyst[low_index]:
                low_index = itr_next
            itr_next += 1
        if low_index != itr:
            swap_at_indexes(lyst, low_index, itr)
        itr += 1
    return lyst

#------ END SORT FUNCTIONS ------#

#------ START HELPER FUNCTIONS ------#

def quicksort_helper(lyst, left_index, right_index):
    """
    Performs quicksort, recursively calls itself for left
    and right bounded partitions until it finishes sorting sub-arrays
    """
    RecursionCounter()
    if left_index < right_index:
        pivot_index = partition(lyst, left_index, right_index)
        quicksort_helper(lyst, left_index, pivot_index - 1)
        quicksort_helper(lyst, pivot_index + 1, right_index)

def partition(lyst, left_index, right_index):
    """
    Helper method for quicksort.
    Swaps mid index value with last index value.
    Sorts from lower bound value to higher bound index.
    Returns leftbound.
    """
    mid_index = math.floor((left_index + right_index) / 2)
    pivot = lyst[mid_index]
    lyst[mid_index] = lyst[right_index]
    lyst[right_index] = pivot

    leftbound = left_index
    for index_itr in range(left_index, right_index):
        if lyst[index_itr] < pivot:
            swap_at_indexes(lyst, leftbound, index_itr)
            leftbound += 1

    swap_at_indexes(lyst, right_index, leftbound)
    return leftbound

def merge(left_array, right_array, lyst):
    """
    Method that merges sorted left sub-array
    and sorted right sub-array into main lyst.
    """
    length_left = len(left_array)
    length_right = len(right_array)
    left_index = 0
    right_index = 0
    main_index = 0

    while left_index < length_left and right_index < length_right:
        if left_array[left_index] <= right_array[right_index]:
            lyst[main_index] = left_array[left_index]
            main_index += 1
            left_index += 1
        else:
            lyst[main_index] = right_array[right_index]
            main_index += 1
            right_index += 1

    while left_index < length_left:
        lyst[main_index] = left_array[left_index]
        left_index += 1
        main_index += 1

    while right_index < length_right:
        lyst[main_index] = right_array[right_index]
        right_index += 1
        main_index += 1

    return lyst

def swap_at_indexes(lyst, index1, index2):
    """
    Takes 2 indexes and swaps data at each index.
    Really I don't know how to make the description more simple.
    """
    temp = lyst[index1]
    lyst[index1] = lyst[index2]
    lyst[index2] = temp

def is_sorted(lyst):
    """
    Method that returns True if lyst is sorted,
    False otherwise. Compares sorted copy of lyst
    to lyst and if same returns True.
    """
    test_is_lyst_and_contains_int(lyst)
    copy_of_lyst = lyst
    if sorted(copy_of_lyst) == lyst:
        return True
    return False

def test_is_lyst_and_contains_int(lyst_test):
    """
    Helper function to test if parameter is a list.
    Also tests if all values in lyst are int
    """
    try:
        isinstance(lyst_test, list)
        for i in lyst_test:
            int(i)
    except ValueError:
        raise ValueError("ValueError: List does not contain all ints")
    except TypeError:
        raise TypeError("Lyst input parameter is not of type lyst")

def execute_sort_and_time_helper(lyst, sorttype):
    """
    Helper function for main to execute each sorting function.
    """
    perf_timer_start = time.perf_counter()
    if sorttype == "quick":
        sort = quicksort(lyst)
    elif sorttype == "merge":
        sort = mergesort(lyst)
    elif sorttype == "selection":
        sort = selection_sort(lyst)
    elif sorttype == "insertion":
        sort = insertion_sort(lyst)
    elif sorttype == "tim":
        sort = lyst.sort()
    perf_timer_stop = time.perf_counter()
    lyst_is_sorted = is_sorted(lyst)
    if not lyst_is_sorted:
        return False
    if lyst_is_sorted:
        if sorttype == "quick":
            success_msg = "quicksort duration: {:.6f} seconds\n"
            print(success_msg.format(perf_timer_stop - perf_timer_start))
        elif sorttype == "merge":
            success_msg = "mergesort duration {:.6f} seconds\n"
            print(success_msg.format(perf_timer_stop - perf_timer_start))
        elif sorttype == "selection":
            success_msg = "selection_sort duration {:.6f} seconds\n"
            print(success_msg.format(perf_timer_stop - perf_timer_start))
        elif sorttype == "insertion":
            success_msg = "insertion_sort duration {:.6f} seconds\n"
            print(success_msg.format(perf_timer_stop - perf_timer_start))
        elif sorttype == 'tim':
            success_msg = "timsort duration: {:.6f} seconds\n"
            print(success_msg.format(perf_timer_stop - perf_timer_start))

#------ END HELPER FUNCTIONS ------#

#------ START MAIN FUNCTION ------#

def main():
    """
    Main driver function. Sorts lists and times how long it takes.
    """
    data_size = 2000
    random.seed(0)
    data = random.sample(range(data_size * 3), k = 200)
    test_insertion = data.copy()
    test_selection = data.copy()
    test_merge = data.copy()
    test_quick = data.copy()
    test_tim = data.copy()
    print("Starting selection_sort")
    execute_sort_and_time_helper(test_selection, "selection")
    print("Starting insertionsort")
    execute_sort_and_time_helper(test_insertion, "insertion")
    print("Starting mergesort")
    execute_sort_and_time_helper(test_merge, "merge")
    print("Starting quicksort")
    execute_sort_and_time_helper(test_quick, "quick")
    print("Starting timsort")
    execute_sort_and_time_helper(test_tim, "tim")

main()
