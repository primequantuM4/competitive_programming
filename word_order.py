# Enter your code here. Read input from STDIN. Print output to STDOUT
number = int(input())
arr = [input() for i in range(number)]
total_num = []
res = set()
dic = {}
for i in arr:
    if i not in res: 
        total_num.append(1)
        res.add(i)
        dic[i] = len(total_num) - 1
    else:
        idx = dic.get(i)
        total_num[idx] += 1

for i in total_num:
    print(i, end=' ')
