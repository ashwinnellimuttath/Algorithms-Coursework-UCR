import collections
from collections import defaultdict

n, m = map(int, input().split())

adjList = [[] for _ in range(n)]

traitors = set()
for i in range(n-1):
    parent = int(input())
    child = i + 1
    adjList[parent].append(child)

for i in range(m):
    traitor = int(input())
    traitors.add(traitor)
    adjList[traitor] = []

def dfs(node):
    if node in traitors:
        return 0
    size = 1
    for neighbor in adjList[node]:
        size += dfs(neighbor)
    return size

max_size = 0
for i in range(n):
    if adjList[i] :
        size = dfs(i)
        max_size = max(max_size, size)

print(max_size)