def maximum_product(arry):
    if len(arry) <= 1:
        return arry[0]

    mid = len(arry) // 2
    right_arry = arry[mid:]
    left_arry = arry[:mid]

    right_max = maximum_product(right_arry)
    left_max = maximum_product(left_arry)

    mid_max = maximum_mid(arry)

    return max(right_max, left_max, mid_max)


def maximum_mid(arry):
    mid = len(arry) // 2

    left_min = 100000
    right_min = 100000
    right_max = -100000
    left_max = -100000
    mult = 1
    for i in range(mid, len(arry)):
        mult = mult * arry[i]
        right_min = min(right_min, mult)
        right_max = max(right_max, mult)


    mult = 1
    for i in range(mid-1, -1, -1):
        mult = mult * arry[i]
        left_min = min(left_min, mult)
        left_max = max(left_max, mult)


    return max((right_max * left_max), (left_min * right_min))


arry = list(map(int, input().split()))
print(maximum_product(arry))
