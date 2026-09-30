n, r = map(int, input().split())
d = [int(i) for i in input().split()]
left = 0
right = 1
ans = 0
while (right < n and left < n):
    if d[right] - d[left] > r:
        ans += n - right
        left += 1
    else:
        right += 1
print(ans)
