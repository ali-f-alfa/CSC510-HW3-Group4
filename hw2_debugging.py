"""
Module for merge sort implementation.
"""
import random

def merge_sort(array):
    """Sorts an array using the merge sort algorithm."""
    if len(array) <= 1:
        return array
    
    half = len(array) // 2
    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))

def recombine(left_array, right_array):
    """Recombines two sorted arrays into a single sorted array."""
    left_index, right_index = 0, 0
    merge_array = []

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merge_array.append(left_array[left_index])
            left_index += 1
        else:
            merge_array.append(right_array[right_index])
            right_index += 1

    # Append any remaining elements
    merge_array.extend(left_array[left_index:])
    merge_array.extend(right_array[right_index:])

    return merge_array

# Generate a random array of 20 elements
arr = [random.randint(0, 100) for _ in range(20)]
arr_out = merge_sort(arr)

print("Unsorted array:", arr)
print("Sorted array:", arr_out)
