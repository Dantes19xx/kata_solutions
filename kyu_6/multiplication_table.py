def multiplication_table(size: int) -> list[list[int]]:
    """Creating NxN table, of size provided in parameter.
    
    :size: Table size.
    :return whole_arr: Multiplicated table.
    """

    whole_arr: list[list[int]] = []
    step = 1
    for i in range(size):
        intermediate_arr: list[int] = []
        for j in range(i + 1, (size + 1) * step, step):
            intermediate_arr.append(j)
        
        step += 1
        whole_arr.append(intermediate_arr)
    return whole_arr
