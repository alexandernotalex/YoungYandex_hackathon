n, m = map(int, input().split())
w_x = 0
w_y = 0
emp = []
for i in range(n):
    str = input()
    w = str.find('W')
    if w != -1:
        w_x = i
        w_y = w
    for j in range(len(str)):
        if str[j] == 'E':
            emp.append([i, j])
ans = 0
for i in range(len(emp)):
    ans += abs(emp[i][0] - w_x) + abs(emp[i][1] - w_y)
print(ans)