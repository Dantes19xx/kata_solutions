def next_smaller(n):
    digits = list(str(n))

    # Ищем pivot: первую цифру справа,
    # которая больше цифры после неё.
    pivot = len(digits) - 2

    while pivot >= 0 and digits[pivot] <= digits[pivot + 1]:
        pivot -= 1

    if pivot < 0:
        return -1

    # Ищем справа первую цифру, меньшую pivot.
    swap_idx = len(digits) - 1

    while digits[swap_idx] >= digits[pivot]:
        swap_idx -= 1

    # Меняем цифры местами.
    digits[pivot], digits[swap_idx] = digits[swap_idx], digits[pivot]

    # Делаем хвост максимально большим.
    digits[pivot + 1:] = sorted(digits[pivot + 1:], reverse=True)

    # Нельзя получить число с ведущим нулём.
    if digits[0] == "0":
        return -1

    return int("".join(digits))