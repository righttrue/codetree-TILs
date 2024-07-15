n = int(input())

arr_2d = [[0 for _ in range(n)] for i in range(n)]

for i in range(len(arr_2d)):
    for j in range(len(arr_2d[0])):
        if i >= j :
            arr_2d[i][j] = 1

for i in range(1,len(arr_2d)):
    for j in range(len(arr_2d[0])):
        arr_2d[i][j] = arr_2d[i-1][j-1] + arr_2d[i-1][j]

for i in range(len(arr_2d)):
    for j in range(len(arr_2d[0])):
        if i >= j :
            print(arr_2d[i][j], end = " ")
    print()