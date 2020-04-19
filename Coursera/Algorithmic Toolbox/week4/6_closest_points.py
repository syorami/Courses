#Uses python2
import sys
import random
import time
import math

def cal_dist(point_A, point_B):
    return math.sqrt((point_A[0] - point_B[0]) ** 2 + (point_A[1] - point_B[1]) ** 2)

def brute_search(points):
    length_point = len(points)
    if length_point == 2:
        return cal_dist(points[0], points[1])
    else:
        min_dist = float('inf')
        for i in range(length_point - 1):
            for j in range(i + 1, length_point):
                dist = cal_dist(points[i], points[j])
                if dist < min_dist: min_dist = dist
        return min_dist

def closest_split_pair(x_sorted, d):
    mid_x = x_sorted[len(x_sorted) // 2][0]
    strip_points = [point for point in x_sorted if mid_x - d <= point[0] <= mid_x + d]
    y_sorted = sorted(strip_points, key=lambda x: x[1])

    min_dist = d
    length_y = len(y_sorted)
    for i in range(length_y - 1):
        for j in range(i + 1, min(i + 7, length_y)):
            dst = cal_dist(y_sorted[i], y_sorted[j])
            if dst < min_dist: min_dist = dst
    return min_dist

def minimum_distance(x_sorted):
    length_x = len(x_sorted)
    if length_x <= 3: return brute_search(x_sorted)
    mid = length_x // 2

    d1 = minimum_distance(x_sorted[:mid])
    d2 = minimum_distance(x_sorted[mid:])
    d = min(d1, d2)

    d3 = closest_split_pair(x_sorted, d)

    return min(d, d3)

def get_min_dist(x, y):
    x_sorted = sorted(zip(x, y), key=lambda x: x[0])
    dist = minimum_distance(x_sorted)
    return dist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    # x = [4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2]
    # y = [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]

    print "{0:.9f}".format(get_min_dist(x, y))

