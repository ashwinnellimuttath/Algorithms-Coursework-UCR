from queue import Queue
from heapq import heappop, heappush

class Cell:
    def __init__(self, row, col, time):
        self.row = row
        self.col = col
        self.time = time

def calculateTimeToBecomeDot(matrix):
    rows = len(matrix)
    if rows == 0:
        return []

    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = Queue()

    # Enqueue all cells containing '.' and mark them as visited with time 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '.':
                q.put(Cell(i, j, 0))
                visited[i][j] = True

    # Perform BFS
    while not q.empty():
        cell = q.get()

        for dir in directions:
            newRow = cell.row + dir[0]
            newCol = cell.col + dir[1]

            if 0 <= newRow < rows and 0 <= newCol < cols and not visited[newRow][newCol]:
                if matrix[newRow][newCol] == 'X':
                    matrix[newRow][newCol] = cell.time + 1
                    q.put(Cell(newRow, newCol, cell.time + 1))
                    visited[newRow][newCol] = True

    # Convert the matrix to contain time values
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'X':
                result[i][j] = -1  # Mark unreachable cells with -1
            else:
                result[i][j] = matrix[i][j] if matrix[i][j] == '.' else 0

    return result

def isValid(row, col, numRows, numCols):
    return 0 <= row < numRows and 0 <= col < numCols

def findMinimumPath(matrix, source, destination):
    numRows = len(matrix)
    numCols = len(matrix[0])
    visited = [[False] * numCols for _ in range(numRows)]
    pq = []
    heappush(pq, Cell(source[0], source[1], matrix[source[0]][source[1]]))
    visited[source[0]][source[1]] = True

    while pq:
        currCell = heappop(pq)
        currRow = currCell.row
        currCol = currCell.col
        currMaxValue = currCell.time

        if currRow == destination[0] and currCol == destination[1]:
            return currMaxValue

        neighborsRow = [-1, 1, 0, 0]
        neighborsCol = [0, 0, -1, 1]

        for i in range(4):
            nextRow = currRow + neighborsRow[i]
            nextCol = currCol + neighborsCol[i]

            if isValid(nextRow, nextCol, numRows, numCols) and not visited[nextRow][nextCol]:
                heappush(pq, Cell(nextRow, nextCol, max(currMaxValue, matrix[nextRow][nextCol])))
                visited[nextRow][nextCol] = True

    return -1

if __name__ == "__main__":
    r, c = map(int, input().split())
    source = (0, 0)
    destination = (3, 3)
    matrix = []

    for _ in range(r):
        row = list(input())
        matrix.append(row)

    change = True
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 'L':
                if change:
                    source = (i, j)
                    change = False
                    matrix[i][j] = '.'
                else:
                    destination = (i, j)
                    matrix[i][j] = '.'

    res = calculateTimeToBecomeDot(matrix)
    for row in res:
        print(' '.join(map(str, row)))

    val = findMinimumPath(res, source, destination)
    print(val)
