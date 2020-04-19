# python3

import sys

def getParent(table):
    # find parent and compress path
    start_node = table
    while parent[start_node] != start_node:
        start_node = parent[start_node]
    parent[table] = start_node
    return start_node

def merge(destination, source, ans):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return ans

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    if rank[realDestination] < rank[realSource]:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
    else:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        if rank[realDestination] == rank[realSource]:
            rank[realDestination] += 1

    ans = max(lines[realDestination], lines[realSource], ans)
    
    return ans

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))

    # n, m = 5, 5
    # lines = [1, 1, 1, 1, 1]
    # destinations = [3, 2, 1, 5, 5]
    # sources = [5, 4, 4, 4, 3]

    rank = [1] * n
    parent = list(range(0, n))
    ans = max(lines)


    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        ans = merge(destination - 1, source - 1, ans)
        # ans = merge(destinations[i] - 1, sources[i] - 1, ans)
        print(ans)
    
