def getNumberGreater(k, arr):
    arr.sort()
    arr.append(float('inf'))
    
    if k == 0:
        return 1 if arr[0] > 1 else -1
      
    potential_x = k - 1

    if arr[potential_x + 1] == arr[potential_x]:
        return -1
    else:
        return arr[potential_x]

arr_length, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
x = getNumberGreater(k, arr)

print(x)

