arr_2d = [list(map(int, input().split())) for _ in range(4)]
total = 0

for i in range(len(arr_2d)):
    for j in range((len(arr_2d[i]))):
        if i >= j:
            total += arr_2d[i][j]
print(total)