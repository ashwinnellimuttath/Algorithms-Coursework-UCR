def evaluate_state(state):
    for row in state:
        if row.count('X') == 3:
            return 1  
        elif row.count('O') == 3:
            return -1  

    # Check columns
    for col in range(3):
        if state[0][col] == state[1][col] == state[2][col] == 'X':
            return 1  
        elif state[0][col] == state[1][col] == state[2][col] == 'O':
            return -1  

    # Check diagonals
    if state[0][0] == state[1][1] == state[2][2] == 'X' or state[0][2] == state[1][1] == state[2][0] == 'X':
        return 1 
    elif state[0][0] == state[1][1] == state[2][2] == 'O' or state[0][2] == state[1][1] == state[2][0] == 'O':
        return -1 

    return 0  # Draw


def is_terminal_state(state):
    for row in state:
        if '#' in row:
            return False  

    return True  


def get_available_actions(state):
    actions = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '#':
                actions.append((i, j))
    return actions


def minimax(state, maximizing_player):
    result = evaluate_state(state)

    if result != 0:  
        return result

    if is_terminal_state(state):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for action in get_available_actions(state):
            new_state = [row[:] for row in state]
            new_state[action[0]][action[1]] = 'X'
            evaluation = minimax(new_state, False)
            max_eval = max(max_eval, evaluation)
        return max_eval

    else:
        min_eval = float('inf')
        for action in get_available_actions(state):
            new_state = [row[:] for row in state]
            new_state[action[0]][action[1]] = 'O'
            evaluation = minimax(new_state, True)
            min_eval = min(min_eval, evaluation)
        return min_eval


def predict_winner(initial_state,player):
    result = minimax(initial_state, player)

    if result > 0:
        return "Crosses win"
    elif result < 0:
        return "Noughts win"
    else:
        return "Draw"


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
winner = predict_winner(board, player1=='X')
print(winner)

# winner = predict_winner(state)
# print(winner)
