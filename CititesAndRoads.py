size = int(input())
value_sum = 0

for row in range(size):
    value_sum += sum(list(map(int, input().split())))

print(value_sum // 2)


