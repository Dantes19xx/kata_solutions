def counting_sort(arr):
    if not arr:
        return arr

    # Находим минимальный и максимальный элементы
    min_val = min(arr)
    max_val = max(arr)

    # Создаём массив счётчиков
    count = [0] * (max_val - min_val + 1)

    # Подсчитываем количество вхождений каждого элемента
    for num in arr:
        count[num - min_val] += 1

    # Восстанавливаем отсортированный массив
    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i + min_val] * c)

    return sorted_arr


print(counting_sort([3, 9, 3, 5, 5, 4]))