import sys
import math
from copy import deepcopy
from random import randint

tiles = [
    "0-0",
    "0-1",
    "0-2",
    "0-3",
    "0-4",
    "0-5",
    "0-6",
    "1-1",
    "1-2",
    "1-3",
    "1-4",
    "1-5",
    "1-6",
    "2-2",
    "2-3",
    "2-4",
    "2-5",
    "2-6",
    "3-3",
    "3-4",
    "3-5",
    "3-6",
    "4-4",
    "4-5",
    "4-6",
    "5-5",
    "5-6",
    "6-6",
]


def printMatrix(arr):
    for i in arr:
        for j in i:
            if j is not None:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()


def getChar():
    return chr(randint(65, 122)) + chr(randint(65, 122))


def getPos(arr, i, j, a, b):
    return {
        "tile": str(arr[i][j]) + "-" + str(arr[a][b]),
        "pos_1": [i, j],
        "pos_2": [a, b],
    }


def getPossibleTiles(arr, mat, i, j, usedTiles):
    i_max = len(arr)
    j_max = len(arr[0])
    pos = []

    if mat[i][j] != -1:
        return pos

    if (
        i - 1 >= 0
        and arr[i - 1][j] is not None
        and mat[i - 1][j] == -1
        and (str(arr[i][j]) + "-" + str(arr[i - 1][j])) not in usedTiles
    ):
        pos.append(getPos(arr, i, j, i - 1, j))

    if (
        i + 1 < i_max
        and arr[i + 1][j] is not None
        and mat[i + 1][j] == -1
        and (str(arr[i][j]) + "-" + str(arr[i + 1][j])) not in usedTiles
    ):
        pos.append(getPos(arr, i, j, i + 1, j))

    if (
        j - 1 >= 0
        and arr[i][j - 1] is not None
        and mat[i][j - 1] == -1
        and (str(arr[i][j]) + "-" + str(arr[i][j - 1])) not in usedTiles
    ):
        pos.append(getPos(arr, i, j, i, j - 1))

    if (
        j + 1 < j_max
        and arr[i][j + 1] is not None
        and mat[i][j + 1] == -1
        and (str(arr[i][j]) + "-" + str(arr[i][j + 1])) not in usedTiles
    ):
        pos.append(getPos(arr, i, j, i, j + 1))

    return pos


def solve(floor, mat, usedTiles, tiles):

    can_solve = False
    for pos in tiles:
        mat_up = deepcopy(mat)
        usedTiles_up = deepcopy(usedTiles)
        curr_char = getChar()

        # Place the tile
        mat_up[pos["pos_1"][0]][pos["pos_1"][1]] = curr_char
        mat_up[pos["pos_2"][0]][pos["pos_2"][1]] = curr_char

        # Add placed tile to a used bag to prevent reusing
        usedTiles_up.add(pos["tile"])
        usedTiles_up.add(pos["tile"][::-1])

        sol, mat_new = tileTheFloor(floor, mat_up, usedTiles_up)
        if sol:
            can_solve = True
            break

    return can_solve, mat_new


def tileTheFloor(floor, mat, usedTiles):

    can_solve = True
    min_len = math.inf
    solveij = []
    for i in range(len(floor)):
        for j in range(len(floor[i])):

            if floor[i][j] is not None:
                pos = getPossibleTiles(floor, mat, i, j, usedTiles)

                if len(pos) > 0 and len(pos) < min_len:
                    min_len = len(pos)
                    solveij = pos

                    if min_len == 1:
                        break

        if min_len == 1:
            break

    if min_len == math.inf:
        if len(usedTiles) != 49:
            return False, mat
        else:
            return True, mat

    can_solve, mat = solve(floor, mat, usedTiles, solveij)

    return can_solve, mat


def dominoetiling():
    file_name = sys.argv[1]
    inp = []
    max_l = 0
    with open(file_name) as data:
        for i in data.readlines():
            l = list(i.strip("\n"))
            max_l = max(max_l, len(l))
            inp.append(l)

    ans = deepcopy(inp)

    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] == " ":
                inp[i][j] = None
                ans[i][j] = None
            else:
                inp[i][j] = int(inp[i][j], 10)
                ans[i][j] = -1

        while len(inp[i]) < max_l:
            inp[i].append(None)

    print("Input:")
    printMatrix(inp)
    # printMatrix(ans)

    # Recursively tile the floor to solve input
    a, floor = tileTheFloor(inp, ans, set())
    print("\nSolvable:", a)
    print("\nSolution:")
    # printMatrix(floor)

    n = 65
    d = {}
    # Generate output.txt file
    with open(file_name.split(".")[0] + ".answer.txt", "w+") as data:
        for i in floor:
            for j in i:
                if j is not None:
                    if j not in d:
                        d[j] = chr(n)
                        n += 1
                    data.write(d[j])
                    print(d[j], end=" ")
                else:
                    data.write(" ")
                    print(" ", end=" ")
            data.write("\n")
            print()


if __name__ == "__main__":
    dominoetiling()
