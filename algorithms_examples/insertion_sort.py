def insertion_sort(arr):
    l = len(arr)

    for i in range(l):
        j = i
        cur = arr[i]

        while j > 0 and arr[j - 1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    a = 1


print(insertion_sort([6, 14, -1, 3, 0, 1, 6, 0, 9, 2]))