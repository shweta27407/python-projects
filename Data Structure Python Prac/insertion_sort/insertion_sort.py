"""
# In insertion sort, it is done in pairs.
# The 2nd value from the list is checked and if its greater than the left value then no change happens
# If its less than the left then the position is moved till condition is not met
# The iteration continues like this till the list is sorted from lowest to highest values
"""


def insertion_sort(array: list) -> None:
    for i in range(1, len(array)):
        k = array[i]
        j = i - 1
        while j >= 0 and k < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = k


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    insertion_sort(array)
    assert array == [1, 2, 3, 4, 5]
