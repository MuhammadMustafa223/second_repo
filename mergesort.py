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

