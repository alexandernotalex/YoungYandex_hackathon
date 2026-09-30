n, k = map(int, input().split())
nums = [int(i) for i in input().split()]

prefix_sum = 0
ans = 0
freq = {0: 1}

for x in nums:
    prefix_sum += x
    if prefix_sum - k in freq:
        ans += freq[prefix_sum - k]
    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
print(ans)
