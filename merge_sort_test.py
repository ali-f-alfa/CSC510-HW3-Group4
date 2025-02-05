import pytest
from hw2_debugging import mergeSort

def test_sorted_array():
    """Test mergeSort with an already sorted array."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert mergeSort(arr) == sorted(arr)

def test_reverse_sorted_array():
    """Test mergeSort with a reverse-sorted array."""
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert mergeSort(arr) == sorted(arr)

def test_random_unsorted_array():
    """Test mergeSort with a randomly unsorted array."""
    arr = [5, 1, 9, 3, 7, 6, 2, 8, 4, 0]
    assert mergeSort(arr) == sorted(arr)
