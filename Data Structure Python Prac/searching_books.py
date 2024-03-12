
def search_linear(a: list[str], item: str) -> int:
    x = len(a)
    for i in range(x):
        if a[i] == item:
            return i 
    return None   
    raise NotImplementedError("No array passed")  # TODO: Add implementation
    
    
def search_binary(a: list[str], item: str) -> int:
    #sorting
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
    print("Sorted array is",a)
    
    #binary search
    l = 0
    u = len(a)-1
    
    
    while l <= u:
        
        mid = (l+u)//2
        if a[mid] == item:
            return mid+1
        else:
            if a[mid] < item:
                l = mid
            else:
                u = mid
                
    return None
    raise NotImplementedError("No array passed")  # TODO: Add implementation
    
        
        
def search_linear_cmp_count(a: list[str], item: str) -> int:
    count = 0
    i = 0
    pos = 0
    
    while i < len(a):
        count = count + 1
        if a[i] == item:
            pos = i+1
            return pos
        i = i+1
        
    return count
    raise NotImplementedError("No array passed")  # TODO: Add implementation
    
    
def search_binary_cmp_count(a: list[str], item: str) -> int:

    #sorting
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
    
    #binary search
    l = 0
    u = len(a)-1
    
    count = 0
    while l <= u:
        mid = (l+u)//2
        count = count + 1
        if a[mid] == item:
            return count
        else:
            count = count + 1
            if a[mid] < item:
                l = mid
            else:
                u = mid
                
    return count
    raise NotImplementedError("No array passed")  # TODO: Add implementation
    
                
if __name__ == "__main__":
    pass
