"""
Module for generating a random array.
"""

import random

def random_array(size=None, arr=None, min_val=1, max_val=20):
    if arr is not None:
        for i in range(len(arr)):
            arr[i] = random.randint(min_val, max_val)
        return arr
    elif size is not None:
        return [random.randint(min_val, max_val) for _ in range(size)]
        """Generates a list of random integers within a range."""
    else:
        raise ValueError("Either arr or size must be provided.")

# Example usage
arr = random_array(20)
print(arr)
