'''
This file contains Python implementation of the Binary Search algorithm
we will call the lower bound and upper bound l and r to resemble left-right
ptr syntax
'''


def binary_search(array, target):
    l, r = 0, len(array) - 1  # zero-based arrays
    while l <= r:  # = important to catch hedge cases
        print("Left: ", l)
        print("Right: ", r)

        mid = int((l + r) / 2)  # mid
        print("Mid: ", mid)

        if array[mid] == target:  # solution
            return mid  # return the right index
        elif array[mid] > target:
            print("Moving right ptr to mid - 1")
            r = mid - 1
        else:
            print("Moving right ptr to mid - 1")
            l = mid + 1
    return -1  # cannot find the number