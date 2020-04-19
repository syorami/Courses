# Uses python3
import sys
import time
from math import inf

def optimal_sequence(n):
    opt_sequence = [[0], [1]]
    minNumOperations = [0] * (n + 1)
    mul_two = lambda x: x / 2
    mul_three = lambda x: x / 3
    add_one = lambda x: x - 1
    operations = [mul_three, mul_two, add_one]
    for m in range(2, n + 1):
        minNumOperations[m] = inf
        tmp1, tmp2, tmp3 = inf, inf, inf
        if m % 3 == 0: tmp1 = minNumOperations[int(operations[0](m))] + 1
        if m % 2 == 0: tmp2 = minNumOperations[int(operations[1](m))] + 1
        tmp3 = minNumOperations[m - 1] + 1

        numOperations = min(tmp1, tmp2, tmp3)
        minNumOperations[m] = numOperations

        if numOperations == tmp1:
            opt_sequence.append(opt_sequence[int(operations[0](m))] + [m])
            continue
        if numOperations == tmp2:
            opt_sequence.append(opt_sequence[int(operations[1](m))] + [m])
            continue
        if numOperations == tmp3:
            opt_sequence.append(opt_sequence[int(operations[2](m))] + [m])

    return opt_sequence[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n = 1
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
