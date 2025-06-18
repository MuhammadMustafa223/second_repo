import time
import random
import matplotlib.pyplot as plt
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Recursively sorts an array using the merge sort algorithm.

    Args:
        arr: A list of integers to be sorted.

    Returns:
        A new sorted list of integers.
    """
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    return merge(left_half, right_half)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left: Sorted left half.
        right: Sorted right half.

    Returns:
        A merged and sorted list containing all elements from left and right.
    """
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index_]()

