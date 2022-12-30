# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

inputs = input()
inputs = inputs.split()
groupA = []
groupB = []

for i in range(int(inputs[0])):
    groupA.append(input())

for i in range(int(inputs[1])):
    groupB.append(input())
    
occurences = defaultdict(list)


for i in range(len(groupA)):
    occurences[groupA[i]].append(str(i + 1))
for i in groupB:
    if occurences[i]:
        print(" ".join(occurences[i]))
    else:
        print("-1")
