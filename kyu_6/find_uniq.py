def find_uniq(arr: list[int | float]) -> int | float:
    """Function getting a uniq element if list.
    
    :arr: Raw list.
    :return: Unique element in the list.
    """

    first_val: int | float = arr[0]

    slice_arr_1: list[int | float] = [i for i in arr if i == first_val]
    slice_arr_2: list[int | float] = [i for i in arr if i != first_val]

    return slice_arr_1[0] if len(slice_arr_1) == 1 else slice_arr_2[0]
