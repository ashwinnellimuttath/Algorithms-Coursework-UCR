# import math

# x1, y1, x2, y2 = map(int, input().split())
# n = int(input())

# missiles = [tuple(map(int, input().split())) for _ in range(n)]

# minR1 = float("inf")
# minR2 = float("inf")

# def distance(x1, y1, x2, y2):
#     return ((x1-x2)**2 + (y1-y2)**2)

# def can_intercept_all_missiles(x1, y1, x2, y2, missiles, r1, r2):
#     for missile in missiles:
#         x, y = missile
#         if ((x-x1)**2 + (y-y1)**2 > r1) or ((x-x2)**2 + (y-y2)**2 > r2):
#             return False
#     return True

# def find_min_cost(x1, y1, x2, y2, missiles):
#     max_dist = 0
#     min_dist = float("inf")
#     for x, y in missiles:
#         max_dist = max(max_dist, (distance(x, y, x1, y1)), (distance(x, y, x2, y2)))
#         min_dist = min(max_dist, (distance(x, y, x1, y1)), (distance(x, y, x2, y2)))
#     # print(max_dist, min_dist)
#     lo, hi = 0, max_dist
#     while lo < hi:
#         mid = (lo + hi) // 2
#         # r1 = max(mid, max_dist - mid)
#         # r2 = min(mid, max_dist - mid)
#         if can_intercept_all_missiles(x1, y1, x2, y2, missiles, r1, r2):
#             lo = mid + 1
#         else:
#             hi = mid
#     print(r1,r2)
#     return minR1 + minR2

# print(find_min_cost(x1, y1, x2, y2, missiles))

import math

def distance(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2


def find_optimal_radii(x1, y1, x2, y2, missiles):
    # find the maximum distance between each system and any missile
    maxRange = []
    aDistances = [(distance(x, y, x1, y1)) for x, y in missiles]
    bDistances = [(distance(x, y, x2, y2)) for x, y in missiles]

    # sortedB = sorted(bDistances)
    # max_val = sortedB[0] # initialize max_val to the first element of the array
    # result = [] # initialize an empty list to store the max value so far at each index
    # for i in range(len(bDistances)):
    #     max_val = max(max_val, sortedB[i]) # update the maximum value seen so far
    #     result.append(max_val) # append the maximum value so far to the result list
    # print(result)
    # return result
    # print(aDistances)
    # print(bDistances)

    sortedRes = sorted(zip(aDistances, bDistances), key=lambda x: x[0])
    # print((sortedRes),"sorted")
    
    maxVal = sortedRes[-1][1]
    newSortedRes = []
    for i in reversed(range(len(sortedRes))):
        maxVal = max(maxVal, sortedRes[i][1])
        # print(sortedRes[i][1], maxVal)
        newTuple = (sortedRes[i][0], max(sortedRes[i][1], maxVal))
        newSortedRes.append(newTuple)
    sortedRes = newSortedRes[::-1]

    # print(sortedRes)

    for i in range(len(sortedRes)):
        aRange = sortedRes[i][0]
        bRange = 0
        j = i + 1
        if j < len(sortedRes):
            bRange = sortedRes[j][1]
        # j = i + 1
        # print(i,j,"i,j")
        # for j in range(i + 1, len(sortedRes)):
        #     bRange = max(bRange,sortedRes[j][1])
        maxRange.append(aRange + bRange)

    return (min(maxRange))
        



#     sortedA = sorted(aDistances)

# # Sort bDistances based on aDistances
#     # bDistances = [bDistances[i] for i in (range(len(bDistances)), key=lambda k: aDistances[k])]

#     print(sortedA)
#     print(bDistances)

    # for a, b in zip(aDistances, bDistances):
    #     print(f"Missile distances to targets: {a}, {b}")


    
x1, y1, x2, y2 = map(int, input().split())
n = int(input())

missiles = [tuple(map(int, input().split())) for _ in range(n)]
print(find_optimal_radii(x1, y1, x2, y2, missiles))

# import math

# def can_intercept_all_missiles(x1, y1, x2, y2, missiles, r1, r2):
#     for missile in missiles:
#         x, y = missile
#         if ((x-x1)**2 + (y-y1)**2 > r1**2) and ((x-x2)**2 + (y-y2)**2 > r2**2):
#             return False
#     return True

# def min_squared_radii(x1, y1, x2, y2, missiles):
#     # calculate the total radius needed to cover all missiles
#     total_radius = 0
#     for missile in missiles:
#         x, y = missile
#         distance = math.sqrt((x-x1)**2 + (y-y1)**2)
#         total_radius = max(total_radius, distance)
#         distance = math.sqrt((x-x2)**2 + (y-y2)**2)
#         total_radius = max(total_radius, distance)

#     # perform binary search to find the minimum sum of squared radii
#     eps = 1e-9
#     low = 0.0
#     high = total_radius
#     while high - low > eps:
#         mid = (low + high) / 2.0
#         r1 = max(mid, total_radius - mid)
#         r2 = min(mid, total_radius - mid)
#         if can_intercept_all_missiles(x1, y1, x2, y2, missiles, r1, r2):
#             low = mid
#         else:
#             high = mid

#     # return the sum of squared radii
#     r1 = max(low, total_radius - low)
#     r2 = total_radius - r1
#     print(r1,r2)
#     return int(r1**2 + r2**2)

# print(min_squared_radii(x1, y1, x2, y2, missiles))
