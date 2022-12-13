def read_graph(file_name1, file_name2):
    # file_name1 = sys.argv[1]
    # file_name2 = sys.argv[2]
    inp = []
    inp2 = []
    with open(file_name1) as data:
        for i in data.readlines():
            inp.append(list(map(int, i.split())))

    popFirst = True
    with open(file_name2) as data:
        for i in data.readlines():
            try:
                inp2.append(int(i, 10))
            except:
                popFirst = False
                inp2 = list(map(int, i.strip().split()))

    weights = inp2
    if popFirst:
        weights = inp2[1:]

    graph = []
    for i in inp[1:]:
        graph.append(set(i[1:]))

    return graph, weights


def read_pd(file_name):
    inp = []
    with open(file_name) as data:
        for i in data.readlines():
            inp.append(set(map(int, i.split())))

    return inp

    