def maximum_product(arry):
    if len(arry) <= 1:
        return arry[0]

    mid = len(arry) // 2
    right_arry = arry[mid:]
    left_arry = arry[:mid]

    right_max = maximum_product(right_arry)
    left_max = maximum_product(left_arry)

    return max(right_max, left_max)


def maximum_mid(arry):
    mid = len(arry) // 2


arry = list(map(int, input().split()))
