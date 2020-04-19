# Uses python3
import sys

def greedy_solution(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight(weight, w):
    value = [[0 for _ in range(len(w) + 1)] for _ in range(weight + 1)]
    for i in range(1, len(w) + 1):
        for W in range(1, weight + 1):
            value[W][i] = value[W][i - 1] # with i-th item
            if w[i - 1] <= W:
                val = value[W - w[i - 1]][i - 1] + w[i - 1]
                if val > value[W][i]:
                    value[W][i] = val
    return value[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W, n = 10, 3
    # *w, = [3, 5, 3, 3, 5]
    print(optimal_weight(W, w))
