def bin_pow(a, n):
    if n == 0:
        return 1
    
    if n % 2 == 1:
        return bin_pow(a, n - 1) * a

    b = bin_pow(a, n // 2)

    return b * b


print(bin_pow(2, 100))
