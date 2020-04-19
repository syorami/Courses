# Uses python3
import sys

def get_pisano_period(m):
    a, b, c = 0, 1, 1
    for i in range(m ** 2):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1: return i + 1
    return 1

def get_fibonacci_huge_naive(n, m):
    remainder = n % get_pisano_period(m)

    first = 0
    second = 1
    res = remainder
    for i in range(1, remainder):
        res = (first + second) % m
        first = second
        second = res

    return res % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
