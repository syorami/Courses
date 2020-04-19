# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(mins, maxs, nums, ops, start, end):
    MAX = float('-inf')
    MIN = float('inf')
    for k in range(start, end):
        a = evalt(maxs[start][k], maxs[k + 1][end], ops[k])
        b = evalt(maxs[start][k], mins[k + 1][end], ops[k])
        c = evalt(mins[start][k], maxs[k + 1][end], ops[k])
        d = evalt(mins[start][k], mins[k + 1][end], ops[k])
        MIN = min(MIN, min(a, b, c, d))
        MAX = max(MAX, max(a, b, c, d))
    return MIN, MAX


def get_maximum_value(dataset):
    op_num = len(dataset) // 2
    n = len(dataset) - op_num
    nums = [int(num) for num in dataset[::2]]
    ops = [op for op in dataset[1::2]]

    mins = [[0 for _ in range(n)] for _ in range(n)]
    maxs = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        mins[i][i], maxs[i][i] = nums[i], nums[i]

    for stride in range(1, n ):
        for start in range(n - stride):
            end = start + stride
            if stride == 1:
                mins[start][end] = evalt(nums[start], nums[end], ops[start])
                maxs[start][end] = mins[start][end]
            else:
                mins[start][end], maxs[start][end] = min_max(mins, maxs, nums, ops, start, end)

    return maxs[0][-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
