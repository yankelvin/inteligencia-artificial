from tictactoe import get_data, win

data = get_data()


def search(state, tree):
    if state["state"] == tree["state"]:
        return tree

    for m in tree["moves"]:
        if state["state"] == m["state"]:
            return m

    for m in tree["moves"]:
        return search(m, tree)


def max_value(state):
    if win(state["state"]) != 0:
        return state

    v = float("inf")
    for m in state["moves"]:
        result = min_value(m)
        v = min(v, result["winner"])
    return {"winner": v, "tree": state}


def min_value(state):
    winner = win(state["state"])
    if winner != 0:
        return {"winner": winner, "tree": state}

    v = float("-inf")
    for m in state["moves"]:
        result = max_value(m)
        v = max(v, result["winner"])
    return {"winner": v, "tree": state}


def minimax(state):
    find = search(state, data)

    return min_value(find)


tree = {"state": [1, 0, 1, 0, 2, 0, 2, 0, 0]}
result = minimax(tree)
print(result)
