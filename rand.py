"""
Module for generating a random array.
"""

import secrets
import random

def random_array(size=None, arr=None, min_val=1, max_val=20, secure=False):
    rand_func = secrets.randbelow if secure else lambda x: random.randint(min_val, x)
    
    if arr is not None:
        for i in range(len(arr)):
            arr[i] = rand_func(max_val) + (1 if secure else 0)
        return arr
    elif size is not None:
        return [rand_func(max_val) + (1 if secure else 0) for _ in range(size)]
    else:
        raise ValueError("Either arr or size must be provided.")
arr = random_array(20, secure=True)  # Uses secure randomness
print(arr)