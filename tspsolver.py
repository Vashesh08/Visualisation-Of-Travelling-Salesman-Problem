from sys import maxsize
from itertools import permutations

V=5

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    small_route=[]
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        current_path=i
        for j in i:
            current_pathweight += graph[k][j]
            k = j


        current_pathweight += graph[k][s]


        # update minimum
        if current_pathweight<min_path:
            small_route=i
        print(current_pathweight)
        min_path = min(min_path, current_pathweight)

    print(s,"->",small_route,"->",s)
    return min_path


# Driver Code
if __name__ == "_main_":
    # matrix representation of graph
    graph = [[0, 74, 4109, 3047, 2266],
    [74, 0, 4069, 2999, 2213],
    [4109, 4069, 0, 1172, 1972],
    [3047, 2999, 1172, 0, 816],
    [2266, 2213, 1972, 816, 0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))