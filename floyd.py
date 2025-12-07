def floyd_warshall(mat):
    n = len(mat)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][k] + mat[k][j] < mat[i][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]
    return mat


INF = 10**9
matrix = [
    [0,   3,   INF],
    [INF, 0,   1  ],
    [INF, INF, 0  ]
]



result = floyd_warshall(matrix)
print("Floyd-Warshall result:")
for row in result:
    print(row)
