from queue import PriorityQueue

# function to check if a cell is valid or not
def is_valid_cell(n, i, j):
    return i >= 0 and i < n and j >= 0 and j < n

# function to find the minimum time to reach the destination
def find_min_time(n, t, playground):
    # initialize the start and destination cells
    start = (0, 0)
    dest = (n-1, n-1)
    
    # initialize the distance array with infinity for all cells except the start cell
    dist = [[float('inf') for j in range(n)] for i in range(n)]
    dist[0][0] = 0
    
    # initialize the priority queue with the start cell and its distance
    pq = PriorityQueue()
    pq.put((0, start))
    
    # initialize the visited array to keep track of visited cells
    visited = [[False for j in range(n)] for i in range(n)]
    
    # run Dijkstra's algorithm
    while not pq.empty():
        # get the cell with the minimum distance from the priority queue
        curr_dist, curr_cell = pq.get()
        
        # if the current cell is the destination, return its distance
        if curr_cell == dest:
            return curr_dist
        
        # mark the current cell as visited
        visited[curr_cell[0]][curr_cell[1]] = True
        
        # check all adjacent cells
        for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            next_cell = (curr_cell[0]+d[0], curr_cell[1]+d[1])
            
            # check if the next cell is valid and not visited
            if is_valid_cell(n, next_cell[0], next_cell[1]) and not visited[next_cell[0]][next_cell[1]]:
                next_dist = curr_dist + 1
                
                # check if the next cell has a banana peel
                if playground[next_cell[0]][next_cell[1]] == 'b':
                    next_dist += t
                
                # update the distance of the next cell if it is shorter than the current distance
                if next_dist < dist[next_cell[0]][next_cell[1]]:
                    dist[next_cell[0]][next_cell[1]] = next_dist
                    pq.put((next_dist, next_cell))
    
    # if the destination cannot be reached, return -1
    return -1

# parse the input
n, t = map(int, input().split())
playground = []
for i in range(n):
    row = input().strip()
    playground.append(row)

# find the minimum time to reach the destination
min_time = find_min_time(n, t, playground)

# output the result
print(min_time)


# import heapq

# n, t = map(int, input().split())
# playground = [input().strip() for _ in range(n)]

# dist = [[float('inf')] * n for _ in range(n)]
# visited = [[False] * n for _ in range(n)]

# # initialize the distances and add the start node to the priority queue
# dist[0][0] = 0
# pq = [(0, (0, 0))]  # priority queue with (distance, node) tuples

# # Dijkstra's algorithm
# while pq:
#     d, (i, j) = heapq.heappop(pq)
#     if visited[i][j]:
#         continue
#     visited[i][j] = True
#     if i == n-1 and j == n-1:  # we have reached the destination
#         print(d)
#         break
#     for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:  # neighbors
#         if 0 <= x < n and 0 <= y < n and not visited[x][y]:
#             w = t if playground[x][y] == 'b' else 1
#             if d + w < dist[x][y]:
#                 dist[x][y] = d + w
#                 heapq.heappush(pq, (dist[x][y], (x, y)))
