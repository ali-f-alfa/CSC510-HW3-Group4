"""
Module for generating a random array.
"""

import subprocess

def random_array(arr):
    """Generates a random array using the 'shuf' command."""
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
