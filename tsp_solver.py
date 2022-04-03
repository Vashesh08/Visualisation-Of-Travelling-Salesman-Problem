# dist = [
#     [0, 74, 4109, 3047, 2266], 
#     [74, 0, 4069, 2999, 2213],
#     [4109, 4069, 0, 1172, 1972], 
#     [3047, 2999, 1172, 0, 816], 
#     [2266, 2213, 1972, 816, 0]
# ]


dist = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]

def path_len(path):
    return sum(dist[i][j] for i, j in zip(path, path[1:]))

to_visit = set(range(len(dist)))

state = {(i, frozenset([0, i])): [0, i] for i in range(1, len(dist[0]))}

for _ in range(len(dist) - 2):
    next_state = {}
    for position, path in state.items():
        current_node, visited = position

        for node in to_visit - visited:
            new_path = path + [node]
            new_pos = (node, frozenset(new_path))

            if new_pos not in next_state or path_len(new_path) < path_len(next_state[new_pos]):
                next_state[new_pos] = new_path

    state = next_state

shortest = min((path + [0] for path in state.values()), key=path_len)
print('path: {0}, length: {1}'.format(shortest, path_len(shortest)))
