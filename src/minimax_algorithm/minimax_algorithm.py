from tictactoe import get_data


def minimax_decision(state):
    # if terminal_test(state):
    #     return utility(state)

    v = float("inf")

    # for a in actions(state):
    #     v = max(v, max_value(result(state, a)))

    return v


def max_value(state):
    # if terminal_test(state):
    #     return utility(state)

    v = float("-inf")

    # for a in actions(state):
    #     v = max(v, min_value(result(state, a)))
    return v


def min_value(state):
    return


print(get_data())
