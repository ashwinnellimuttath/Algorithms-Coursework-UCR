def evaluate(board):
    # Check rows
    for row in board:
        if row.count('X') == 3:
            return 'Crosses win'
        elif row.count('O') == 3:
            return 'Noughts win'

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            return 'Crosses win'
        elif board[0][col] == board[1][col] == board[2][col] == 'O':
            return 'Noughts win'

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return 'Crosses win'
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'Noughts win'

    return 'Draw'


def minimax(board, player):
    result = evaluate(board)

    if result != 'Draw':
        return result

    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '#':
                new_board = [row.copy() for row in board]
                new_board[i][j] = player
                moves.append((i, j, minimax(new_board, 'O' if player == 'X' else 'X')))

    if player == 'X':
        best_move = max(moves, key=lambda move: move[2])
    else:
        best_move = min(moves, key=lambda move: move[2])

    return best_move[2]


# Example usage:
board = []
for _ in range(3):
    row = input().strip()
    board.append(list(row))

count_x = 0
count_o = 0

for row in board:
    count_x += row.count('X')
    count_o += row.count('O')

if count_x > count_o:
    player1 = 'O'
else:
    player1 = 'X'
winner = minimax(board, player1)
print(winner)
