"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flattened_board = [item for sublist in board for item in sublist]
    if flattened_board.count(X) == flattened_board.count(O):
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Action is a list of two integers representing the row and column of the move.
    """

    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid move")
    else:
        new_board = [row[:] for row in board]
        new_board[action[0]][action[1]] = player(board)
        return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    flattened_list = [item for sublist in board for item in sublist]
    if flattened_list.count(EMPTY) == 0: #is full
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    match winner(board):
        case value if value == X:
            return 1
        case value if value == O:
            return -1
        case None:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    possible_actions = actions(board)
    current_player = player(board)
    best_value = -math.inf if current_player == X else math.inf

    if not possible_actions:
        raise Exception("No possible actions")

    best_action = None

    for action in possible_actions:
        candidate_value = utility(result(board, action))

        if current_player == X:
            if candidate_value > best_value:
                best_value = candidate_value
                best_action = action
            if candidate_value == 1:
                return action
        elif current_player == O:
            if candidate_value < best_value:
                best_value = candidate_value
                best_action = action
            if candidate_value == -1:
                return action
        else:
            raise Exception("Invalid player")

    return best_action if best_action is not None else possible_actions[0]

