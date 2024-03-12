"""
2.  # Quick Sort: It uses a partitioning method & is a divide and conquer algorithm
    # A pivot is selected & then the elements are divided into subarrays
    # The animation shows how subarrays are created
3.  # Best case scenario: Partitioning always splits the array exactly into half (log(n))
    # Worst case scenario: Partitioning always splits off only one element of the array (O(n^2))

    Notes
    # Quick sort is quadratic in nature so complexity is very bad

"""

from typing import List


def partition(array: List[int], low: List[int], high: List[int]) -> List[int]:
  
    pivot = array[high]
  
    i = low - 1
  
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
    return i + 1


def quick_sort(array: List[int]) -> List[int]:
    low = 0
    high = len(array) - 1
    
    def q_sort(array: List[int], low: List[int], high: List[int]) -> List[int]:
        if low < high:
  
            pi = partition(array, low, high)
  
            q_sort(array, low, pi - 1)
  
            q_sort(array, pi + 1, high)
    q_sort(array, low, high)


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    quick_sort(array)
    print(array)

