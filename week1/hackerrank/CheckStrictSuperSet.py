# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(map(int, input().split()))
numberOfOtherSets = int(input())
isSuperStrict = True

for _ in range(numberOfOtherSets):
    checkedSet = set(map(int, input().split()))
    if not setA.issuperset(checkedSet):
        isSuperStrict = False
    

print(isSuperStrict)
