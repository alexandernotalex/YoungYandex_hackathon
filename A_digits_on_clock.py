def time(num):
    if num < 10:
        return [0, num]
    return [num // 10, num % 10]

start_time = [int(i) for i in input().split(":")]
end_time = [int(i) for i in input().split(":")]
ans = {key: 0 for key in range(10)}

for i in range(3):
    for j in range(2):
        ans[time(end_time[i])[j]] += 1

while end_time != start_time:
    for i in range(3):
        for j in range(2):
            ans[time(start_time[i])[j]] += 1

    if (start_time[2] == 59):
        start_time[2] = 0
        if (start_time[1] == 59):
            start_time[1] = 0
            if (start_time[0] == 23):
                start_time[0] = 0
            else:
                start_time[0] += 1
        else:
            start_time[1] += 1
    else:
        start_time[2] += 1
        
for i in range(len(ans)):
    if i != 9:
        print(ans[i], end = " ")
    else:
        print(ans[i], end = "")