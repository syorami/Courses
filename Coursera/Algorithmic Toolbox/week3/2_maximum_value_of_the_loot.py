# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    sort_weight_val = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    for item in sort_weight_val:
    	if capacity == 0: return value
    	weight, val = item[0], item[1]
    	value += val * min(capacity, weight) / weight
    	capacity -= min(capacity, weight)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
