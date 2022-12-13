import sys
from graph import read_graph


def addToSet(c_set, el):
    c_set_new = c_set.copy()
    c_set_new.add(el)
    return c_set_new


def getDegree(
    graph,
    i,
    dropped_set,
):
    deg = len(graph[i])

    for i in graph[i]:
        if i in dropped_set:
            deg -= 1

    return deg


def minWeightVertexCover(graph, weights, curr_weight, curr_set, dropped_set):

    # Solve all degree zero and degree one nodes
    toSolve = set()
    curr_set_up = curr_set.copy()
    dropped_set_up = dropped_set.copy()

    for i in range(len(graph)):
        if i not in dropped_set_up:
            deg = getDegree(
                graph,
                i,
                dropped_set_up,
            )

            if deg == 0:
                dropped_set_up.add(i)

            elif deg == 1:

                for j in graph[i]:
                    if j not in dropped_set_up:
                        neighbour = j
                        break
                deg_n = getDegree(
                    graph,
                    neighbour,
                    dropped_set_up,
                )

                if deg_n == 1:
                    if i not in curr_set_up and neighbour not in curr_set_up:
                        if weights[i] > weights[neighbour]:
                            curr_weight += weights[neighbour]
                            curr_set_up.add(neighbour)
                        else:
                            curr_weight += weights[i]
                            curr_set_up.add(i)

                    dropped_set_up.add(i)
                    dropped_set_up.add(neighbour)

                else:
                    toSolve.add(i)

            else:
                toSolve.add(i)

    # Solve remaining graph
    for i in toSolve:
        if i not in dropped_set_up:

            # node is part of set
            curr_set1 = addToSet(curr_set_up, i)
            curr_weight1 = curr_weight
            if i not in curr_set_up:
                curr_weight1 += weights[i]

            # drop the node
            dropped_set1 = addToSet(dropped_set_up, i)

            w1, s1, d1 = minWeightVertexCover(
                graph,
                weights,
                curr_weight1,
                curr_set1,
                dropped_set1,
            )

            # node is not part of set
            # drop the node
            dropped_set2 = addToSet(dropped_set_up, i)
            curr_set2 = curr_set_up.copy()
            curr_weight2 = curr_weight
            # neighbours are part of set
            # drop all neighbours
            for j in graph[i]:
                if j not in curr_set_up:
                    curr_weight2 += weights[j]
                    curr_set2.add(j)

            w2, s2, d2 = minWeightVertexCover(
                graph, weights, curr_weight2, curr_set2, dropped_set2
            )

            if w1 < w2:
                curr_weight = w1
                curr_set_up = s1
                dropped_set_up = d1
            else:
                curr_weight = w2
                curr_set_up = s2
                dropped_set_up = d2

    return curr_weight, curr_set_up, dropped_set_up


def main():
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]

    graph, weights = read_graph(file_name1, file_name2)

    w, s, _ = minWeightVertexCover(graph, weights, 0, set(), set())

    print("Weight:", w)
    print("Vertex Cover Set:", s)


if __name__ == "__main__":
    main()
