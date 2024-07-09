arr_2d = [
    list(map(int,input().split()))
    for _ in range(2)
]

for i in range(len(arr_2d)):
    print(sum(arr_2d[i])/len(arr_2d[i]), end = " ")
print()


for j in range(len(arr_2d[0])):
    i= 0
    add= 0
    while i < len(arr_2d):
        add +=arr_2d[i][j]
        i+=1
    print(add/len(arr_2d), end = " ")
print()
total_sum = 0
count = 0
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        count+=1
        total_sum += arr_2d[i][j]
print(total_sum/count)