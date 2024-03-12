# exercise done in group with Osama Kamal
from typing import List
from random import randint
import time


def binary_search(a: List[int], item: int) -> int | None:
    """Searches the list for item with binary search. Returns the position of item."""
    low = 0
    high = len(a) - 1
    while low <= high:

        mid = low + (high - low) // 2

        if a[mid] == item:
            return mid

        elif a[mid] < item:
            low = mid + 1

        else:
            high = mid - 1

    return None


def ternary_search(a: List[int], item: int) -> int | None:
    low = 0
    high = len(a) - 1
    while low <= high:

        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if a[mid1] == item:
            return mid1
        
        if a[mid2] == item:
            return mid2

        elif a[mid1] > item:
            high = mid1 - 1
        
        elif a[mid2] < item:
            low = mid2 + 1

        else:
            low = mid1 + 1
            high = mid2 - 1

    return None


def time_binary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    binary_search(arr, item)
    return time.time() - start


def time_ternary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    ternary_search(arr, item)
    return time.time() - start


if __name__ == "__main__":
    # TODO: Test your binary and ternary search implementation here...

    # These constants should be defined here, don't move them!
    MAX_VALUE = 50_000_000
    NUM_ITER = 100_000
    SEARCH_VALUES = [randint(0, MAX_VALUE - 1) for _ in range(NUM_ITER)]
    ARRAY = list(range(MAX_VALUE))
    print(f"Searching {NUM_ITER:_} random values in an array of size {MAX_VALUE:_}")

    time_binary = 0.
    for value in SEARCH_VALUES:
        time_binary += time_binary_search_in_s(ARRAY, value)

    time_ternary = 0.
    for value in SEARCH_VALUES:
        time_ternary += time_ternary_search_in_s(ARRAY, value)

    print(f"Total binary search time:    {time_binary:.9f} s")
    print(f"Total ternary search time:   {time_ternary:.9f} s")
    print(f"Average binary search time:  {time_binary / NUM_ITER:.9f} s")
    print(f"Average ternary search time: {time_ternary / NUM_ITER:.9f} s")

"""
TODO: Task 3, compare the algorithms.
"""
