n = 5
arr_2d = [
    list(input().split())
    for _ in range(5)
]

for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        print(arr_2d[i][j].upper(),end = " ")
    print()