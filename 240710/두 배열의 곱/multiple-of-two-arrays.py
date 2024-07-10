arr_1 = [list(map(int,input().split())) for _ in range(3)]

arr_2 = [list(map(int,input().split())) for _ in range(4)]

arr3 = [[0 for _ in range(3)] for _ in range(3)]


for i in range(3):
    for j in range(3):
        arr3[i][j] = arr_1[i][j] * arr_2[i+1][j]

for row in arr3:
    for ele in row:
        print(ele, end = " ")
    print()