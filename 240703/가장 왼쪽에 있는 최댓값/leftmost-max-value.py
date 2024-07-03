N = int(input())
arr = list(map(int,input().split(" ")))

while True:
    max = -999
    idx = 0
    max_idx = 0
    for i in arr:
        if i > max:
            max = i
            max_idx  = idx
            idx+=1
            
        elif i == max:
            max = i
            idx+=1
        else:
            idx+=1
    if len(set(arr)) == 0:
        break
    else:
        print(max_idx+1, end= " ")
    
    arr2 = [] 
    for j in arr[0:max_idx]:
        if j ==max:
            j  = -999
            arr2.append(j)
        else:
            arr2.append(j)

    arr = arr2