def find_max_sum(arry, length):
    mid = length // 2
    if len(arry) <= 1:
        return arry[0]

    left_subarry = arry[:mid]
    right_subarry = arry[mid:]

    right_max = find_max_sum(left_subarry, len(left_subarry))
    left_max = find_max_sum(right_subarry, len(right_subarry))
    mid_max = find_max_in_middle(arry, length)
    return max(left_max, right_max, mid_max)


def find_max_in_middle(arry, length):
    mid = length // 2
    left_max_sum = -1000000
    right_max_sum = -1000000
    sum = 0
    for i in range(mid, 0, -1):
        sum += arry[i]
        left_max_sum = max(left_max_sum, sum)
    sum = 0
    for i in range(mid + 1, length):
        sum += arry[i]
        right_max_sum = max(right_max_sum, sum)

    return left_max_sum + right_max_sum


length = int(input())

arry = list(map(int, input().split()))
max_sum = find_max_sum(arry, length)
print(max_sum)
