import math
import random
import time
from recursioncounter import RecursionCounter

# ------- START SEARCH FUNCTIONS ------- #

def linear_search(lyst, target):
    """
    Iterates linearly through list and
    returns true if it finds target param.

    Keyword arguments:
    lyst -- List we are searchging through
    target -- Target integer we want to find
    """
    validate_int_helper(lyst, target)
    for i in lyst:
        if i == target:
            return True
    return False

def recursive_binary_search_helper(low_index, high_index, lyst, target):
    """
    Helper function to process recursion
    from initial binary_search function.

    Keyword Arguments
    lyst -- the list we are searching through
    target -- the target we are searching for
    low_index -- the lowest index of the sub-array
    high_index -- highest index of sub-array
    """
    RecursionCounter()
    if high_index >= low_index:
        mid_index = math.floor((high_index + low_index) / 2)
        if lyst[mid_index] == target:
            return True
        elif lyst[mid_index] > target:
            return recursive_binary_search_helper(low_index, mid_index - 1,lyst, target)
        else:
            return recursive_binary_search_helper(mid_index + 1, high_index, lyst, target)
    else:
        return False

def recursive_binary_search(lyst, target):
    """
    Checks if initial value is true and
    if it is, returns True, otherwise begins recursive search.

    Keyword Arguments:
    lyst -- list we are searching through
    target -- Integer we want to find
    """
    validate_int_helper(lyst, target)
    if lyst[0] == target:
        return True
    return recursive_binary_search_helper(0, len(lyst) - 1, lyst, target)

def jump_search_helper_reverse_linear_search(current_index, previous_jump_index, lyst, target):
    """
    Reverse linear search called after jump search has
    jumped past value (list[current_index] > value).

    Keyword Arguments:
    current-index -- index we are at
    previous_jump_index -- index we were at to serve as
    lyst -- list of ints to search through
    target -- value we are searching for
    """
    itr = current_index
    while itr >= previous_jump_index:
        if lyst[itr] == target:
            return True
        itr -= 1
    return False

def jump_search(lyst, target):
    """
    Iterates through list by increment of
    floor sqrt(list.size) and if target is not found and
    target < list[current_index] reverse linear searches

    Keyword Arguments:
    lyst -- list we are searching through
    target -- value we are attempting to find
    """
    validate_int_helper(lyst, target)
    itr = 0
    if lyst[itr] == target:
        return True
    jump_index_increment = math.floor(math.sqrt(len(lyst)))
    found = False
    while not found:
        last_index = itr
        itr += jump_index_increment
        if itr >= len(lyst):
            itr = len(lyst) - 1
        curr_val = lyst[itr]
        if curr_val == target:
            return True
        elif target < curr_val:
            return jump_search_helper_reverse_linear_search(
                itr, last_index,
                lyst, target)
        elif itr == len(lyst) - 1 and target > lyst[itr]:
            return False
    return False

#------- END SEARCH FUNCTIONS ------#

#------- BEGIN HELPER FUNCTIONS ------#

def validate_int_helper(lyst, target):
    """
    Validates if target value is integer and
    if list contains valid values. If not throws
    ValueError exception.

    Keyword Arguments:
    lyst -- list we are searching through
    target -- our target value
    """
    try:
        target_check = int(target)
        target <= 0
        for i in lyst:
            target_check = int(i)
    except ValueError:
        raise ValueError("ValueError exception thrown: target not int")

def execute_search_and_time_helper(lyst, target, searchtype):
    """
    Helper function for main to execute each search at
    indexes beginning, middle, and end. Also tests values
    not in list.

    Keyword Arguments:
    lyst -- Pre-sorted list we are searching through
    target -- target we are searching for
    searchtype -- String value of type of search. One of three strings
    """
    search = False
    perf_timer_start = time.perf_counter()
    if searchtype == "linear":
        search = linear_search(lyst, target)
    elif searchtype == "binary":
        search = recursive_binary_search(lyst, target)
    elif searchtype == "jump":
        search = jump_search(lyst, target)
    perf_timer_stop = time.perf_counter()
    if search:
        if searchtype == "linear":
            success_msg = "{:>8}linear_search() returned True in {:.6f} seconds"
            print(success_msg.format("", perf_timer_stop - perf_timer_start))
        elif searchtype == "binary":
            success_msg = "{:>8}recursive_binary_search() returned True in {:.6f} seconds"
            print(success_msg.format("", perf_timer_stop - perf_timer_start))
        else:
            success_msg = "{:>8}jump_search() returned True in {:.6f} seconds"
            print(success_msg.format("", perf_timer_stop - perf_timer_start))
    else:
        if searchtype == "linear":
            failure_msg = "{:>8}linear_search() returned False in {:.6f} seconds"
            print(failure_msg.format("", perf_timer_stop - perf_timer_start))
        elif searchtype == "binary":
            failure_msg = "{:>8}recursive_binary_search() returned False in {:.6f} seconds"
            print(failure_msg.format("", perf_timer_stop - perf_timer_start))
        else:
            failure_msg = "{:>8}jump_search() returned False in {:.6f} seconds"
            print(failure_msg.format("", perf_timer_stop - perf_timer_start))

#------- END MAIN HELPER ------#

#------- BEGIN MAIN OPERATIVE FUNCTION ------#

def main():
    random.seed(25)
    list_size = 100
    print("Creating a sorted array of " + str(list_size))
    lyst = random.sample(range(list_size), k = 25)
    lyst.sort()
    print("Finished creating sorted array of " + str(list_size) + "\n\n")
    test_numbers_from_lyst = [lyst[0], lyst[500000], lyst[list_size - 1], -1, "dog"]
    print("Searching for number at start of the array")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[0],"linear")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[0], "binary")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[0], "jump")
    print("Searching for a numbe rin the middle of an array")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[1], "linear")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[1], "binary")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[1], "jump")
    print("Searching for a number at the end of the array")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[2], "linear")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[2], "binary")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[2], "jump")
    print("Searching for a number NOT in the array")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[3], "linear")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[3], "binary")
    execute_search_and_time_helper(lyst, test_numbers_from_lyst[3], "jump")

#------- END MAIN OPERATIVE FUNCTION -------#

if __name__=="__main__":
    main()
