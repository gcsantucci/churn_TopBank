import sys
import numpy as np

def knapsack(W, wt, val):
    n = len(val)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    #Table in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    max_val = K[n][W]
    keep = [False]*n
    res = max_val
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: break
        if res == K[i - 1][w]: continue
        else: 
            keep[i - 1] = True
            res = res - val[i - 1] 
            w = w - wt[i - 1] 
    print(sys.getsizeof(K))
    return max_val, keep
            
if __name__ == '__main__':
    indices = [3, 51, 89]
    val = [60, 100, 120]
    wt = [1, 2, 3]
    W = 5

    indices = [51, 89, 3]
    val = [100, 120, 60]
    wt = [2, 3, 1]
    max_val, keep = knapsack(W, wt, val)
    print(f'max val = {max_val}')
    print(f'keep objects: {keep}')
    indices = np.array(indices)
    print(indices[keep])
