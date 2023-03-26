#!/bin/python3
from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    Perform binary search on a sorted list to find the index of a target value.

    Args:
        arr: A sorted list of values to search.
        target: The value to search for.

    Returns:
        The index of the target value if it is found, or -1 if it is not found.
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
