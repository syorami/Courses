# Uses python3
import sys
import random
from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    start_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    point_points = zip(points, ['p'] * len(points), range(len(points)))

    sort_list = chain(start_points, end_points, point_points)
    sort_list = sorted(sort_list, key=lambda a: (a[0], a[1]))
    segment = 0
    i = 0
    for num, letter, index in sort_list:
        if letter == 'l':
            segment += 1
        elif letter == 'r':
            segment -= 1
        else:
            cnt[index] = segment
            i += 1
    return cnt

def partition3(a, l, r):
    num = 1
    j = l + 1
    for i in range(l + 1, r + 1):
        if a[i][0] == a[l][0]:
            a[i], a[j] = a[j], a[i]
            j += 1
            num += 1
    m2 = partition2(a, l + num - 1, r)
    for i in range(1, num):
        a[m2 - i], a[l + i - 1] = a[l + i - 1], a[m2 - i]
    m1 = m2 - num + 1
    return m1, m2

def partition2(a, l, r):
    x = a[l][0]
    j = l
    for i in range(l + 1, r + 1):
        if a[i][0] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

def fast_count_segments_slow(starts, ends, points):
    cnt = [0] * len(points)

    start_pairs = [(starts[i], 'l', i) for i in range(len(starts))]
    end_pairs = [(ends[i], 'r', i) for i in range(len(ends))]
    point_pairs = [(points[i], 'point', i) for i in range(len(points))]

    sort_list = chain(start_pairs, end_pairs, point_pairs)
    sort_list = sorted(sort_list, key=lambda a: (a[0], a[1]))

    count = 0
    for pair in sort_list:
        if pair[1] == 'l': count += 1
        if pair[1] == 'r': count -= 1
        # arr.index() causes linear search time
        if pair[1] == 'point': cnt[pair[2]] = count

    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    # starts = [0, -3, 7]
    # ends = [5, 2, 10]
    # points = [1, 6]

    cnt = fast_count_segments_slow(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
