def distance(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

def find_min_cost(x1, y1, x2, y2, missiles):
    n = len(missiles)
    distances = [(distance(x, y, x1, y1), distance(x, y, x2, y2)) for x, y in missiles]
    distances.sort(reverse=True)
    maxA = maxB = 0
    for d1, d2 in distances:
        if d1 < d2:
            maxA = max(maxA, d1)
            r = d1
        else:
            maxB = max(maxB, d2)
            r = d2
        for j in range(n):
            if distance(missiles[j][0], missiles[j][1], missiles[d1 < d2][0], missiles[d1 < d2][1]) <= r:
                distances[j] = (min(distances[j][0], d1), min(distances[j][1], d2))
    return maxA + maxB

x1, y1, x2, y2 = map(int, input().split())
n = int(input())
missiles = [tuple(map(int, input().split())) for _ in range(n)]
print(find_min_cost(x1, y1, x2, y2, missiles))


# import heapq

# def distance(x1, y1, x2, y2):
#     return (x1-x2)**2 + (y1-y2)**2

# def find_min_cost(x1, y1, x2, y2, missiles):
#     max_dist = 0
#     n = len(missiles)
#     distances = [[distance(x, y, x1, y1), distance(x, y, x2, y2)] for x, y in missiles]
#     max_heap = [(-dist, i) for i, dist in enumerate(map(max, distances))]
#     heapq.heapify(max_heap)
#     maxA = maxB = 0
#     distanceArray = [10**18] * n
#     while max_heap:
#         _, i = heapq.heappop(max_heap)
#         d1, d2 = distances[i]
#         if distanceArray[i] < d1 and distanceArray[i] < d2:
#             continue
#         if d1 < d2:
#             maxA = max(maxA, d1)
#             r = d1
#         else:
#             maxB = max(maxB, d2)
#             r = d2
#         distanceArray[i] = r
#         for j in range(n):
#             if j == i:
#                 continue
#             dist = distance(missiles[i][0], missiles[i][1], missiles[j][0], missiles[j][1])
#             if dist <= r:
#                 d1, d2 = distances[j]
#                 if distanceArray[j] < d1 and distanceArray[j] < d2:
#                     continue
#                 if d1 < d2:
#                     heapq.heappush(max_heap, (-d1, j))
#                 else:
#                     heapq.heappush(max_heap, (-d2, j))
#                 distanceArray[j] = min(d1, d2)
#     return maxA + maxB


# x1, y1, x2, y2 = map(int, input().split())
# n = int(input())
# missiles = [tuple(map(int, input().split())) for _ in range(n)]
# print(find_min_cost(x1, y1, x2, y2, missiles)) 