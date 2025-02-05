"""
Module for merge sort implementation.
"""
import random

def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return recombine(left, right)

def recombine(left, right):
    """Merges two sorted arrays into a single sorted array."""
    left_index, right_index = 0, 0
    merged = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Generate a random array of 20 elements
arr = [random.randint(0, 100) for _ in range(20)]
arr_out = merge_sort(arr)

print("Unsorted array:", arr)
print("Sorted array:", arr_out)
