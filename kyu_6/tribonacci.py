def tribonacci(signature, n):
    if n <= len(signature):
        return signature[0:n]
    for i in range(n):
        if len(signature) == n:
            break
        signature.append(sum(signature[-3:]))
    
    return signature

tribonacci([0.5, 0.5, 0.5], 30)

# [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]