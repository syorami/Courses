# Uses python3
def edit_distance(s, t):
    distance = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        distance[i][0] = i
    for i in range(len(t) + 1):
        distance[0][i] = i

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(distance[i - 1][j], distance[i][j - 1], distance[i - 1][j - 1])
    #write your code here
    return distance[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
