import heapq

def find_lowest_possible_P(n, m, u, v, s, f, highways):
    adj_list = [[] for _ in range(n+1)]
    for a, b, c in highways:
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))

    dist = [float('inf')] * (n+1)
    min_hotel = [float('inf')] * (n+1)
    dist[u] = 0
    min_hotel[u] = f[u]

    pq = [(0, u)]  # (distance, city)
    while pq:
        cost, city = heapq.heappop(pq)

        if cost > dist[city]:
            continue

        for neighbor, highway_cost in adj_list[city]:
            new_cost = dist[city] + highway_cost
            if new_cost < dist[neighbor] and new_cost <= s:
                dist[neighbor] = new_cost
                min_hotel[neighbor] = min(min_hotel[city], f[neighbor])
                heapq.heappush(pq, (new_cost, neighbor))

    if dist[v] > s:
        return -1

    return max(min_hotel[v], f[u])

# Read input
n, m, u, v, s = map(int, input().split())
f = [int(input()) for _ in range(n)]
highways = [list(map(int, input().split())) for _ in range(m)]

print(highways,f)

# Find the lowest possible value of P
# lowest_P = find_lowest_possible_P(n, m, u, v, s, f, highways)
# print(lowest_P)
