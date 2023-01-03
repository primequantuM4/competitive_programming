inputs = list(map(int, input().split()))
integers = list(map(int, input().split()))
arrayA = set(map(int, input().split()))
arrayB = set(map(int, input().split()))

result = 0
for i in integers:
    if i in arrayA:
        result += 1
    if i in arrayB:
        result -= 1

print(result)