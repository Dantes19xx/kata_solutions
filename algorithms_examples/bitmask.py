
def t():
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)

    for mask in range(1 << n):  # перебираем все битовые маски
        subset = []
        for i in range(n):
            if mask & (1 << i):  # если i-й бит установлен, добавляем элемент
                subset.append(arr[i])
        print("{", ", ".join(map(str, subset)), "}")


t()