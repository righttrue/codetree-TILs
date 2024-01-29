N = int(input())

arr = list(map(int, input().split()))

arr2 = []
ans = 0
for i in range(len(arr)):
    if arr[i] in arr[i+1:]:
        arr2.append(arr[i])
max_num = arr[0]
for i in arr:
    if i in arr2:
        continue
    if max_num <= i:
        max_num = i
        ans = 0
if len(set(arr)) == len(set(arr2)):    print(ans)
else:
    print(max_num)
print(arr2)