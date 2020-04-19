# Uses python3
import sys
from math import inf

def get_change(m):
    #write your code here
    minNumCoins = [0] * (m + 1)
    coins = [1, 3, 4]
    for m in range(1, m + 1):
        minNumCoins[m] = inf
        for i in range(len(coins)):
            if m >= coins[i]:
                numCoins = minNumCoins[m - coins[i]] + 1
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins
    return minNumCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 34
    print(get_change(m))
