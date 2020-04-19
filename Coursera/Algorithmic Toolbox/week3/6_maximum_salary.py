#Uses python3

from functools import cmp_to_key

import sys

def resort(a, b):
	if a[0] != b[0]:
		return -(a[0] - b[0])
	else:
		return -(int(a[1] + b[1])) + (int(b[1] + a[1]))

def largest_number(a):
    #write your code here
    res = ""
    first_digit = [int(item[0]) for item in a]
    zip_sort = sorted(zip(first_digit, a), key=cmp_to_key(lambda a, b: resort(a, b)))
    for item in zip_sort:
    	res += item[1]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
