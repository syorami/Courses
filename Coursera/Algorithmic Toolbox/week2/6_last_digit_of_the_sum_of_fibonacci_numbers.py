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

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
