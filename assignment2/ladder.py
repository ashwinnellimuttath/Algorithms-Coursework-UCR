import heapq

# Define the ladder class
class Ladder:
    def __init__(self, x1, y1, x2, y2, index):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.index = index
        
    def __lt__(self, other):
        return self.x2 < other.x2

# Read input
n, k = map(int, input().split())
ladders = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    ladder = Ladder(x1, y1, x2, y2, i + 1)
    ladders.append(ladder)

# Sort ladders by x-coordinate of the left endpoint
ladders.sort(key=lambda ladder: ladder.x1)

# Initialize the priority queue and active set
pq = []
active = set()

# Sweep the line from left to right
for ladder in ladders:
    # Add the ladder to the active set
    active.add(ladder)
    
    # Remove ladders that end before the current ladder starts
    while len(pq) > 0 and pq[0].x2 <= ladder.x1:
        ended_ladder = heapq.heappop(pq)
        active.remove(ended_ladder)
    
    # Add intersections with active ladders to the priority queue
    for active_ladder in active:
        if ladder.y1 <= active_ladder.y2 and ladder.y2 >= active_ladder.y1:
            x = (active_ladder.y1 - ladder.y1) / (ladder.y2 - ladder.y1 - active_ladder.y2 + active_ladder.y1)
            intersection = (ladder.x1 + x * (ladder.x2 - ladder.x1), active_ladder.index, ladder.index)
            heapq.heappush(pq, intersection)
    
    # If the k-th intersection is found, output the result and exit
    if len(pq) >= k:
        intersection = heapq.nsmallest(k, pq)[-1]
        print(intersection[1], intersection[2])
        break

# from bisect import bisect_left

# # function to calculate the slope and y-intercept of a ladder
# def get_slope_intercept(x1, y1, x2, y2):
#     slope = (y2 - y1) / (x2 - x1)
#     y_intercept = y1 - slope * x1
#     return slope, y_intercept

# # read input
# n, k = map(int, input().split())

# # read ladder coordinates and calculate slope and y-intercept
# ladders = []
# for i in range(n):
#     x1, y1, x2, y2 = map(int, input().split())
#     slope, y_intercept = get_slope_intercept(x1, y1, x2, y2)
#     ladders.append((slope, y_intercept, i))

# # sort ladders by slope, breaking ties by y-intercept
# ladders.sort()

# # calculate all intersection points
# intersections = []
# for i in range(n):
#     for j in range(i + 1, n):
#         slope1, y_intercept1, ladder1 = ladders[i]
#         slope2, y_intercept2, ladder2 = ladders[j]
#         x = (y_intercept2 - y_intercept1) / (slope1 - slope2)
#         y = slope1 * x + y_intercept1
#         intersections.append((x, y, ladder1, ladder2))

# # sort intersections by x-coordinate
# intersections.sort()

# # perform binary search to find k-th intersection point
# left = 0
# right = len(intersections) - 1
# while left < right:
#     mid = (left + right) // 2
#     count = 0
#     for i in range(mid + 1):
#         x, y, ladder1, ladder2 = intersections[i]
#         if ladder1 < ladder2:
#             count += 1
#     if count < k:
#         left = mid + 1
#     else:
#         right = mid

# # output the k-th intersection point
# x, y, ladder1, ladder2 = intersections[left]
# print(ladder1 + 1, ladder2 + 1)
