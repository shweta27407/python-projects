"""
# The list is iterated and the highest value is moved to the end of the list
# Then other values are checked and if higher than the last then that value is moved to last
# The iteration continues like this untill the list is sorted from lowest to highest values
"""


def bubble_sort(array: list) -> None:
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(array)):
            if array[j - 1] > array[j]:
                swap = False
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp 


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    bubble_sort(array)
    assert array == [1, 2, 3, 4, 5]
