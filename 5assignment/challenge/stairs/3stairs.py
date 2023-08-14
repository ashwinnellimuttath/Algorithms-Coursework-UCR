from collections import deque

def find_earliest_time(n, k, stairways):
    adj_listy = [[] for _ in range(n)]
    adj_listz = [[] for _ in range(n)]
    # adj_list = [[] for _ in range(n)]
    for x, y, z in stairways:
        adj_listy[x].append(y)
        adj_listy[y].append(x)
        adj_listy[x].append(z)
        adj_listz[z].append(x)
        # adj_listz[x].append(z)
        # adj_listz[z].append(y)
        # adj_list[x].append(y)
        # adj_list[x].append(z)
        # adj_list[y].append(x)
        # adj_list[z].append(x)
        # adj_list[z].append(y)
        # adj_list[y].append(z)

        # adj_list[x].append(y)
    # print(adj_listy,adj_listz)
    min_time = [float('inf')] * n
    min_time[0] = 0




    queue = deque()
    queue.append((0,0))
    # visited = set()
    # visited.add(0)
    minimumTime = float("inf")
    # currTime = 0
    while queue:
        current_platform,curr_time = queue.popleft()
        # print(current_platform,curr_time,"current_platform,curr_time")
        # print(min_time[current_platform])
        if min_time[current_platform] > curr_time:
            print(current_platform,curr_time,"heredfdsfsdg")
        
        min_time[current_platform] = min(min_time[current_platform] , curr_time)
        if current_platform == k:
            # print(current_platform,curr_time,"here")
            minimumTime = min(minimumTime, curr_time)
            # return curr_time

        if curr_time > min_time[current_platform]:
            continue

        if current_platform == 5:
            print(adj_listy[current_platform],adj_listz[current_platform],"5555")
        # if curr_time % 2 == 0:  # even timestamp
        #     next_platform = y
        #     next_time = curr_time + 1
        # else:  # odd timestamp
        #     next_platform = z
        #     next_time = curr_time + 2
        # visited.add(current_platform)

        # for neighbor in adj_list[current_platform]:
        #     queue.append((neighbor,curr_time + 1))

        if curr_time %2 == 0:
            for neighbor in adj_listz[current_platform]:
                queue.append((neighbor,curr_time + 1))
            for neighbor in adj_listy[current_platform]:
                queue.append((neighbor,curr_time + 2))

        else:
            for neighbor in adj_listy[current_platform]:
                queue.append((neighbor,curr_time + 1))
            for neighbor in adj_listz[current_platform]:
                queue.append((neighbor,curr_time + 2))

        # for neighbor in adj_list[current_platform]:
        #     # if min_time[neighbor] == float('inf'):
        #     min_time[neighbor] = min(min_time[neighbor],min_time[current_platform] + 1)
        #     if neighbor not in visited:
        #         queue.append(neighbor)

    if min_time[k] == float('inf'):
        return -1
    else:
        return min_time[k]
    # return minimumTime

n, m, k = map(int, input().split())

stairways = []
for _ in range(m):
    x, y, z = map(int, input().split())
    stairways.append((x, y, z))
# print(stairways)
# k=5
# n=6
# stairways = [(0, 1, 2), (3, 2, 1), (4, 2, 3), (5, 3, 4)]

earliest_time = find_earliest_time(n,k, stairways)

print(earliest_time + 1)
