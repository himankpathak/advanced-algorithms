import sys
from graph import read_graph
from collections import defaultdict


def check_recursive(graph, visited, index, parent):
    visited[index] = True
    for i in graph[index]:
        if visited[i] == False:
            if not check_recursive(graph, visited, i, index):
                return False
        elif i != parent:
            return False
    return True


def checkTree(graph):
    visited = defaultdict(bool)

    isValid = check_recursive(graph, visited, 0, -1)

    if not isValid:
        raise Exception("Graph is not a tree")


def calcCost(weights, children, cost_include, cost_exclude, index, action):

    ans_set = set()
    weight = 0

    child_action = "min"
    if action == "include" or cost_include[index] <= cost_exclude[index]:
        ans_set.add(index)
        weight += weights[index]
    else:
        child_action = "include"

    for child in children[index]:
        w, s = calcCost(
            weights, children, cost_include, cost_exclude, child, child_action
        )
        ans_set.update(s)
        weight += w

    return weight, ans_set


def treeVertexCover(
    graph,
    weights,
):
    stack = [0]
    visited = {0}
    children = defaultdict(list)
    cost_include = {}
    cost_exclude = {}

    while len(stack) != 0:
        toSolve = stack[-1]

        # check neighbours
        solvable = True
        for neighbour in graph[toSolve]:
            # is child
            if neighbour not in visited:
                solvable = False
                children[toSolve].append(neighbour)
                stack.append(neighbour)
                visited.add(neighbour)

        if solvable:
            stack.pop()

            c_0 = 0
            c_1 = weights[toSolve]
            for child in children[toSolve]:
                c_0 += cost_include[child]
                c_1 += min(cost_exclude[child], cost_include[child])

            cost_exclude[toSolve] = c_0
            cost_include[toSolve] = c_1

    return calcCost(weights, children, cost_include, cost_exclude, 0, "min")


def main():
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]

    graph, weights = read_graph(file_name1, file_name2)
    checkTree(graph)

    w, s = treeVertexCover(
        graph,
        weights,
    )

    print("Weight:", w)
    print("Vertex Cover Set:", s)


if __name__ == "__main__":
    main()
