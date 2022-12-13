import math, sys, itertools
from graph import read_graph, read_pd


def subsets(ss):
    res = []
    for L in range(len(ss) + 1):
        for subset in itertools.combinations(ss, L):
            res.append(frozenset(subset))
    return res


def checkVC(graph, weights, pd, subset):
    all_edges = []
    for node in pd:
        for n in graph[node]:
            if n in pd and n not in subset and node not in subset:
                all_edges.append({node, n})

    if len(all_edges) != 0:
        return math.inf

    w = 0
    for node in subset:
        w += weights[node]

    return w


def pdVertexCover(graph, weights, paths):
    op = []
    cost = []
    history = {}
    for i in range(len(paths)):

        if i == 0 or len(paths[i]) > len(paths[i - 1]):
            curr_op = "INSERT"
            changed_node = list(paths[i].difference(paths[i - 1]))[0]
        else:
            curr_op = "DELETE"
            changed_node = list(paths[i - 1].difference(paths[i]))[0]

        op.append([curr_op, changed_node])

        all_sub = subsets(paths[i])
        d = {}

        if i == 0:
            for ss in all_sub:
                d[ss] = checkVC(graph, weights, paths[i], ss)
                history[ss] = ss

        elif curr_op == "DELETE":
            for ss in all_sub:
                ssUNode = ss.union({changed_node})

                if cost[i - 1][ss] < cost[i - 1][ssUNode]:
                    d[ss] = cost[i - 1][ss]
                else:
                    d[ss] = cost[i - 1][ssUNode]
                    history[ss] = history[ssUNode]

        elif curr_op == "INSERT":
            for ss in all_sub:

                if changed_node in ss:
                    ssDNode = ss.difference({changed_node})
                    d[ss] = cost[i - 1][ssDNode] + weights[changed_node]
                    history[ss] = history[ssDNode].union({changed_node})
                else:
                    d[ss] = checkVC(graph, weights, paths[i], ss)
                    if d[ss] != math.inf:
                        d[ss] = cost[i - 1][ss]

        cost.append(d)

    curr_set, min_weight = min(cost[-1].items(), key=lambda x: x[1])

    return min_weight, set(history[curr_set])


def main():
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]
    path_file_name = sys.argv[3]

    graph, weights = read_graph(file_name1, file_name2)
    paths = read_pd(path_file_name)

    w, s = pdVertexCover(graph, weights, paths)

    print("Weight:", w)
    print("Vertex Cover Set:", s)


if __name__ == "__main__":
    main()
