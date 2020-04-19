# Uses python3
import sys

def gcd_naive(a, b):
	bigger = max(a, b)
	smaller = min(a, b)
	while bigger % smaller != 0:
		temp = bigger % smaller
		bigger = smaller
		smaller = temp

	return smaller

def lcm_naive(a, b):
    return a * b // gcd_naive(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

