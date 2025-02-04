"""
Module for generating a random array.
"""

import random

def random_array(size, min_val=1, max_val=20):
    """Generates a list of random integers within a range."""
    return [random.randint(min_val, max_val) for _ in range(size)]

# Example usage
arr = random_array(20)
print(arr)
