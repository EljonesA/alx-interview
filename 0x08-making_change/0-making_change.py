#!/usr/bin/python3
""" Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    '''coins is a list of the values of the coins in your possession
    '''
    if total <= 0:
        return 0

    # initialize the dp array
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Build up the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # check if we found a solution
    return dp[total] if dp[total] != total + 1 else -1
