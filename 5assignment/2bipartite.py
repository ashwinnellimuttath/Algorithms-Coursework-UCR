import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def construct_graph(students, shelters, b):
    graph = []
    for student in students:
        row = []
        for shelter in shelters:
            distance = calculate_distance(student[0], student[1], shelter[0], shelter[1])
            time = distance / student[2]
            if time <= b:
                row.append(time)
            else:
                row.append(float('inf'))
        graph.append(row)
    return graph

def dfs(graph, u, match, seen):
    for v in range(len(graph[0])):
        if graph[u][v] and not seen[v]:
            seen[v] = True
            if match[v] == -1 or dfs(graph, match[v], match, seen):
                match[v] = u
                return True
    return False

def maximum_matching(graph):
    n = len(graph)
    m = len(graph[0])
    match = [-1] * m
    count = 0
    for u in range(n):
        seen = [False] * m
        if dfs(graph, u, match, seen):
            count += 1
    return count

# Read input
n, m, b = map(int, input().split())

students = []
for _ in range(n):
    x, y, r = map(int, input().split())
    students.append((x, y, r))

shelters = []
for _ in range(m):
    x, y = map(int, input().split())
    shelters.append((x, y))

# Construct the bipartite graph
graph = construct_graph(students, shelters, b)

# Find the maximum matching
max_matching = maximum_matching(graph)

# Calculate the minimum number of sick students
min_sick_students = n - max_matching

# Output the result
print(min_sick_students)
