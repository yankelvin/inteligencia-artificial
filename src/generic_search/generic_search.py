import random

map_maze = {
    'A': {
        'adjacent': [('B', 5)],
        'point': (1, 1)
    },
    'B': {
        'adjacent': [('A', 5), ('C', 7), ('F', 2)],
        'point': (1, 6)
    },
    'C': {
        'adjacent': [('B', 7), ('L', 8)],
        'point': (1, 13)
    },
    'D': {
        'adjacent': [('E', 3)],
        'point': (3, 1)
    },
    'E': {
        'adjacent': [('D', 3), ('I', 6)],
        'point': (3, 4)
    },
    'F': {
        'adjacent': [('B', 2), ('G', 5), ('J', 6)],
        'point': (3, 6)
    },
    'G': {
        'adjacent': [('F', 5), ('K', 6)],
        'point': (3, 11)
    },
    'H': {
        'adjacent': [('I', 3)],
        'point': (9, 1)
    },
    'I': {
        'adjacent': [('E', 6), ('J', 2), ('H', 3)],
        'point': (9, 4)
    },
    'J': {
        'adjacent': [('F', 6), ('I', 2), ('K', 5), ('O', 2)],
        'point': (9, 6)
    },
    'K': {
        'adjacent': [('G', 6), ('J', 5), ('L', 2), ('T', 9)],
        'point': (9, 11)
    },
    'L': {
        'adjacent': [('C', 8), ('K', 2), ('U', 9)],
        'point': (9, 13)
    },
    'M': {
        'adjacent': [('N', 3)],
        'point': (11, 1)
    },
    'N': {
        'adjacent': [('M', 3), ('O', 2), ('R', 7)],
        'point': (11, 4)
    },
    'O': {
        'adjacent': [('J', 2), ('N', 2), ('P', 3)],
        'point': (11, 6)
    },
    'P': {
        'adjacent': [('O', 3), ('S', 7)],
        'point': (11, 9)
    },
    'Q': {
        'adjacent': [('R', 3)],
        'point': (18, 1)
    },
    'R': {
        'adjacent': [('N', 7), ('Q', 3), ('S', 5)],
        'point': (18, 4)
    },
    'S': {
        'adjacent': [('P', 7), ('R', 5), ('T', 2)],
        'point': (18, 9)
    },
    'T': {
        'adjacent': [('K', 9), ('S', 2), ('U', 2)],
        'point': (18, 11)
    },
    'U': {
        'adjacent': [('L', 9), ('T', 2)],
        'point': (18, 13)
    }
}


def get_adjacent_not_visited(state_, visited, map):
    states = map_maze[state_]
    return_ = []

    for s in states['adjacent']:
        if s[0] not in visited:
            return_.append([s[0], s[1], state_])

    return return_


def generic_search(map, first_state, objective_state, type):
    visited = [first_state]
    result = [first_state]
    state_ = first_state
    value_ = 0
    count_cost = 0

    control = {
        state_: {
            'sequence': [first_state],
            'cost': value_
        }
    }

    not_visited = []
    destiny_point = map[objective_state]['point']

    while state_ != objective_state:
        not_visited.extend(get_adjacent_not_visited(state_, visited, map))

        if len(not_visited) != 0:
            if type == 0:
                selected_state = random.choice(not_visited)
            elif type == 1:
                selected_state = uniform_cost(not_visited, control)
            elif type == 2:
                selected_state = greedy(
                    not_visited, control, destiny_point, map)
            elif type == 3:
                selected_state = a_star(
                    not_visited, control, destiny_point, map)

            state_ = selected_state[0]
            value_ = selected_state[1]
            visited.append(state_)
            count_cost += value_
            result.append(state_)

            control[state_] = {
                'sequence':  control[selected_state[2]]['sequence'][:],
                'cost': value_ + control[selected_state[2]]['cost']
            }

            control[state_]['sequence'].append(state_)

            not_visited.remove(selected_state)
        else:
            del result[-1]
            state_ = result[-1]
            count_cost -= value_

    return {'sequence': control[objective_state]['sequence'], 'cost': control[objective_state]['cost']}


def uniform_cost(states, control):
    less_value = float('Inf')
    less_state = states[0]

    if len(states) == 1:
        return states[0]

    for s in states:
        s_cost = control[s[2]]['cost'] + s[1]
        less_cost = control[less_state[2]]['cost'] + less_value
        if s_cost < less_cost:
            less_value = s[1]
            less_state = s

    return less_state


def greedy(states, control, destiny, map):
    less_value = float('Inf')
    less_state = states[0]

    if len(states) == 1:
        return states[0]

    for s in states:
        s_point = map[s[0]]['point']

        dist = ((destiny[0] - s_point[0])**2 +
                (destiny[1] - s_point[1])**2)**(0.5)

        if dist < less_value:
            less_value = dist
            less_state = s

    return less_state


def a_star(states, control, destiny, map):
    less_value = float('Inf')
    less_state = states[0]

    if len(states) == 1:
        return states[0]

    for s in states:
        s_point = map[s[0]]['point']
        less_cost = control[less_state[2]]['cost'] + less_value

        s_cost = control[s[2]]['cost'] + s[1]
        dist = ((destiny[0] - s_point[0])**2 +
                (destiny[1] - s_point[1])**2)**(0.5)

        if (s_cost + dist) < (less_cost + less_value):
            less_value = dist
            less_state = s

    return less_state


# Type = 0 (Random) | 1 (Uniform Cost) | 2 (Greedy) | 3 (A-Star)
result = generic_search(map_maze, 'A', 'Q', type=1)

print(f"Caminho resultante: {result['sequence']}")
print(f"Custo do caminho: {result['cost']}")
