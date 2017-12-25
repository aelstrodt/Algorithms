# Given an amount and a list of coins
# figure out the minimum amount of coins
# needed to get amount

# Greedy approach fails because largest
# coin smaller than amount, may or may not
# be part of the optimal solution.

# Recursive approach
# Goes on forever
def recursive_change(amount, coins):
    if amount = 0:
        return 0
    min_coins = 10000
    for coin in coins:
        if amount >= coin:
            num_coins = recursive_change(amount - coin, coins)
            if num_coins + 1 < min_coins:
                min_coins = num_coins + 1
    return min_coins

# Dynamic Programming
# target = 1; coin = 1; sub = 1; dp[target] = 0
def dp_change(amount, coins):
    dp = [100000] * (amount + 1)
    dp[0] = 0
    for target in range(1,amount+1):
        for coin in coins:
            if coin <= target:
                sub = dp[target - coin] + 1
                if sub < dp[target]: dp[target] = sub
    return dp[-1]
    
