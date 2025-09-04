def two_sum(numbers, target):
    """two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
    two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)
    """
    
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return (i, j)
