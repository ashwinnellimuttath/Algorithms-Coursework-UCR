from collections import deque
import heapq

def can_meet(r, c, grid):
    # grid = [list(row) for row in lake]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_cell(row, col):
        return 0 <= row < r and 0 <= col < c

    def get_adjacent_cells(row, col):
        adjacent_cells = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_cell(new_row, new_col) and grid[new_row][new_col] != 'X':
                adjacent_cells.append((new_row, new_col))
        return adjacent_cells

    queue = deque()
    visited = [[False] * c for _ in range(r)]
    days = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                queue.append((i, j, 0))
                visited[i][j] = True

    while queue:
        days += 1
        length = len(queue)

        for _ in range(length):
            row, col, timenow = queue.popleft()
            for dr,dc in directions:
                newRow, newCol= row + dr, col + dc
                if is_valid_cell(newRow, newCol) and not visited[newRow][newCol]:
                    if grid[newRow][newCol] != "L":
                        grid[newRow][newCol] = timenow + 1
                        visited[newRow][newCol] = True
                        queue.append((newRow,newCol,timenow + 1))


    result = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'X':
                result[i][j] = -1
            else:
                result[i][j] = 0 if grid[i][j] == '.' else grid[i][j]

    return result


def isValid(row, col, numRows, numCols):
    return 0 <= row < numRows and 0 <= col < numCols

def findMinimumPath(matrix, source, destination):
    numRows = len(matrix)
    numCols = len(matrix[0])
    visited = [[False] * numCols for _ in range(numRows)]
    pq = []
    heapq.heappush(pq, (0, source))
    visited[source[0]][source[1]] = True

    while pq:
        t,(r,c) = heapq.heappop(pq)
        # if visited[r][c]
        currMaxValue = t

        if r == destination[0] and c == destination[1]:
            return currMaxValue

        neighborsRow = [-1, 1, 0, 0]
        neighborsCol = [0, 0, -1, 1]

        for i in range(4):
            nextRow = r + neighborsRow[i]
            nextCol = c + neighborsCol[i]

            if isValid(nextRow, nextCol, numRows, numCols) and not visited[nextRow][nextCol]:
                # heapq.heappush(pq, (max(currMaxValue,matrix[nextRow][nextCol]), matrix[nextRow][nextCol] ))
                # print(matrix[nextRow][nextCol])
                heapq.heappush(pq, (max(currMaxValue,matrix[nextRow][nextCol]), (nextRow,nextCol) ))
                visited[nextRow][nextCol] = True

    return -1










r, c = map(int, input().split())
lake = [input() for _ in range(r)]
grid = [list(row) for row in lake]
change = True
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'L':
            if change:
                source = (i, j)
                change = False
                grid[i][j] = '.'
            else:
                destination = (i, j)
                grid[i][j] = '.' 
result = can_meet(r, c, grid)


val = findMinimumPath(result, source, destination)
print(val) 