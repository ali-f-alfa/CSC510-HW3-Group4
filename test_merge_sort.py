from hw2_debugging import merge_sort  # Replace 'your_module' with the actual filename

def test_random_list():
    """Test merge_sort with an unsorted random list."""
    input_list = [12, 5, 3, 19, 8, 7, 1, 14]
    expected_output = sorted(input_list)
    assert merge_sort(input_list) == expected_output

def test_sorted_list():
    """Test merge_sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_output = input_list  # Should remain the same
    assert merge_sort(input_list) == expected_output

def test_list_with_duplicates():
    """Test merge_sort with a list containing duplicate values."""
    input_list = [4, 2, 7, 3, 4, 1, 2, 7]
    expected_output = sorted(input_list)
    assert merge_sort(input_list) == expected_output