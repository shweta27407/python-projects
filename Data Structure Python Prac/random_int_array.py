from array import *
import random
from typing import List
from typing import List

def create_random(n: int) -> List[int]:
    arr = [random.randint(5, 99) for i in range(n)]
    print(arr)
    return arr

def to_string(a: List[int]) -> str:
    tstr = ''.join(map(str, a))
    print(tstr)
    
def pos_min(a: List[int]) -> int:
    length = len(a)
    min_ind = 0
    min_val = a[0]
    for i in range (1,length):
        if a[i] < min_val: 
            min_val = a[i]
            min_ind = i
    print ("The minimum is at position", min_ind + 1)
    
def swap(a: List[int]) -> None:
    my_list = list(a)
    size_of_list = len(my_list)
    first = my_list [0]
    last = my_list[size_of_list-1]

    my_list[0] = last
    my_list[size_of_list-1] = first
    print ("Swapped array",my_list)


def main(): 
    s=int(input("Enter an int to return random array of same length: "))
    a = create_random(s)
    b = to_string(a)
    c = pos_min(a)
    d = swap(a)

if __name__ == "__main__":
    main()
 

