# Uses python3
import sys

def fibonacci_sum_naive(n):

    if n <= 1: return n
    last_digits = [1, 1]
    for i in range(2, min(60, n)):
        last_digits.append((last_digits[i - 1] + last_digits[i - 2]) % 10)
    
    if n <= 60:
        return sum(last_digits) % 10
    else:
        return ((n // 60) * sum(last_digits) + sum(last_digits[:n % 60])) % 10

def fibonacci_partial_sum_naive(from_, to):

	complete = lambda x: x + 10 if x < 0 else x
	return complete(fibonacci_sum_naive(to) - fibonacci_sum_naive(max(0, from_ - 1)))

    # if to <= 1: return to
    # last_digits = [1, 1]
    # for i in range(2, to):
    #     last_digits.append((last_digits[i - 1] + last_digits[i - 2]) % 10)

    # return sum(last_digits[from_ - 1: to + 1]) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))