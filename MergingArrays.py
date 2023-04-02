size1, size2 = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ptr_arr1 = 0
ptr_arr2 = 0

resulting_array = []

while ptr_arr1 < len(arr1) and ptr_arr2 < len(arr2):
    if arr1[ptr_arr1] < arr2[ptr_arr2]:
        resulting_array.append(arr1[ptr_arr1])
        ptr_arr1 += 1
    else:
        resulting_array.append(arr2[ptr_arr2])
        ptr_arr2 += 1
    
resulting_array.extend(arr2[ptr_arr2:])
resulting_array.extend(arr1[ptr_arr1:])

print(*resulting_array)
