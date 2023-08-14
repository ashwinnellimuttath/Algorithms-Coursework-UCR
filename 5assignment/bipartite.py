import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def build_bipartite_graph(students, shelters):
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

def find_matching(graph):
    num_students = len(graph)
    num_shelters = len(graph[0])
    matching = [-1] * num_shelters
    visited = [False] * num_shelters

    def dfs(student):
        for shelter in range(num_shelters):
            if not visited[shelter] and graph[student][shelter] != float("inf"):
                visited[shelter] = True
                if matching[shelter] == -1 or dfs(matching[shelter]):
                    matching[shelter] = student
                    return True
        return False

    for student in range(num_students):
        visited = [False] * num_shelters
        dfs(student)

    return matching

def count_sick_students(students, shelters, b):
    graph = build_bipartite_graph(students, shelters)
    matching = find_matching(graph)
    num_sick_students = 0
    non_sick_students = 0

    for student, shelter in enumerate(matching):
        if shelter != -1:
            non_sick_students += 1

    return len(graph) - non_sick_students

n, m, b = map(int, input().split())

students = []
for _ in range(n):
    x, y, r = map(int, input().split())
    students.append((x, y, r))

shelters = []
for _ in range(m):
    x, y = map(int, input().split())
    shelters.append((x, y))

min_sick_students = count_sick_students(students, shelters, b)
print(min_sick_students)
