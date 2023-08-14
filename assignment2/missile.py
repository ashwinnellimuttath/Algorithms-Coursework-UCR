# import math

# def distance(x1, y1, x2, y2):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# def can_intercept(x1, y1, x2, y2, r1, r2, missiles):
#     for x, y in missiles:
#         if distance(x, y, x1, y1) > r1 and distance(x, y, x2, y2) > r2:
#             return False
#     return True

# def find_min_cost(x1, y1, x2, y2, missiles):
#     max_dist = 0
#     for x, y in missiles:
#         max_dist = max(max_dist, distance(x, y, x1, y1), distance(x, y, x2, y2))
#     lo, hi = 0, max_dist**2
#     while lo < hi:
#         mid = (lo + hi) // 2
#         r1 = math.sqrt(mid)
#         r2 = math.sqrt(mid)
#         if can_intercept(x1, y1, x2, y2, r1, r2, missiles):
#             hi = mid
#         else:
#             lo = mid + 1
#     r1 = math.sqrt(lo)
#     lo, hi = 0, max_dist**2
#     while lo < hi:
#         mid = (lo + hi) // 2
#         r1 = math.sqrt(lo)
#         r2 = math.sqrt(mid)
#         if can_intercept(x1, y1, x2, y2, r1, r2, missiles):
#             hi = mid
#         else:
#             lo = mid + 1
#     r2 = math.sqrt(lo)
#     return r1**2, r2**2

# x1, y1, x2, y2 = map(int, input().split())
# n = int(input())
# missiles = [tuple(map(int, input().split())) for _ in range(n)]
# print(find_min_cost(x1, y1, x2, y2, missiles))  # Output: 18



import math

x1, y1, x2, y2 = map(int, input().split())
n = int(input())
distanceArray = [float("inf")] * n

missiles = [tuple(map(int, input().split())) for _ in range(n)]

minR1 = float("inf")
minR2 = float("inf")

def distance(x1, y1, x2, y2):
    # print(x1,y1,x2,y2)
    # print((x1-x2)**2 + (y1-y2)**2)
    return ((x1-x2)**2 + (y1-y2)**2)

def can_intercept(x1, y1, x2, y2, r, missiles):
    global minR1,minR2, distanceArray
    isPossible = False
    # print(r,"r")
    for i,(x, y) in enumerate(missiles):
        print(distanceArray)
        dist = distance(x, y, x1, y1)
        if dist <= r:
            if distanceArray[i] >= r:
                distanceArray[i] = r
                # print(r,"radiuis")
                # print(minR1)
                minR1 = min(minR1,r)
                isPossible = True

        # if distance(x, y, x2, y2) <= r:
        #     if distanceArray[i] >= r:
        #         distanceArray[i] = r
        #         minR2 = min(minR2,r)
        #         isPossible = True
    return isPossible

def find_min_cost(x1, y1, x2, y2, missiles):
    max_dist = 0
    for x, y in missiles:
        max_dist = max(max_dist, distance(x, y, x1, y1), distance(x, y, x2, y2))
    lo, hi = 0, max_dist**2
    while lo < hi:
        mid = (lo + hi) // 2
        if can_intercept(x1, y1, x2, y2, mid, missiles):
            hi = mid
        else:
            lo = mid + 1
    return lo

    

# Example usage

(find_min_cost(x1, y1, x2, y2, missiles)) 
print(distanceArray)
print(minR1, "R1",minR2, "R2","min")


# import math

# def squared_distance(x1, y1, x2, y2):
#     return (x1 - x2) ** 2 + (y1 - y2) ** 2

# def can_intercept_all_missiles(x1, y1, x2, y2, r, missiles):

#     for missile in missiles:
#         x, y = missile
#         if squared_distance(x1, y1, x, y) > r and squared_distance(x2, y2, x, y) > r:
#             return False
#     return True

# def smallest_sum_of_squared_radii(x1, y1, x2, y2, missiles):
#     lo = 0
#     hi = 30
#     while lo < hi:
#         mid = (lo + hi) // 2
#         if can_intercept_all_missiles(x1, y1, x2, y2, mid, missiles):
#             hi = mid
#         else:
#             lo = mid + 1
#     print(mid,x1, y1, x2, y2 )
#     return hi ** 2

# x1, y1, x2, y2 = map(int, input().split())
# n = int(input())
# missiles = [tuple(map(int, input().split())) for _ in range(n)]
# print(smallest_sum_of_squared_radii(x1, y1, x2, y2, missiles))



# import math

# def can_intercept_all(x, y, r, missiles):
#     for mx, my in missiles:
#         if math.hypot(mx-x, my-y) > r:
#             return False
#     return True

# x1, y1, x2, y2 = map(int, input().split())
# n = int(input())
# missiles = [tuple(map(int, input().split())) for _ in range(n)]

# # binary search for r1
# lo, hi = 0, 30
# while lo < hi:
#     mid = (lo + hi) // 2
#     if can_intercept_all(x1, y1, mid, missiles):
#         hi = mid
#     else:
#         lo = mid + 1
# print(mid,lo,"here")
# r1 = lo

# # binary search for r2
# lo, hi = 0, 30
# while lo < hi:
#     mid = (lo + hi) // 2
#     if can_intercept_all(x2, y2, mid, missiles):
#         hi = mid
#     else:
#         lo = mid + 1
# print(mid,lo,"here")
# r2 = lo

# print(r1*r1 + r2*r2)
