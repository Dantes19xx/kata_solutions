def bin_search(arr):
    l = 0
    r = len(arr) - 1
    target = 9
    
    while l <= r:
        m = l + ((r - l) // 2)
        if arr[m] < target:
            l =  m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m
    
    return None
        

print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 13]))
