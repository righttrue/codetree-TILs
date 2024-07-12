n  = int(input())
N = n*n 

arr_2d = [[0 for _ in range(n)] for _ in range(n)]
num = 1
count = 0
for j in range(n-1, -1,-1):
    if count%2 == 0:
        count +=1
        for i in range(n-1, -1,-1):
            arr_2d[i][j] = num
            num +=1
    else:
        count +=1
        for i in range(n):
            arr_2d[i][j] = num
            num +=1

for row in arr_2d:
    for elem in row:
        print(elem, end = " ")
    print()