from collections import defaultdict

def dfs(city, visited, adjacency_list, reachable):
    if city in visited:
        return
    visited.add(city)
    # visited[city] = True
    reachable[city] += 1
    # print(adjacency_list,city,len(adjacency_list[city]))
    if len(adjacency_list[city]):
        for neighbor in adjacency_list[city]:
            # print(neighbor)
            if neighbor and neighbor not in visited:
                dfs(neighbor, visited, adjacency_list, reachable)

n, m = map(int, input().split())

adjacency_list = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    adjacency_list[a].append(b)

# print(adjacency_list[2],"adj")
# print(adjacency_list,"adj")

reachable = [0] * (n+2)

for city in range(1, n+1):
    visited = set()
    # visited = [False] * (n+1)
    dfs(city, visited, adjacency_list, reachable)

candidate_cities = []
for city in range(1, n+1):
    if reachable[city] == n:
        candidate_cities.append(city)

print(len(candidate_cities) or 1)
print(" ".join(map(str, candidate_cities)))
