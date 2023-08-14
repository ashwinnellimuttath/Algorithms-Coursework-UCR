from collections import deque

def bfs(adj, parent, src, dest):
    visited = [False] * len(adj)
    queue = deque()
    queue.append(src)
    visited[src] = True

    while queue:
        u = queue.popleft()

        for v in adj[u]:
            if not visited[v] and v[1] > 0:
                queue.append(v[0])
                visited[v[0]] = True
                parent[v[0]] = u
                if v[0] == dest:
                    return True

    return False

def find_min_police_vehicles(n, m, A, B, roads):
    adj = [[] for _ in range(n)]

    for u, v, c in roads:
        adj[u - 1].append((v - 1, c))
        adj[v - 1].append((u - 1, c))

    parent = [-1] * n
    totalPoliceVehicles = 0

    while bfs(adj, parent, A - 1, B - 1):
        minCapacity = float('inf')
        v = B - 1

        while v != A - 1:
            u = parent[v]
            minCapacity = min(minCapacity, next(c for (n, c) in adj[u] if n == v))
            v = u

        v = B - 1

        while v != A - 1:
            u = parent[v]
            adj[u][next(i for i, (n, c) in enumerate(adj[u]) if n == v)][1] -= minCapacity
            adj[v][next(i for i, (n, c) in enumerate(adj[v]) if n == u)][1] += minCapacity
            v = u

        totalPoliceVehicles += minCapacity

    return totalPoliceVehicles

n, m, A, B = map(int, input().split())

roads = []
for _ in range(m):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

minPoliceVehicles = find_min_police_vehicles(n, m, A, B, roads)
print(minPoliceVehicles)
