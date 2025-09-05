def remove_smallest(numbers: list[int]):
    """
    Нужно убрать первый попавшийся минимальный элемент,
    не менять порядок и не менять исходный массив
    * Input: [1,2,3,4,5], output = [2,3,4,5]
    * Input: [5,3,2,1,4], output = [5,3,2,4]
    * Input: [2,2,1,2,1], output = [2,2,2,1]"""
    
    if not numbers:
        return []
    
    min_val: int = min(numbers)
    min_idx = numbers.index(min_val)
    res_arr = list(numbers)

    res_arr.pop(min_idx)

    return res_arr
