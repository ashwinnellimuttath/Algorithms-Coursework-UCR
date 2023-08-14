from collections import defaultdict

def dfs(city, adjacency_list, reachable):
    visited = set()
    stack = [city]
    while stack:
        current_city = stack.pop()
        if current_city in visited:
            continue
        visited.add(current_city)
        reachable[current_city] += 1
        if len(adjacency_list[current_city]):
            for neighbor in adjacency_list[current_city]:
                if neighbor not in visited:
                    stack.append(neighbor)

n, m = map(int, input().split())

# adjacency_list = defaultdict(list)
adjacency_list = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adjacency_list[a].append(b)

reachable = [0] * (n+2)

for city in range(1, n+1):
    dfs(city, adjacency_list, reachable)

candidate_cities = []
for city in range(1, n+1):
    if reachable[city] == n:
        candidate_cities.append(city)

print(len(candidate_cities))
print(" ".join(map(str, candidate_cities)))
