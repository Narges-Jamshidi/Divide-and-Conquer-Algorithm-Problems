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

    P1 = matrix_mult(matrix_sum(A11, A22), matrix_sum(B11, B22))
    P2 = matrix_mult(matrix_sum(A21, A22), B11)
    P3 = matrix_mult(A11, matrix_sub(B12, B22))
    P4 = matrix_mult(A22, matrix_sub(B21, B11))
    P5 = matrix_mult(matrix_sum(A11, A12), B22)
    P6 = matrix_mult(matrix_sub(A21, A11), matrix_sum(B11, B12))
    P7 = matrix_mult(matrix_sub(A12, A22), matrix_sum(B21, B22))

    C11 = matrix_sum(matrix_sub(matrix_sum(P1, P4), P5), P7)
    C12 = matrix_sum(P3, P5)
    C21 = matrix_sum(P2, P4)
    C22 = matrix_sum(matrix_sub(matrix_sum(P1, P3), P2), P6)

    result = combine(C11, C12, C21, C22)
    return result


def combine(C11, C12, C21, C22):
    n = len(C11)
    result = []
    for i in range(n):
        result.append(C11[i] + C12[i])
    for i in range(n):
        result.append(C21[i] + C22[i])
    return result


def matrix_sub(matrix_a, matrix_b):
    n = len(matrix_a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return result


def matrix_sum(matrix_a, matrix_b):
    n = len(matrix_a)
    result = [[0] * n for _ in range(n)]
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
for _ in range(n):
    matrix_A.append(list(map(int, input().split())))
for _ in range(n):
    matrix_B.append(list(map(int, input().split())))

result = matrix_mult(matrix_A, matrix_B)

for row in result:
    print(' '.join(map(str, row)))
