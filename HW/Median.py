import random


def finde_median(arr, pivot, counter):
    if counter > 10:
        return 0
    counter += 1
    if len(arr) % 2 == 0:
        mid = len(arr) // 2
    else:
        mid = (len(arr) + 1) // 2
    temp_arry1 = []
    temp_arry2 = []

    for num in arr:
        if num < pivot:
            temp_arry1.append(num)
        elif num > pivot:
            temp_arry2.append(num)

    if len(temp_arry1) == mid - 1:
        return pivot

    arr.clear()

    for num in temp_arry1:
        arr.append(num)
    arr.append(pivot)
    for num in temp_arry2:
        arr.append(num)

    if len(temp_arry1) > len(temp_arry2):
        pivot = random.choice(temp_arry1)
        temp_arry1.clear()
        return finde_median(arr, pivot, counter)
    else:
        pivot = random.choice(temp_arry2)
        temp_arry2.clear()
        return finde_median(arr, pivot, counter)


arry = list(map(int, input().split()))
print(finde_median(arry, arry[0], 0))
