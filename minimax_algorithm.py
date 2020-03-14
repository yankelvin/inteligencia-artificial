from pprint import pprint
import pickle


def tictactoe_tree():
    initial = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    tree = {"state": initial, "moves": []}

    def generate(node, round):
        move = node["state"][:]
        moves = []
        for i, s in enumerate(node["state"]):
            if s == 0:
                if round % 2 == 1:
                    move[i] = 1
                else:
                    move[i] = 2

                moves.append(move[:])
                move[i] = 0

        if len(moves) == 0:
            return tree["moves"].append(node)

        for m in moves:
            t = {"state": move, "moves": moves}
            node["moves"].append(t)
            generate({"state": m, "moves": []}, round + 1)

    generate(tree, 1)

    return tree


def minimax_decision(state):
    return min_value()


def max_value(state):
    if terminal_test(state):
        return utility(state)

    v = float("-inf")

    for a in actions(state):
        v = max(v, min_value(result(state, a)))
    return v


def min_value(state):
    return


tictactoe_tree()
# Grava os arquivos serializados
# pickle.dump(tictactoe_tree(), open('tictactoe_tree.pkl', 'wb'))

# Lê os arquivos e de-serializa
# data = pickle.load(open('tictactoe_tree.pkl', 'rb'))

pprint(data)
