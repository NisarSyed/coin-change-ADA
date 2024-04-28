def coinchangeaux(n, coins, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n < 0:
        return float('inf')
    mincoins = float('inf')
    for coin in coins:
        mincoins = min(mincoins, coinchangeaux(n-coin, coins, memo) + 1)
    memo[n] = mincoins
    return mincoins

def coinChange(coins, amount: int) -> int:
    memo = {}
    return coinchangeaux(amount, coins, memo) if coinchangeaux(amount, coins, memo) != float('inf') else -1