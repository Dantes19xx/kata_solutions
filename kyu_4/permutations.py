def permute(arr):
    if len(arr) == 0:
        return [""]   
    result = []
    for i in range(len(arr)):

        char = arr[i]

        rest = arr[:i] + arr[i+1:]

        for perm in permute(rest):
            result.append(char + perm)
    return result

def permutations(s):
    return sorted(set(permute(list(s))))





permutations("abc")

['abc', 'acb', 'bac', 'bca', 'cab', 'cba']