import heapq

n, t = map(int, input().split())
grid = []
for i in range(n):
    row = input().strip()
    grid.append(row)

def djikstras():
    distances = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    visited = set()
    minHeap = [(0,0,0)]

    while minHeap:
        distance,x,y = heapq.heappop(minHeap)
        if (x,y) in visited:
            continue
        visited.add((x,y))

        if x == n-1 and y == n-1: 
            return distances[n-1][n-1]

        distances[x][y] = distance

        directions = [(1,0), (-1,0), (0,1),(0,-1)]

        for nx,ny in directions:
            newX,newY = x + nx, y + ny


            if newX < 0 or newY < 0 or newX >= n or newY >= n or (newX,newY) in visited:
                continue
            newdistance =  distance + 1
            if (grid[newX][newY] == 'b'):
                newdistance += t

            if newdistance < distances[newX][newY]:
                distances[newX][newY] = newdistance
                heapq.heappush(minHeap, (newdistance, newX, newY))
    
    return (distances[n-1][n-1])

print(djikstras())