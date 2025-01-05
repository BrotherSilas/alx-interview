#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total
    
    Args:
        coins (list): List of coin values available
        total (int): Target amount to make change for
    
    Returns:
        int: Fewest number of coins needed to meet total, -1 if impossible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for optimization
    coins.sort(reverse=True)

    # Initialize dp array with total + 1 (impossible value)
    # dp[i] represents the minimum coins needed for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build solution for each amount from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
