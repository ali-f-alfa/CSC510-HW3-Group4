"""
Module for merge sort implementation.
"""

import rand

def merge_sort(array):
    """Sorts an array using the merge sort algorithm."""
    if len(array) == 1:  # Removed unnecessary parentheses
        return array

    half = len(array) // 2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))

def recombine(left_array, right_array):
    """Recombines two sorted arrays into a single sorted array."""
    left_index = 0
    right_index = 0
    merge_array = [None] * (len(left_array) + len(right_array))
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merge_array[left_index + right_index] = left_array[left_index]
            left_index += 1
        else:
            merge_array[left_index + right_index] = right_array[right_index]
            right_index += 1

    for i in range(right_index, len(right_array)):
        merge_array[left_index + right_index] = right_array[i]
    
    for i in range(left_index, len(left_array)):
        merge_array[left_index + right_index] = left_array[i]

    return merge_array

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)