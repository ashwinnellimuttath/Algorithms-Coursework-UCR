n, m = map(int, input().split())

# Initialize an empty adjacency list
# adjList = collections.defaultdict(list)
adjList = [[] for _ in range(n)]

# Parse the parent-child relationships
traitors = []
for i in range(n-1):
    parent = int(input())
    child = i + 1
    adjList[parent].append(child)

# Parse the traitors and remove them from the adjacency list
for i in range(m):
    traitor = int(input())
    traitors.append(traitor)
    adjList[traitor] = []

visited = set()

def dfs(node, count):
    if node in traitors:
        return
    count[node] += 1
    for neighbor in adjList[node]:
        if count[neighbor] == 0:
            dfs(neighbor, count)

# Compute the count of nodes in each connected component
counts = [0] * n
for i in range(n):
    if adjList[i] and i not in traitors and counts[i] == 0:
        dfs(i, counts)

# Find the size of the largest connected component
max_size = max(counts)
print(max_size)


# def dfs(node):
#     visited.add(node)
#     if node in traitors:
#         return 0
#     size = 1
#     for neighbor in adjList[node]:
#         if neighbor not in visited:
#             size += dfs(neighbor)
#     return size

# max_size = 0
# for i in range(n):
#     if adjList[i] and i not in traitors and i not in visited:  # If the node is not a traitor
#         size = dfs(i)
#         max_size = max(max_size, size)

# print(max_size)

