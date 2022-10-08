import sys


def getEl(arr, k, i, j):
    if k < 0 or i < 0 or j < 0 or j >= len(arr[0][0]):
        return False

    return arr[k][i][j]


def zerosumgame():

    file_name = sys.argv[1]
    inp = []
    with open(file_name) as data:
        for i in data.readlines():
            inp.append(int(i, 10))

    k_inp = inp[0]
    inp = inp[1:]
    k = len(inp)

    print("Input Set:", inp)
    print("K:", k_inp)

    sumplus = 0
    summinus = 0
    for i in inp:
        if i > 0:
            sumplus += i
        else:
            summinus += i

    arr = [
        [[False for j in range(summinus, sumplus + 1)] for i in range(len(inp))]
        for _ in range(k + 1)
    ]

    for ki in range(k + 1):
        for i in range(len(arr[ki])):

            for j in range(len(arr[ki][i])):

                if ki == 1:
                    if (j - abs(summinus)) == inp[i]:
                        arr[ki][i][j] = {inp[i]}

                else:
                    prevElement = getEl(arr, ki, i - 1, j)

                    incCurrElement = getEl(arr, ki - 1, i - 1, (j) - inp[i])

                    tempset = False
                    if incCurrElement:
                        tempset = incCurrElement.copy()
                        tempset.add(inp[i])

                    arr[ki][i][j] = prevElement or tempset

    ans = False
    for i in range(k_inp, k + 1):
        if arr[i][len(inp) - 1][abs(summinus)]:
            ans = arr[i][len(inp) - 1][abs(summinus)]
            break

    if ans:
        print(True)
        print("Ans:", ans)
    else:
        print(False)


if __name__ == "__main__":
    zerosumgame()
