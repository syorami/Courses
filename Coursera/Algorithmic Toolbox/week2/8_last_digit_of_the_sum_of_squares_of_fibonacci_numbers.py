# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1: return n
    last_digits = [1, 1]
    for i in range(2, min(60, n)):
        last_digits.append((last_digits[i - 1] + last_digits[i - 2]) % 10)
    
    if n <= 60:
        return sum([digit ** 2 % 10 for digit in last_digits]) % 10
    else:
        return ((n // 60) * sum([digit ** 2 % 10 for digit in last_digits]) + \
            sum([digit ** 2 % 10 for digit in last_digits[:n % 60]])) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
