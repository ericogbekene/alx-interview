#!/usr/bin/python3
"""
working on make change algorithm
"""


def makeChange(coins, total):
    """
    make change function
    """
    # Handle base cases
    if total <= 0:
        return 0

    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill dp array
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
