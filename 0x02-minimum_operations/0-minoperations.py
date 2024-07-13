#!/usr/bin/env python3
'''
Minimum operations
'''


def minOperations(n):
    '''
    args:
        - n: number of characters required
    '''
    if n == 1:
        return 0

    dp = {1: 0}  # Base case: 1 H requires 0 operations
    for length in range(2, n + 1):
        min_ops = float('inf')
        for j in range(1, length // 2 + 1):
            if length % j == 0:
                min_ops = min(min_ops, dp[j] + length // j)
        dp[length] = min_ops

    return dp.get(n, 0)
