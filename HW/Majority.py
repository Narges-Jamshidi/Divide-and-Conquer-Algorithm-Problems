


def find_majority(arry, number):
    if len(arry) <= 1:
        if arry[0] == number:
            return 1
        else:
            return 0

    mid = len(arry) // 2
    left_subarry = arry[:mid]
    right_subarry = arry[mid:]

    left_count = find_majority(left_subarry, number)
    right_count = find_majority(right_subarry, number)
    return left_count + right_count

#arry = list(map(int, input().split()))
arry=[]
while True:
    try:
        line = input().strip()
        if not line:
            break
        arry.extend(map(int, line.split()))
    except EOFError:
        break
majority = 0
visited = []
num = 0
for i in arry:
    if i not in visited:
        visited.append(i)
        n = find_majority(arry, i)
        if n > majority:
            majority = n
            num = i

print(num)
