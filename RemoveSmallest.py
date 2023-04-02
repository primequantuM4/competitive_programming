def hasValidPairs(arr):
    if len(arr) == 1:
        return True
    arr.sort()
    pairs = 0

    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] <= 1:
                pairs += 1
                break
    return len(arr) - pairs == 1

test_cases = int(input())

for _ in range(test_cases):
    length = int(input())
    arr = list(map(int, input().split()))

    if hasValidPairs(arr):
        print("YES")
    else:
        print("NO")
