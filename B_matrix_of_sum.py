n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
ans = []
ans.append((matrix[0][1] + matrix[0][2] + matrix[1][2]) // 2 - matrix[1][2])
for i in range(1, n):
    ans.append(matrix[0][i] - ans[0])
print(*ans)
