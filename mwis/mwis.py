def addToSet(c_set, el):
    c_set2 = c_set.copy()
    c_set.add(el)
    return c_set2


def check_mwis(memo, graph, weights, i, curr_weight, curr_set, dropped_set):
    # print("ICALL", i)
    # print("curr_set", curr_set)
    # print("dropped_set", dropped_set)

    # key = str(sorted(curr_set))
    key = i
    if key in memo:
        # print("returing memo for i:", i)
        return memo[key]["w"], memo[key]["s"]

    if i >= len(weights):
        return curr_weight, curr_set

    w1 = 0
    s1 = set()
    if i not in dropped_set:

        neighbours = graph[i]
        n_len = len(neighbours)
        if n_len == 0:
            curr_set1 = curr_set.copy()
            curr_set1.add(i)

            max_w = curr_weight + weights[i]
            max_set = addToSet(curr_set, i)
            memo[i] = {"w": max_w, "s": max_set}

            return max_w, max_set

        elif n_len == 1:
            n = neighbours[0]
            if len(graph[n]) == 1:
                if weights[i] >= weights[n]:

                    max_w = curr_weight + weights[i]
                    max_set = addToSet(curr_set, i)
                    memo[i] = {"w": max_w, "s": max_set}
                    memo[n] = {"w": max_w, "s": max_set}

                    return max_w, max_set
                else:
                    max_w = curr_weight + weights[n]
                    max_set = addToSet(curr_set, n)
                    memo[i] = {"w": max_w, "s": max_set}
                    memo[n] = {"w": max_w, "s": max_set}

                    return max_w, max_set

            else:

                w, s = check_mwis(
                    memo,
                    graph,
                    weights,
                    n,
                    curr_weight,
                    curr_set,
                    addToSet(dropped_set, i),
                )
                if n not in s:
                    return curr_weight + weights[i], addToSet(curr_set, i)
                else:
                    return w, s

        # node is part of set
        curr_set1 = curr_set.copy()
        curr_set1.add(i)
        # drop the node
        dropped_set1 = dropped_set.copy()
        dropped_set1.add(i)
        # drop all neighbours
        for j in graph[i]:
            dropped_set1.add(j)

        w1, s1 = check_mwis(
            memo,
            graph,
            weights,
            i + 1,
            curr_weight + weights[i],
            curr_set1,
            dropped_set1,
        )

    # node is not part of set
    # drop the node
    dropped_set2 = dropped_set.copy()
    dropped_set2.add(i)
    w2, s2 = check_mwis(
        memo, graph, weights, i + 1, curr_weight, curr_set, dropped_set2
    )

    # print("w1", w1)
    # print("s1", s1)
    # print("w2", w2)
    # print("s2", s2)

    # print()

    if w1 >= w2:
        max_w = w1
        max_set = s1
        curr_set_key = curr_set1
    else:
        max_w = w2
        max_set = s2
        curr_set_key = curr_set

    # memo[str(sorted(curr_set_key))] = {"w": max_w, "s": max_set}

    return max_w, max_set


def mwis():

    # n = 3
    graph = [
        {2, 3},
        {2, 3},
        {0, 1},
        {0, 1},
    ]
    graph1 = [
        {0, 3},
        {1, 9},
        {2, 6, 7, 8},
        {3, 0, 4},
        {4, 3, 5},
        {5, 4, 6, 7},
        {6, 2, 5},
        {7, 2, 5},
        {8, 2, 10},
        {9, 1, 10},
        {10, 8, 9},
    ]
    graph = [
        {0, 3, 4, 8, 11, 12},
        {1, 2},
        {2, 1, 3, 4, 5},
        {3, 0, 2},
        {4, 0, 2},
        {5, 2, 28, 29},
        {6, 13, 28, 29},
        {7, 9, 10, 11, 12, 17, 18, 19},
        {8, 0, 9, 10},
        {9, 7, 8},
        {10, 7, 8},
        {11, 0, 7},
        {12, 0, 7},
        {13, 6, 26, 27},
        {14, 25, 26, 27},
        {15, 22, 23, 24, 25},
        {16, 17, 18, 19, 20},
        {17, 7, 16},
        {18, 7, 16},
        {19, 7, 16},
        {20, 16, 21, 24},
        {21, 20, 22, 23},
        {22, 15, 21},
        {23, 15, 21},
        {24, 15, 20},
        {25, 14, 15},
        {26, 13, 14},
        {27, 13, 14},
        {28, 5, 6},
        {29, 5, 6},
    ]
    graph1 = [
        {0, 3, 6, 32, 33, 34, 35},
        {1, 2},
        {2, 1, 3, 4},
        {3, 0, 2},
        {4, 2, 5, 33, 34, 35},
        {5, 4, 7, 8, 30, 32},
        {6, 0, 7, 8, 9},
        {7, 5, 6},
        {8, 5, 6},
        {9, 6, 12},
        {10, 11, 26, 27, 28, 29},
        {11, 10, 15, 17},
        {12, 9, 13},
        {13, 12, 14},
        {14, 13, 15, 16},
        {15, 11, 14},
        {16, 14, 20, 21},
        {17, 11, 22},
        {18, 19, 23, 24},
        {19, 18, 20, 21},
        {20, 16, 19},
        {21, 16, 19},
        {22, 17, 23, 24},
        {23, 18, 22},
        {24, 18, 22},
        {25, 26, 27, 28, 29, 31},
        {26, 10, 25},
        {27, 10, 25},
        {28, 10, 25},
        {29, 10, 25},
        {30, 5, 31},
        {31, 25, 30},
        {32, 0, 5},
        {33, 0, 4},
        {34, 0, 4},
        {35, 0, 4},
    ]
    weights = [
        898,
        803,
        766,
        993,
    ]
    weights1 = [
        898,
        803,
        766,
        993,
        2,
        522,
        221,
        381,
        730,
        970,
        185,
    ]
    weights = [
        898,
        803,
        766,
        993,
        2,
        522,
        221,
        381,
        730,
        970,
        185,
        888,
        105,
        642,
        910,
        379,
        725,
        583,
        388,
        584,
        242,
        295,
        160,
        199,
        654,
        370,
        419,
        693,
        37,
        902,
    ]
    weights1 = [
        898,
        803,
        766,
        993,
        2,
        522,
        221,
        381,
        730,
        970,
        185,
        888,
        105,
        642,
        910,
        379,
        725,
        583,
        388,
        584,
        242,
        295,
        160,
        199,
        654,
        370,
        419,
        693,
        37,
        902,
        517,
        624,
        704,
        972,
        305,
        395,
    ]

    w1, s1 = check_mwis(
        {},
        graph,
        weights,
        0,
        0,
        set(),
        set(),
    )

    print("final")
    print(w1, s1)


if __name__ == "__main__":
    mwis()
