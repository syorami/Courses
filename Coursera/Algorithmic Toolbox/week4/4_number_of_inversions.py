# Uses python3
import sys

def merge(B, C):
    print(B, C)
    sorted_arr = []
    number_of_inversions = 0
    lenB, lenC = len(B), len(C)
    i, j = 0, 0
    while i != lenB and j != lenC:
        if C[j] < B[i]:
            sorted_arr.append(C[j])
            j += 1
            number_of_inversions += lenB - i
        else:
            sorted_arr.append(B[i])
            i += 1
    if i == lenB: sorted_arr.extend(C[j:])
    if j == lenC: sorted_arr.extend(B[i:])
    return sorted_arr, number_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    sorted_arr, number = merge(a[left:ave], a[ave:right])
    a[left: right] = sorted_arr

    number_of_inversions += number

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    # input = '5\n2 3 9 2 9'
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
