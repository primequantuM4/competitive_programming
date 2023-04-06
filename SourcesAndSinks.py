number_of_nodes = int(input())

adj_mat = []

for row in range(number_of_nodes):
    adj_mat.append(list(map(int, input().split())))

sinks = []

count_references = {}
for node in range(1, number_of_nodes + 1):
    count_references[node] = 0

for row in range(number_of_nodes):
    is_a_sink = True
    for col in range(number_of_nodes):
        if adj_mat[row][col] == 1:
            is_a_sink = False
            if col + 1 in count_references:
                count_references.pop(col + 1)
    
    if is_a_sink:
        sinks.append(row+1)

sources = [i for i in count_references]

print(len(sources), *sorted(sources))
print(len(sinks), *sorted(sinks))
