from sys import maxsize
from itertools import permutations

V = 5

def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    small_route=[]
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0

        k = s
        current_path=i
        for j in i:
            current_pathweight += graph[k][j]
            k = j


        current_pathweight += graph[k][s]


        if current_pathweight<min_path:
            small_route=i
        min_path = min(min_path, current_pathweight)

    y = s+"->"+small_route+"->"+s
    return y,min_path


if __name__ == "_main_":
    graph = [[0, 74, 4109, 3047, 2266],
    [74, 0, 4069, 2999, 2213],
    [4109, 4069, 0, 1172, 1972],
    [3047, 2999, 1172, 0, 816],
    [2266, 2213, 1972, 816, 0]]
    s = 0
