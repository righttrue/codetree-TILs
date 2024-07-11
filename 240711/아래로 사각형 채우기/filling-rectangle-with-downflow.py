N = int(input())
arr_2d =  [[0 for _ in range(N)] for _ in range(N)]
a = 1
for j in range(N):
    for i in range(N):
        arr_2d[i][j] = a
        a+=1

for row in arr_2d:
    for el in row:
        print(el, end = " ")
    print()