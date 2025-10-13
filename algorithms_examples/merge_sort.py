def merge_sort(arr):
    # Базовый случай: массив длиной 0 или 1 уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем массив пополам
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Сливаем отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # Сравниваем элементы и добавляем в результат
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы (если есть)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
