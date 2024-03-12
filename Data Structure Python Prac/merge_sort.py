"""
1.  # Divide and conquer
       # dividing is done when you rearrange the elements into two subarrays
       # Elements of the left subarray should be less than or equal to the elements of the right subarray
       # Conquering is when those subarrays are sorted recursively until those only have a single element
    
    # Stable sorting: 
       # Relative order of the items having the same key is maintainted in stable sorting when the list is sorted
    
2.  # merge_sort = [5, 3, 2, 7, 6, 9, 1, 8, 4, 10] -> divided in array (a, b)
    # This will be divided into 2 smaller arrays (a, b) of 5 elements each
    # Then sorting done in an output array (c) using 3 indices (array a, b, c indices) 
    # Elements will be compared in array (a, b) and smaller will be added to array (c)
    # The pointer will be advanced in arrays (a, b) till all elements are sorted

    Notes
    # we can have a temporary array to overwrite values as merging is done so it will be (2n) which means we need to 2 arrays and this makes merge_sort an out of place algorithm
    # The merge sort we did consume a lot of memory
    # Stable algorithm is when relative order of the items having equal keys remain intact 
    # there is no animation for merge sort as the input array remains the same

"""
from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def merge_sort(array: List[int]) -> List[int]:
    if (len(array) <= 1):
        return array
    mid = int(len(array) / 2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    result = merge_sort(array)
    print(result)
    