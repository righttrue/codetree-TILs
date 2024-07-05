arr = list(map(int,input().split()))

arr_over = []
arr_under = []
for i in arr:
    if i > 500:
        arr_over.append(i)
    elif i < 500:
        arr_under.append(i)

print(max(arr_under), min(arr_over))