def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    a = 1


print(bubble_sort([7, 4, 8, 1, 0, 3]))