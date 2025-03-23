def matrix_mult(matrix_a, matrix_b):
    if len(matrix_a) <= 2:
        return matrix_calc(matrix_a, matrix_b)

    return strassten(matrix_a, matrix_b)


def matrix_calc(matrix_a, matrix_b):
    n = len(matrix_a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


def strassten(matrix_a, matrix_b):
    A11, A12, A21, A22 = split(matrix_a)
    B11, B12, B21, B22 = split(matrix_b)
    S1 = matrix_sub(B12, B22)
    S2 = matrix_sum(A11, A12)
    S3 = matrix_sum(A21, A22)
    S4 = matrix_sub(B21, B11)
    S5 = matrix_sum(A11, A22)
    S6 = matrix_sum(B11, B22)
    S7 = matrix_sub(A12, A22)
    S8 = matrix_sum(B21, B22)
    S9 = matrix_sub(A11, A12)
    S10 = matrix_sum(B11, B12)

    P1 = matrix_mult(A11, S1)
    P2 = matrix_mult(S2, B22)
    P3 = matrix_mult(S3, B11)
    P4 = matrix_mult(A22, S4)
    P5 = matrix_mult(S5, S6)
    P6 = matrix_mult(S7, S8)
    P7 = matrix_mult(S9, S10)

    C11 = matrix_sum(matrix_sum(P5, P4), matrix_sub(P6, P2))
    C12 = matrix_sum(P1, P2)
    C21 = matrix_sum(P3, P4)
    C22 = matrix_sum(matrix_sum(P5, P6), matrix_sub(P7, P3))
    result = combine(C11, C12, C21, C22)
    return result


def combine(A11, A12, A21, A22):
    n = len(A11)
    top = []
    bottom = []
    for i in range(n):
        top.append(A11[i] + A12[i])

    for i in range(n):
        bottom.append(A21[i] + A22[i])

    return top + bottom


def matrix_sub(matrix_a, matrix_b):
    n = len(matrix_a)
    result = [[0] * n for _ in range(n)]  # ماتزیس نتیجه که مقدار اولیه همه درایه های آن 0 است
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return result


def matrix_sum(matrix_a, matrix_b):
    n = len(matrix_a)
    result = [[0] * n for _ in range(n)]  # ماتریس نتیجه که مقدار اولیه همه درایه های آن 0 است
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result


def split(matrix):
    n = len(matrix) // 2
    A11 = [row[:n] for row in matrix[:n]]
    A12 = [row[n:] for row in matrix[:n]]
    A21 = [row[:n] for row in matrix[n:]]
    A22 = [row[n:] for row in matrix[n:]]
    return A11, A12, A21, A22


n = int(input())

matrix_A = []
matrix_B = []
for i in range(n):
    matrix_A.append(list(map(int, input().split())))
for i in range(n):
    matrix_B.append(list(map(int, input().split())))

result = matrix_mult(matrix_A, matrix_B)

for row in result:
    for elem in row:
        print(elem, end=' ')
    print()
