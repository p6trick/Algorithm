def matmul(A,B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    print(C)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]

print(f'matmul : {matmul(A,B)}')
