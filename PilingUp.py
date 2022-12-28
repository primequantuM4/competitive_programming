# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
def checkIfPilable(arr):
    #start with a none pile element and we just pop towards the prev pile
    prev_pile = None
    #check if the left most or the right most is greater and then check if that is greater than the prev_pile if it is return no. Until we have no element left to pop
    while arr:
        if arr[-1] > arr[0]:
            prev_pile = arr.pop()
        else:
            prev_pile = arr.popleft()
        if len(arr) == 0:
            return "Yes"
        if arr[-1] > prev_pile  or arr[0] > prev_pile:
            return "No"
        

for i in range(int(input())):
    number_of_blocks = int(input())
    blocks = deque(map(int, input().split()))
    print(checkIfPilable(blocks))
