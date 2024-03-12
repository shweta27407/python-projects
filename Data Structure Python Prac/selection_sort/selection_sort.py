"""
1.  #  In-Place sorting algorithms: it doesn't require additional memory to transform the input
    #  Out-of-Place sorting algorithms: It requires extra memory depending on the size of the input
    #  Complexity of in-place sorting algorithm: O(log(n))
    #  Complexity of out-of-place sorting algorithms: O(n) 

2.  # In Selection sort, the entire list is iterated for the smallest element
    # Which is brought to the beginning of the list
    # The iteration keeps on going till the list is sorted from lowest to the highest values
"""


def selection_sort(array: list) -> None:
    suffix_counter = 0
    while suffix_counter != len(array):
        for i in range(suffix_counter, len(array)):
            if array[i] < array[suffix_counter]:
                array[suffix_counter], array[i] = array[i], array[suffix_counter]
        suffix_counter += 1


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    selection_sort(array)
    assert array == [1, 2, 3, 4, 5]

