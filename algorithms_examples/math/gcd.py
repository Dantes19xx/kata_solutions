def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)

def lcm(a, b):

    return a / gcd(a, b) * b

print(gcd(8, 12))
print(gcd(15, 25))
print(gcd(7, 13))
print('----------')
print(gcd(0, 5))
print(gcd(5, 0))
print(gcd(0, 0))