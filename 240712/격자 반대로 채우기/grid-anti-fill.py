n  = int(input())
N = n*n 

arr_2d = [[0 for _ in range(n)] for _ in range(n)]
num = N
for j in range(n):
    if j%2 == 0:
        for i in range(n-1, -1,-1):
            arr_2d[i][j] = num
            num -=1
    else:
        for i in range(n):
            arr_2d[i][j] = num
            num -=1

for row in arr_2d:
    for elem in row:
        print(elem, end = " ")
    print()