import sys
from graph import read_graph

NOT_FOUND = [False, 0, set()]


def addToSet(c_set, el):
    c_set_new = c_set.copy()
    c_set_new.add(el)
    return c_set_new


def bstVertexCover(graph, weights, k, dropped_set):
    if k < 0:
        return NOT_FOUND

    edge = None
    for i in range(len(graph)):
        if i not in dropped_set:
            for j in graph[i]:
                if j not in dropped_set:
                    edge = [i, j]
                    break
        if edge is not None:
            break

    if edge is None:
        return True, 0, set()

    ans1, weight1, set1 = bstVertexCover(
        graph, weights, k - 1, addToSet(dropped_set, edge[0])
    )

    ans2, weight2, set2 = bstVertexCover(
        graph, weights, k - 1, addToSet(dropped_set, edge[1])
    )

    if ans1 and ans2:
        if weight1 + weights[edge[0]] > weight2 + weights[edge[1]]:
            return ans2, weight2 + weights[edge[1]], addToSet(set2, edge[1])
        else:
            return ans1, weight1 + weights[edge[0]], addToSet(set1, edge[0])
    elif ans1:
        return ans1, weight1 + weights[edge[0]], addToSet(set1, edge[0])
    elif ans2:
        return ans2, weight2 + weights[edge[1]], addToSet(set2, edge[1])
    return NOT_FOUND


def main():
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]
    k = int(sys.argv[3])

    graph, weights = read_graph(file_name1, file_name2)

    answer, w, s = bstVertexCover(graph, weights, k, set())
    if answer:
        print("Weight:", w)
        print("Vertex Cover Set:", s)
    else:
        print("No vertex cover of size", k)


if __name__ == "__main__":
    main()
