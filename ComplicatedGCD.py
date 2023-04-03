def confusingGCD(a, b):
    if a == b:
        return a
    
    return 1

first_num, second_num = list(map(int, input().split()))
print(confusingGCD(first_num, second_num))
