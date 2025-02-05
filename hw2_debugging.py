"""
Module for sorting algorithms.
"""

import random
import os
import secrets

def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    return recombine(left, right)

def recombine(left_arr, right_arr):
    """Recombines two sorted arrays into a single sorted array."""
    left_index, right_index = 0, 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])
    return merge_arr

def bubble_sort(arr):
    """Sorts an array using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def authenticate_user():
    """Simple authentication function."""
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")

    if user_input and pass_input:
        print("Access Granted!")
    else:
        print("Access Denied!")
def delete_file():
    """Deletes a file if it exists."""
    filename = input("Enter filename to delete: ")
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"File {filename} deleted successfully.")
        except OSError as e:
            print(f"Error deleting file: {e}")
    else:
        print("File not found.")
def divide_numbers():
    """Performs division with user input."""
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        print(a / b)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numbers.")
def main():
    """Main function to execute the script."""
    authenticate_user()
    delete_file()
    divide_numbers()

    # Generate a random array of 20 elements for sorting
    arr = [secrets.randbelow(0, 100) for _ in range(20)]
    print("Unsorted array:", arr)
    print("Sorted with merge sort:", merge_sort(arr))
    print("Sorted with bubble sort:", bubble_sort(arr))

if __name__ == '__main__':
    main()
