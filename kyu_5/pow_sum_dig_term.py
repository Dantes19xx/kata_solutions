def pow_sum_dig_term(n: int) -> int:
    current = 81
    found = 0

    while True:
        digits = str(current)

        if sum(map(int, digits)) ** len(digits) == current:
            found += 1

            if found == n:
                return current

        current += 1