import heapq

def find_earliest_arrival(n, k, stairways):
    adj_list = [[] for _ in range(n)]
    for x, y, z in stairways:
        adj_list[x].append((y, z))
        adj_list[y].append((x, z))
    dist = [float('inf')] * n
    dist[0] = 0

    minHeap = [(0, 0)]
    heapq.heapify(minHeap)

    while minHeap:
        curr_platform, curr_time = heapq.heappop(minHeap)

        if curr_platform == k:
            return curr_time

        # if curr_time > dist[curr_platform]:
        #     continue
        print("current", curr_platform)
        for next_platform, stairway in adj_list[curr_platform]:
            if curr_time % 2 == 0:  # even timestamp
                next_time = curr_time + 1
            else:  # odd timestamp
                next_time = curr_time + 2

            if next_time < dist[next_platform]:
                dist[next_platform] = next_time
                heapq.heappush(minHeap, (next_platform, next_time))
        # for x, y, z in stairways:
        #     if x == curr_platform:
        #         if curr_time % 2 == 0:  # even timestamp
        #             next_platform = y
        #             next_time = curr_time + 1
        #         else:  # odd timestamp
        #             next_platform = z
        #             next_time = curr_time + 2

        #         print(next_time,next_platform,dist[next_platform])
        #         if next_time < dist[next_platform]:
        #             dist[next_platform] = next_time
        #             heapq.heappush(minHeap, (next_platform, next_time))

    return -1


n, m, k = map(int, input().split())

stairways = []
for _ in range(m):
    x, y, z = map(int, input().split())
    stairways.append((x, y, z))
earliest_time = find_earliest_arrival(n, k, stairways)
print(earliest_time)