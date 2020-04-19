#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    lcs = [[[0 for _ in range(len(c) + 1)] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                    lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
                else:
                    lcs[i][j][k] = max(lcs[i - 1][j][k], lcs[i][j - 1][k], lcs[i][j][k - 1])

    return lcs[-1][-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    # a = [8, 3, 2, 1, 7]
    # b = [8, 2, 1, 3, 8, 10, 7]
    # c = [6, 8, 3, 1, 4, 7]
    print(lcs3(a, b, c))
