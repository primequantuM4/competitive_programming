from collections import defaultdict

graph = defaultdict(list)
def addEdge(node_a, node_b):

    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

def printNeighbors(node):
    return graph[node]

number_of_nodes = int(input())
number_of_instructions = int(input())

for _ in range(number_of_instructions):
    instructions = list(map(int, input().split()))
    printInstructions = instructions[0] - 1

    if printInstructions:
        node = instructions[1]
        print(*printNeighbors(node))

    else:
        node_a, node_b = instructions[1], instructions[2]
        addEdge(node_a, node_b)
