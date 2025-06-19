
def find_unique_element(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if len(arr) % 2 == 0:
        raise ValueError("Array length must be odd.")
    
    result = 0
    for num in arr:
        if not isinstance(num, int):
            raise ValueError("All elements must be integers.")
        result ^= num
    return result
