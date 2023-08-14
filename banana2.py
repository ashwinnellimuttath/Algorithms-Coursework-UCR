import heapq

n, t = map(int, input().split())
# grid = [input().strip() for _ in range(n)]
grid = []
for i in range(n):
    row = input().strip()
    grid.append(row)

def dijkstra():
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    visited = set()
    distances[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    while pq:
        dist, x, y = heapq.heappop(pq)

        if (x,y) in visited:
            continue

        visited.add((x,y))


        if x == n-1 and y == n-1: 
            return distances[n-1][n-1]
        
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            
            dist_neighbor = dist + 1

            if grid[nx][ny] == 'b':
                dist_neighbor += t
            
            if dist_neighbor < distances[nx][ny]:
                distances[nx][ny] = dist_neighbor
                heapq.heappush(pq, (dist_neighbor, nx, ny))
    
    return distances[n-1][n-1]

print(dijkstra())