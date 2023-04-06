from collections import defaultdict

def change_to_adj_list(adj_mat):
    adj_list = defaultdict(list)

    for row in range(len(adj_mat)):
        node = row + 1
        for col in range(len(adj_mat)):
            if adj_mat[row][col] == 1:
                adj_list[node].append(col + 1)

    return adj_list

number_of_nodes = int(input())
adj_mat = []

for _ in range(number_of_nodes):
    adj_mat.append(list(map(int, input().split())))

adj_list = sorted(change_to_adj_list(adj_mat).items())

for _, neighbors in adj_list:
    neighbors.sort()
    print(len(neighbors), *neighbors)
