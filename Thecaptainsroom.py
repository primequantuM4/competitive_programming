from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
number = int(input())
room_numbers = input()
room_numbers = room_numbers.split()
room_occupants = Counter(room_numbers)

for i in room_numbers:
    if room_occupants[i] == 1:
        print(i)
        break
