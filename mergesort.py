<<<<<<<<< Temporary merge branch 1
import time
import random
import matplotlib.pyplot as plt
from typing import List


def merge_sort(arr: List[int]) -> None:
    """Sorts the array in-place using Merge Sort algorithm."""
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(arr, left, right)


def merge(arr: List[int], left: List[int], right: List[int]) -> None:
    """Merges two sorted sublists into arr."""
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def measure_execution_time(n: int) -> float:
    """Returns execution time to sort a list of size n."""
    test_list = [random.randint(0, 10000) for _ in range(n)]
    start = time.time()
    merge_sort(test_list)
    end = time.time()
    return end - start


def plot_merge_sort_performance():
    """Plots Merge Sort execution time vs input size."""
    sizes = [100, 500, 1000, 2000, 4000, 8000, 16000]
    times = [measure_execution_time(size) for size in sizes]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='blue')
    plt.title("Merge Sort Performance")
    plt.xlabel("Input Size (Number of Elements)")
    plt.ylabel("Execution Time (Seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_merge_sort_performance()

=========
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
    merged.extend(right[right_index:])
    
    return merged

# Example usage (for testing purposes)
if __name__ == "__main__":
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(sample_list)
    print(f"Sorted list: {sorted_list}")
>>>>>>>>> Temporary merge branch 2
