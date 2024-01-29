N = 4

arr = [3,2,3,1]
arr2 = []
arr3 = []
ans = -1
for i in range(len(arr)):
    if arr[i] in arr[i+1:]:
        arr2.append(arr[i])
max_num = arr[0]
for i in arr:
    if i in arr2:
        continue
    else:
        arr3.append(i)


if len(set(arr)) == len(set(arr2)):   
    print(ans)
else:
    print(max(arr3))