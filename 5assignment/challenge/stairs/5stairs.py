import heapq



def minimumTime(matrix, n, dest):
    adjacency0 = [[] for _ in range(n)]
    adjacency1 = [[] for _ in range(n)]
    for x, y, z in matrix:
        adjacency0[x].append(z)
        adjacency1[x].append(y)
        adjacency0[y].append(x)
        adjacency0[y].append(z)
        adjacency1[z].append(x)
        adjacency1[z].append(y)
        # adjacency[x].append(z)
        # adjacency[x].append(z)
        # adjacency[y].append((x, z))
        # adjacency[z].append((x, y))

    visited = [False] * n
    pq = []
    heapq.heappush(pq, (0,0))

    while pq:
        time,platform = heapq.heappop(pq)
        if visited[platform]:
            continue
        visited[platform] = True
        timer = time
        if platform == dest:
            return timer
        first = 0
        second = 0
        if timer % 2 == 0:
            first = 2
            second = 1
        else:
            first = 1
            second = 2
        for neighPlatform in adjacency0[platform]:
            if visited[neighPlatform]:
                continue
            # heapq.heappush(pq, Cell(neighPlatform, timer + (first if time == 0 else second)))
            heapq.heappush(pq, (timer + second,neighPlatform ))

        for neighPlatform in adjacency1[platform]:
            if visited[neighPlatform]:
                continue
            # heapq.heappush(pq, Cell(neighPlatform, timer + (first if time == 0 else second)))
            heapq.heappush(pq, (timer + first,neighPlatform ))

    return -1






# a = [1]
# a.append((1,2))
# print(a)











n, m, k = map(int, input().split())

stairways = []
for _ in range(m):
    x, y, z = map(int, input().split())
    stairways.append((x, y, z))
earliest_time = minimumTime(stairways, n, k)
print(earliest_time)