# Uses python3
import sys

def optimal_summands(n):
	summands = []
	i = 1
	while n - i != 0:
		if n - i > i:
			summands.append(i)
			n -= i
			i += 1
		else:
			i = i + 1
	summands.append(i)
	return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
