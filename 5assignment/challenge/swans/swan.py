from collections import deque

def can_meet(r, c, lake):
    grid = [list(row) for row in lake]
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
            if grid[i][j] == 'L':
                queue.append((i, j))
                visited[i][j] = True

    while queue:
        days += 1
        level_size = len(queue)

        for _ in range(level_size):
            row, col = queue.popleft()

            for adj_row, adj_col in get_adjacent_cells(row, col):
                if grid[adj_row][adj_col] == 'L':
                    return days

                visited[adj_row][adj_col] = True
                queue.append((adj_row, adj_col))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'X':
                    for dr, dc in directions:
                        new_row, new_col = i + dr, j + dc
                        if is_valid_cell(new_row, new_col) and grid[new_row][new_col] == '.':
                            grid[i][j] = '.'
                            break

    return -1
r, c = map(int, input().split())
lake = [input() for _ in range(r)]
result = can_meet(r, c, lake)
print(result)
