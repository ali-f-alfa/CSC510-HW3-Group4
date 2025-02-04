import pytest
from hw2_debugging import mergesort


def test_merge_sort_zero():
#Test that mergesort correctly handles list of a zero
    arr = [0]
    expected = [0]
    assert mergesort(arr) == expected

def test_merge_sort_single_element():
#Test that mergesort correctly handles a single-element list
    arr = [42]
    expected = [42]
    assert mergesort(arr) == expected

def test_merge_sort_multiple_elements():
#Test that mergesort correctly sorts a list with multiple elements
    arr = [5, 1, 4, 2, 8]
    expected = [1, 2, 4, 5, 8]
    assert mergesort(arr) == expected
