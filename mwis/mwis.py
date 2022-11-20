import sys


def addToSet(c_set, el):
    c_set2 = c_set.copy()
    c_set2.add(el)
    return c_set2


def getDegree(graph, i, dropped_set):
    deg = len(graph[i])

    for i in graph[i]:
        if i in dropped_set:
            deg -= 1

    return deg


def check_mwis(graph, weights, curr_weight, curr_set, dropped_set):

    # Solve all degree zero and degree one nodes

    toSolve = set()
    curr_set_up = curr_set.copy()
    dropped_set_up = dropped_set.copy()

    for i in range(len(graph)):
        if i not in dropped_set_up:
            deg = getDegree(graph, i, dropped_set_up)

            if deg == 0:
                curr_weight += weights[i]
                curr_set_up.add(i)
                dropped_set_up.add(i)

            elif deg == 1:
                for j in graph[i]:
                    if j not in dropped_set_up:
                        neighbour = j
                        break
                deg_n = getDegree(graph, neighbour, dropped_set_up)

                if deg_n == 1:
                    if weights[i] < weights[neighbour]:
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

            # drop the node
            dropped_set1 = addToSet(dropped_set_up, i)

            # drop all neighbours
            for j in graph[i]:
                dropped_set1.add(j)

            w1, s1, d1 = check_mwis(
                graph,
                weights,
                curr_weight + weights[i],
                curr_set1,
                dropped_set1,
            )

            # node is not part of set
            # drop the node
            dropped_set2 = addToSet(dropped_set_up, i)

            w2, s2, d2 = check_mwis(
                graph, weights, curr_weight, curr_set_up, dropped_set2
            )

            if w1 >= w2:
                curr_weight = w1
                curr_set_up = s1
                dropped_set_up = d1
            else:
                curr_weight = w2
                curr_set_up = s2
                dropped_set_up = d2

    return curr_weight, curr_set_up, dropped_set_up


def mwis():

    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]
    inp = []
    inp2 = []
    with open(file_name1) as data:
        for i in data.readlines():
            inp.append(list(map(int, i.split())))

    with open(file_name2) as data:
        for i in data.readlines():
            inp2.append(int(i, 10))

    weights = inp2[1:]
    graph = []
    for i in inp[1:]:
        graph.append(set(i[1:]))

    w, s, d = check_mwis(
        graph,
        weights,
        0,
        set(),
        set(),
    )

    print("Weight:", w)
    print("Set:", s)


if __name__ == "__main__":
    mwis()
