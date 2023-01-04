# Enter your code here. Read input from STDIN. Print output to STDOUT
englishStudentsNumber = int(input())
englishSet = set(map(int, input().split()))

frenchStudentsNumber = int(input())
frenchSet = set(map(int, input().split()))

print(len(englishSet.difference(frenchSet)))
