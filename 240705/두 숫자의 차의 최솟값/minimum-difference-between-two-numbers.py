n = input()
arr = list(map(int,input().split()))


max_profit = 100
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        profit = abs(arr[i] - arr[j])

        if profit <= max_profit :
            max_profit = profit

print(max_profit)