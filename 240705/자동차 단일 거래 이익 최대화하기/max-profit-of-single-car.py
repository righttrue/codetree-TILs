n = input()
arr = list(map(int,input().split()))


max_profit = 0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        profit = arr[j] - arr[i]

        if profit >= max_profit :
            max_profit = profit

print(max_profit)