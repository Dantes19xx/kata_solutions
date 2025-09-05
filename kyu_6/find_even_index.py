def find_even_index(arr):
    """У тебя есть массив чисел. Нужно найти такой индекс N, чтобы:
    сумма всех элементов слева от N была равна
    сумме всех элементов справа от N.
    При этом сам элемент на позиции N в расчёты не включается.

    Примеры:

    {1,2,3,4,3,2,1} → индекс 3, потому что 1+2+3 = 3+2+1 = 6.
    {1,100,50,-51,1,1} → индекс 1, потому что 1 = 50-51+1+1.
    {20,10,-80,10,10,15,35} → индекс 0, потому что слева пусто (0), а справа сумма тоже 0.
    """

    n = len(arr)
    left_side_sum = []
    right_side_sum = []

    for i in range(n):
        if i == 0:
            left_side_sum = 0
        else:
            left_side_sum = sum([arr[x] for x in range(i)])
        
        if i == n - 1:
            right_side_sum = 0
        else:    
            right_side_sum = sum([arr[x] for x in range(i + 1, n)])

        if left_side_sum == right_side_sum:
            return i
    
    return -1
        