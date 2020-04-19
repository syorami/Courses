# python3

import sys
import threading

def recursive_search(nodes, idx):
    MAX_HEIGHT = float('-inf')
    if len(nodes[idx][0]) == 0: return 1
    for child in nodes[idx][0]:
        height = 1
        height += recursive_search(nodes, child)
        MAX_HEIGHT = max(MAX_HEIGHT, height)
    return MAX_HEIGHT

def compute_height(n, parents):
    nodes = [[[], -1] for _ in parents]
    root_idx = 0
    for i in range(n):
        if parents[i] == -1:
            root_idx = i
        else:
            nodes[parents[i]][0].append(i)
            nodes[i][1] = parents[i]

    height = recursive_search(nodes, root_idx)
    return height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
