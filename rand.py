"""
Module for generating a random array.
"""

import secrets

def random_array(size=None, arr=None, min_val=1, max_val=20, secure=False):
    """Generates a random array with specified parameters."""
    rand_func = secrets.randbelow if secure else lambda x: secrets.randbelow(x)
    if arr is not None:
        for i, _ in enumerate(arr):
            arr[i] = rand_func(max_val) + (1 if secure else 0)
        return arr
    if size is not None:
        return [rand_func(max_val) + (1 if secure else 0) for _ in range(size)]
    raise ValueError("Either arr or size must be provided.")

random_array_instance = random_array(20, secure=True)  # Uses secure randomness
print(random_array_instance)
