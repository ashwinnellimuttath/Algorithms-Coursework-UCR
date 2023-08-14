from collections import defaultdict
import heapq

n, m = map(int, input().split())

adj_list = {i: [] for i in range( n+1)}

for _ in range(m):
    x, y, z = map(int, input().split())
    adj_list[x].append((z, y))
    adj_list[y].append((z, x))


def minimum_tank_capacity(n, adj_list):
    # adj_list = defaultdict(list)
    # for x, y, z in roads:
    #     adj_list[x].append((z, y))
    #     adj_list[y].append((z, x))
    # print(adj_list[0])

    minHeap = [(0,0)]
    visited = set()
    res = 0
    while len(visited) < n:
        dist,node = heapq.heappop(minHeap)
        if node in visited:
            continue
        visited.add(node)
        res = max(res,dist)
        for distNei,nodeNei in adj_list[node]:
            if nodeNei not in visited:
                heapq.heappush(minHeap,[distNei,nodeNei])


    return res

min_capacity = minimum_tank_capacity(n,adj_list)
print(min_capacity)