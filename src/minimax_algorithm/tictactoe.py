import pickle
from pprint import pprint


def tictactoe_tree(state, round):
    tree = {"state": state, "moves": [], "winner": 0}

    flag = win(tree["state"])
    if flag == 1:
        tree["winner"] = 1
        return tree
    elif flag == 2:
        tree["winner"] = 2
        return tree

    moves = generate_moves(state, round)
    for m in moves:
        if type(m) is list:
            tree["moves"].append(tictactoe_tree(m, round + 1))

    return tree


def generate_moves(_move, round):
    move = _move[:]
    moves = []
    for i, m in enumerate(_move):
        if m == 0:
            if round % 2 == 1:
                move[i] = 1
            else:
                move[i] = 2

            moves.append(move[:])
            move[i] = 0

    return moves


def filter(case_win, array):
    for w in case_win:
        if array[w[0]] == 1 and array[w[1]] == 1 and array[w[2]] == 1:
            return 1
        elif array[w[0]] == 2 and array[w[1]] == 2 and array[w[2]] == 2:
            return 2
    return 0


def win(array):
    # Case 1 horizontal
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    horizontal = filter(wins, array)

    # Case 2 vertical
    wins = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]

    vertical = filter(wins, array)

    # Case 2 diagonal
    wins = [[0, 4, 8], [2, 4, 6]]

    diagonal = filter(wins, array)

    if horizontal == 1 or vertical == 1 or diagonal == 1:
        return 1
    elif horizontal == 2 or vertical == 2 or diagonal == 2:
        return 2

    return 0

# data = tictactoe_tree([0, 0, 0, 0, 0, 0, 0, 0, 0], 1)
# Grava os arquivos serializados
# pickle.dump(data, open('tictactoe_tree.pkl', 'wb'))


# Lê os arquivos e desserializa
def get_data():
    data = pickle.load(
        open('./src/minimax_algorithm/tictactoe_tree.pkl', 'rb'))
    return data

# pprint(data)
