# Uses python3
import sys
import itertools

def two_partition(weight, w):
    value = [[0 for _ in range(len(w) + 1)] for _ in range(weight + 1)]
    for i in range(0, len(w) + 1):
        value[0][i] = 1

    for i in range(1, len(w) + 1):
        for W in range(1, weight + 1):
            value[W][i] = value[W][i - 1] # with i-th item
            if w[i - 1] <= W:
                value[W][i] = value[W][i] | value[W - w[i - 1]][i - 1]
    return value[-1][-1]

def three_partition(a, b, w):
    value = [[[0 for _ in range(len(w) + 1)] for _ in range(b + 1)] for _ in range(a + 1)]
    for i in range(0, len(w) + 1):
        value[0][0][i] = 1

    for i in range(1, len(w) + 1):
        for a_ in range(0, a + 1):
            for b_ in range(0, b + 1):
                value[a_][b_][i] = value[a_][b_][i - 1]
                set_to_a, set_to_b = 0, 0
                if w[i - 1] <= a_:
                    set_to_a = value[a_ - w[i - 1]][b_][i - 1]
                if w[i - 1] <= b_:
                    set_to_b = value[a_][b_ - w[i - 1]][i - 1]
                value[a_][b_][i] = value[a_][b_][i] | set_to_a | set_to_b
    return value[-1][-1][-1]

def partition3(A):
    if sum(A) % 3 == 0 and len(A) >= 3:
        avg_num = sum(A) // 3
        return three_partition(avg_num, avg_num, A)
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    # *A, = [40]
    # *A, = [1, 1, 2, 1, 1]
    # *A, = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
    print(partition3(A))

