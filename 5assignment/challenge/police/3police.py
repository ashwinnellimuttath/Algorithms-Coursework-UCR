from collections import deque

def bfs(adj, parent, src, dest):
    visited = [False] * len(adj)
    queue = deque()
    queue.append(src)
    visited[src] = True

    while queue:
        u = queue.popleft()
        for v, capacity in adj[u]:
            if not visited[v] and capacity > 0:
                visited[v] = True
                parent[v] = u
                queue.append(v)
                if v == dest:
                    return True

        # for v in range(len(adj)):
        #     if not visited[v] and adj[u][v] > 0:
        #         queue.append(v)
        #         visited[v] = True
        #         parent[v] = u
        #         if v == dest:
        #             return True

    return False

def find_min_police_vehicles(n, m, A, B, roads):
    # adj = [[0] * n for _ in range(n)]
    adj = [[] for _ in range(n)]

    for u,v,c in roads:
        adj[u-1].append((v-1,c))
        adj[v-1].append((u-1,c))
    # for u, v, c in roads:
    #     adj[u - 1][v - 1] = c
    #     adj[v - 1][u - 1] = c

    parent = [-1] * n
    totalPoliceVehicles = 0

    while bfs(adj, parent, A - 1, B - 1):
        # print(parent)
        minCapacity = float('inf')
        v = B - 1
        while v != A - 1:
            u = parent[v]

            for neigh, cap in adj[u]:
                if neigh == v:
                    # print("here",v)
                    minCapacity = min(minCapacity,cap)
                    # v = u
                    break
            v = u

        # while v != A - 1:
        #     u = parent[v]
        #     minCapacity = min(minCapacity, adj[u][v])
        #     v = u



        # v = B
        v = B - 1

        while v != A - 1:
            # print("wek")
            for i,(neigh, cap) in enumerate (adj[parent[v]]):
                if neigh == v:
                    adj[parent[v]][i] = neigh,cap - minCapacity
                    break
            for i,(neigh,cap) in enumerate(adj[v]):
                if neigh == parent[v]:
                    adj[v][i] = neigh, cap + minCapacity
                    break
            v = parent[v]
            # u = parent[v]
            # adj[u][v] -= minCapacity
            # adj[v][u] += minCapacity
            # v = u

        totalPoliceVehicles += minCapacity

    return totalPoliceVehicles

n, m, A, B = map(int, input().split())

roads = []
for _ in range(m):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))
minPoliceVehicles = find_min_police_vehicles(n, m, A, B, roads)
print(minPoliceVehicles)
