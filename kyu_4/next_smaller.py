def next_smaller(n):
    n = list(str(n))
    pivot_idx = -1

    for i in range(len(n)-2, -1, -1):
        if int(n[i]) > int(n[i+1]):
            pivot_idx = i
            break

    if pivot_idx == -1:
        return -1

    max_smaller_idx = -1
    for j in range(len(n)-1, pivot_idx, -1):
        if int(n[j]) < int(n[pivot_idx]):
            if max_smaller_idx == -1 or int(n[j]) > int(n[max_smaller_idx]):
                max_smaller_idx = j

    n[pivot_idx], n[max_smaller_idx] = n[max_smaller_idx], n[pivot_idx]

    right_side = sorted(n[pivot_idx+1:], reverse=True)
    left_side = n[:pivot_idx+1]

    if left_side[0] == "0":
        return -1

    res = int("".join(left_side + right_side))
    return res