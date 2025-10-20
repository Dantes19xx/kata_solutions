def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # результирующий массив
    count = [0] * 10  # цифры от 0 до 9

    # Подсчёт количества цифр в текущем разряде
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Преобразуем count в накопительный массив
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Формируем выходной массив (с конца для стабильности)
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Копируем результат в исходный массив
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Находим максимальное число, чтобы узнать количество разрядов
    max_num = max(arr)

    # Проходим по всем разрядам (1, 10, 100, 1000, ...)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Пример использования
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Отсортированный массив:", arr)
