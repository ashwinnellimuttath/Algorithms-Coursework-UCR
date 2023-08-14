import math

x1, y1, x2, y2 = map(int, input().split())
n = int(input())
distanceArray = [float("inf")] * n

missiles = [tuple(map(int, input().split())) for _ in range(n)]

minR1 = float("inf")
minR2 = float("inf")

def distance(x1, y1, x2, y2):
    # print(x1,y1,x2,y2)
    return ((x1-x2)**2 + (y1-y2)**2)

def can_intercept(x1, y1, r, missiles):
    global minR1,minR2, distanceArray
    # print(r,"r")
    isPossible = False
    # print(x1,y1, "x222")
    for i,(x, y) in enumerate(missiles):
        # print(distanceArray)
        dist = distance(x, y, x1, y1)
        # print(dist,"dsttt",x, y, x1, y1)
        if dist <= r:
            if distanceArray[i] > dist:
                distanceArray[i] = dist
                # print(r,"radiuis")
                # print(minR1)
                # minR1 = min(minR1,r)
                isPossible = True
                print(dist,i,r)
                if minR1 > r:
                    minR1 = r
        # else:
        #     return False

        # if distance(x, y, x1, y1) <= r:
        #     if distanceArray[i] >= r:
        #         distanceArray[i] = r
        #         minR2 = min(minR2,r)
        #         isPossible = True
    return isPossible
        # return not (distance(x1, y1, x, y) > r)
#             return False

def find_min_cost(x1, y1, x2, y2, missiles):
    global distanceArray, minR1
    max_dist = 0
    for x, y in missiles:
        max_dist = max(max_dist, distance(x, y, x1, y1), distance(x, y, x2, y2))

    # missiles = [(distance(x, y, x1, y1)) for x, y in missiles]
    # missiles.sort(reverse=True)
    missiles.sort(key=lambda missile: -(missile[0] - x1) ** 2 + (missile[1] - y1) ** 2)

    # print(missiles)
    lo, hi = 0, max_dist*2
    while lo < hi:
        mid = (lo + hi) // 2
        print(mid, "mid")
        if can_intercept(x1, y1, mid, missiles):
            hi = mid - 1
        else:
            lo = mid + 1
    a = (distanceArray) 
    print(distanceArray, minR1)

    # distanceArray = [float("inf")] * n
    minR1 = float("inf")
    lo, hi = 0, max_dist
    while lo < hi:
        mid = (lo + hi) // 2
        if can_intercept(x2, y2, mid, missiles):
            hi = mid
        else:
            lo = mid + 1
    b = minR1
    # print(minR1)
    print(distanceArray)

    b = (distanceArray)
    # print(min(a,c), min(b,d))
    maxA = float("-inf")
    maxB = float("-inf")
    for i in range(len(distanceArray)):
        a[i] = min(a[i],b[i])
        b[i] = max(a[i],b[i])
    # print(maxA,maxB, "msx")
    # print(a[i])
    print(max(a), min(b))
    return (maxA + maxB)


    
    

# Example usage

print(find_min_cost(x1, y1, x2, y2, missiles)) 
# print(distanceArray)
# print(minR1, "R1",minR2, "R2","min")
