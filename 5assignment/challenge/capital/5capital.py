from collections import defaultdict, deque


def tarjan(v, graph, visited, lowlink, stack, onStack, index, scc):
    visited[v] = index
    lowlink[v] = index
    index += 1
    stack.append(v)
    onStack[v] = True

    for u in graph[v]:
        if visited[u] == -1:
            index = tarjan(u, graph, visited, lowlink, stack, onStack, index, scc)
            lowlink[v] = min(lowlink[v], lowlink[u])
        elif onStack[u]:
            lowlink[v] = min(lowlink[v], visited[u])

    if visited[v] == lowlink[v]:
        current_scc = []
        while True:
            u = stack.pop()
            onStack[u] = False
            current_scc.append(u)
            if u == v:
                break
        scc.append(current_scc)

    return index


def find_candidate_cities(n, m, roads):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)

    visited = [-1] * (n + 1)
    lowlink = [-1] * (n + 1)
    onStack = [False] * (n + 1)
    stack = []
    index = 0
    scc = []

    for v in range(1, n + 1):
        if visited[v] == -1:
            index = tarjan(v, graph, visited, lowlink, stack, onStack, index, scc)

    # Check if the condensation graph is connected
    start_vertex = scc[0][0]
    visited = [False] * (n + 1)
    visited[start_vertex] = True
    queue = deque([start_vertex])

    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

    if not all(visited):
        return 0, []

    # Find candidate cities
    candidate_cities = set()
    for component in scc:
        out_degree = 0
        for vertex in component:
            for neighbor in graph[vertex]:
                if neighbor not in component:
                    out_degree += 1
                    break
        if out_degree == 0:
            candidate_cities.update(component)

    candidate_cities = sorted(candidate_cities)
    return len(candidate_cities), candidate_cities


# Example usage
n = 5
m = 6
roads = [(1, 2), (2, 3), (3, 1), (4, 2), (4, 3), (5, 4)]

num_candidates, candidates = find_candidate_cities(n, m, roads)
print(num_candidates)
print(candidates)
