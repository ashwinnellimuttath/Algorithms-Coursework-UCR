from collections import deque

def find_earliest_time(n, m, k, stairways):
    adj_list = [[] for _ in range(n)]
    for x, y, z in stairways:
        adj_list[x].append(y)
        adj_list[y].append(x)
        adj_list[x].append(z)
        adj_list[z].append(x)

    min_time = [float('inf')] * n
    min_time[0] = 0




    queue = deque()
    queue.append((0,0))
    visited = set()
    visited.add(0)
    currTime = 0
    while queue:
        current_platform,currTime = queue.popleft()
            #         if curr_time % 2 == 0:  # even timestamp
    #             next_platform = y
    #             next_time = curr_time + 1
    #         else:  # odd timestamp
    #             next_platform = z
    #             next_time = curr_time + 2
        visited.add(current_platform)
        for neighbor in adj_list[current_platform]:
            # if min_time[neighbor] == float('inf'):
            min_time[neighbor] = min(min_time[neighbor],min_time[current_platform] + 1)
            if neighbor not in visited:
                queue.append(neighbor)

    if min_time[k] == float('inf'):
        return -1
    else:
        return min_time[k]

n, m, k = map(int, input().split())

stairways = []
for _ in range(m):
    x, y, z = map(int, input().split())
    stairways.append((x, y, z))
earliest_time = find_earliest_time(n, m, k, stairways)

print(earliest_time + 1)
