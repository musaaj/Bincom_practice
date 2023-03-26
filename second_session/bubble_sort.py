#!/bin/python3
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the bubble sort algorithm.

    Args:
        arr: A list of integers to be sorted.

    Returns:
        A new list of integers containing the sorted elements.
    """
    n: int = len(arr)
    sorted_arr: List[int] = arr.copy()

    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]

    return sorted_arr
