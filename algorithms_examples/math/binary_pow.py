def bin_pow(self, a, x):
    if x == 0:
        return 1
    
    if x < 0:
        return 1 / self.bin_pow(a, -x)
    
    if x % 2 == 1:
        return self.bin_pow(a, x-1) * a
    
    b = self.bin_pow(a, x//2)

    return b * b


print(bin_pow(2, 100))
