import itertools

n, k = map(int, input().split())

ladders = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    ladders.append(((x1, y1), (x2, y2)))

# print(ladders)
# ladders.sort(key=lambda ladder: ladder[0][0])
# print(ladders)



intersections = []
for i, j in itertools.combinations(range(n), 2):
    (x1, y1), (x2, y2) = ladders[i]
    (x3, y3), (x4, y4) = ladders[j]
    a1, b1, c1 = y2 - y1, x1 - x2, x2*y1 - x1*y2
    a2, b2, c2 = y4 - y3, x3 - x4, x4*y3 - x3*y4
    det = a1*b2 - a2*b1
    if det != 0:
        x = (b2*c1 - b1*c2) / det
        y = (a1*c2 - a2*c1) / det
        # if min(x1, x2) <= x <= max(x1, x2) and min(x3, x4) <= x <= max(x3, x4):
        intersections.append((x, y, i, j))

intersections.sort()

i, j = intersections[k-1][2], intersections[k-1][3]
print(intersections)
print(i+1, j+1)



# from typing import List, Tuple

# # Function to find intersection point of two line segments
# def find_intersection_point(l1: Tuple[int, int, int, int], l2: Tuple[int, int, int, int]) -> Tuple[float, float]:
#     x1, y1, x2, y2 = l1
#     x3, y3, x4, y4 = l2
    
#     # Calculate slopes and y-intercepts of the two lines
#     slope1 = (y2 - y1) / (x2 - x1)
#     slope2 = (y4 - y3) / (x4 - x3)
#     yint1 = y1 - slope1 * x1
#     yint2 = y3 - slope2 * x3
    
#     # Calculate intersection point
#     x_int = (yint2 - yint1) / (slope1 - slope2)
#     y_int = slope1 * x_int + yint1
    
#     return x_int, y_int


# # Function to find kth intersection point
# def find_kth_intersection(n: int, k: int, ladders: List[Tuple[int, int, int, int]]) -> Tuple[int, int]:
#     intersections = []
    
#     # Find all intersection points
#     for i in range(n):
#         for j in range(i+1, n):
#             intersection_point = find_intersection_point(ladders[i], ladders[j])
#             intersections.append((intersection_point[0], i, j))
    
#     # Sort intersection points by x-coordinate
#     intersections.sort()
    
#     # Return kth intersection point
#     return intersections[k-1][1], intersections[k-1][2]

# print(find_kth_intersection(n,k,ladders))



