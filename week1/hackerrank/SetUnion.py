# Enter your code here. Read input from STDIN. Print output to STDOUT
numOfEnglishStudents = int(input())
englishStudents = set(map(int, input().split()))

numOfFrenchStudents = int(input())
frenchStudents = set(map(int,input().split()))

print(len(englishStudents.union(frenchStudents)))
