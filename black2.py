import collections
from collections import defaultdict

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

# print(adjList)

    # def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
    #     if not n:
    #         return True

    #     adjacencyList = {i:[] for i in range(n)}
    #     for n1,n2 in edges:
    #         adjacencyList[n1].append(n2)
    #         adjacencyList[n2].append(n1)
    #     visited = set()

    #     def dfs(node,prev):
    #         if node in visited:
    #             return False
    #         visited.add(node)

    #         for j in adjacencyList[node]:
    #             if j == prev:
    #                 continue
    #             if not dfs(j,node):
    #                 return False

    #         return True


    #     if not dfs(0,-1): return False
    #     return n == len(visited)

def dfs(node):
    if node in traitors:
        return 0
    size = 1
    for neighbor in adjList[node]:
        size += dfs(neighbor)
    return size

# Compute the size of the largest connected component
max_size = 0
for i in range(n):
    if adjList[i] and adjList[i] not in traitors:  # If the node is not a traitor
        size = dfs(i)
        max_size = max(max_size, size)

# Print the result
print(max_size)

# def find_max():
#     def dfs(node):
#         count = 1
#         visited.add(node)
#         for nei in adjList[node]:
#             if nei not in visited:
#                 count += dfs(nei)
#         return count

#     visited = set()
#     maxSize = 0
#     for node in adjList:
#         if node not in visited:
#             familySize = dfs(node)
#             if familySize > maxSize:
#                 maxSize = familySize
#     return maxSize

# print(find_max())

