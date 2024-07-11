n, m = map(int,input().split())

arr_2d = [[0 for _ in range(m)] for _ in range(n)]

diag = 0
num = 1 
while diag <= n + m +1:
    for i in range(n):
        for j in range(m):
            if i + j == diag :
                arr_2d[i][j] += num 
                num +=1
            else:
                continue
    diag +=1
for row in arr_2d:
    for elem in row:
        print(elem, end = " ")
    print()