# 8 + 1 = 9 and 92 = 81
# 512 = 5 + 1 + 2 = 8 and 83 = 512

from math import pow

def digit_parsing_sum(d: int) -> tuple[int, int]:
    s = str(d)
    return sum(map(int, s)), len(s)


def pow_sum_dig_term(n: int) -> int:
    if n == 1:
        return 81
    
    res_array: list[int] = [81]
    current_digit: int = 82

    while len(res_array) < n:
        parsed_and_summed, power = digit_parsing_sum(current_digit)
        parsed_and_powered: int = 1

        parsed_and_powered = pow(parsed_and_summed, power)

        if parsed_and_powered == current_digit:
            res_array.append(current_digit)

            if len(res_array) == n:
                return current_digit
        
        current_digit += 1
        # print(current_digit)


pow_sum_dig_term(2)
