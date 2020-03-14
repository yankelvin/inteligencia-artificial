from tictactoe import get_data

data = get_data()


def search(node, tree):
    if node["state"] == tree["state"]:
        return tree

    for m in tree["moves"]:
        if node["state"] == m["state"]:
            return m

    for m in node["moves"]:
        search(m, tree)


def minimax(node, round):
    find = search(node, data)

    if len(find["moves"]) == 0:
        return find["winner"]
    elif round % 2 == 0:
        a = float("inf")
        for m in find["moves"]:
            a = min(a, minimax(m, round + 1))
        return a
    else:
        a = float("-inf")
        for m in find["moves"]:
            a = max(a, minimax(m, round + 1))
        return a


tree = {"state": [0, 0, 0, 0, 0, 0, 0, 0, 0],
        "moves": [], "winner": 0}
resp = minimax(tree, 1)
print(resp)
