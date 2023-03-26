
from typing import List


def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    The Fibonacci series is a sequence of numbers in which each number is
    the sum of the two preceding ones. The first two numbers in the series
    are 0 and 1. For example, the first ten numbers in the series are:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

    Args:
        n (int): The position of the desired Fibonacci number in the series.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_series(length: int) -> List[int]:
    """
    Return a list containing the first n Fibonacci numbers.

    The Fibonacci series is a sequence of numbers in which each number is
    the sum of the two preceding ones. The first two numbers in the series
    are 0 and 1. For example, the first ten numbers in the series are:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

    Args:
        length (int): The number of Fibonacci numbers to generate.

    Returns:
        List[int]: A list containing the first n Fibonacci numbers.
    """
    series: List[int] = []
    for i in range(length):
        series.append(fibonacci(i))
    return series

