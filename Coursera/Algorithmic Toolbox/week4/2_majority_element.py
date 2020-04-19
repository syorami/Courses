# Uses python3
import sys

def get_majority_element(a, left, right):
    if right == left: return -1
    if left + 1 == right: return a[left]

    mid = left + (right - left) // 2

    left_element = get_majority_element(a, left, mid)
    right_element = get_majority_element(a, mid, right)

    left_count = a[left: right].count(left_element)
    right_count = a[left: right].count(right_element)

    if left_count > (right - left) // 2:
        return left_element
    elif right_count > (right - left) // 2:
        return right_element
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

    # a = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
    # a = [2, 3, 2, 9, 2, 2]
    # print(get_majority_element(a, 0, 6))
