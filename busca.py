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

exit = 'Q'


def search_generic(map, destiny):
    sequence = []
    initial = state = list(map.keys())[0]
    visiteds = {initial: 0}
    control = map[initial]['adjacent'][:]

    while len(control) > 0:
        adjs = [i for i in control if i[0] not in visiteds]

        position = -1
        for i, adj in enumerate(adjs):
            if i == 0:
                position = i
            else:
                if (visiteds[state] + adj[1]) < (visiteds[state] + adjs[position][1]):
                    position = i
        visited = adjs[position]

        sequence.append((visited[0], visited[1]))

        if initial == state:
            visiteds[visited[0]] = visited[1] + visiteds[initial]
        else:
            visiteds[visited[0]] = visited[1] + visiteds[control[position][2]]

        control.remove(visited)

        state = adjs[position][0]

        if state == destiny:
            return sequence

        values = map[state]['adjacent']
        for v in values:
            if v[0] not in visiteds:
                control.append([v[0], v[1], state])

    return sequence


result = search_generic(map_maze, exit)
total = 0
for map in result:
    print(map[0], end=" → ")
    total += map[1]
print("FINISH")
print(f"Total: {total}")
