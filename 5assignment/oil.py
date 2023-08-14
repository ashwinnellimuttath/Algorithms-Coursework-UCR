from collections import defaultdict

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def minimum_tank_capacity(n, m, roads):
    adj_list = defaultdict(list)
    for x, y, z in roads:
        adj_list[x].append((y, z))
        adj_list[y].append((x, z))

    parent = [i for i in range(n)]
    rank = [0] * n

    edges = []
    for x in adj_list:
        for y, z in adj_list[x]:
            edges.append((x, y, z))

    edges.sort(key=lambda x: x[2])

    mst_weight = 0
    edge_count = 0
    for x, y, z in edges:
        xroot = find(parent, x)
        yroot = find(parent, y)
        if xroot != yroot:
            mst_weight += z
            edge_count += 1
            union(parent, rank, xroot, yroot)
        if edge_count == n - 1:
            break

    return mst_weight

# Read input values
n, m = map(int, input().split())

roads = []
for _ in range(m):
    x, y, z = map(int, input().split())
    roads.append((x, y, z))

# Calculate and output the minimum tank capacity
min_capacity = minimum_tank_capacity(n, m, roads)
print(min_capacity)
