from typing import List
def interleave(a: List[int], b: List[int]) -> List[int]:
    result = []
    a1 = len(a)
    b1 = len(b)
    
    for i in range(max(a1, b1)):
        if i < a1:
            result.append(a[i])
        if i < b1:
            result.append(b[i])
    return result
n = int(input("Enter number of elements for array 1 : "))
m = int(input("Enter number of elements for array 2 : "))
a = list(map(int,input("\nEnter the numbers for array 1 : ").strip().split()))[:n]
b = list(map(int,input("\nEnter the numbers for array 2: ").strip().split()))[:m]
print("\nInterleave said lists of same lengths:")
print(interleave(a, b))

from itertools import chain
def perfect_shuffle(a: List[int]) -> List[int]:
    a = (interleave(a, b))
    half = len(a) // 2
    return list(chain.from_iterable(zip(a[:half], a[half:])))
print(perfect_shuffle(a))



