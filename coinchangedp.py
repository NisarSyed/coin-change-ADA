

def coinChange(coins, amount: int) -> int:
        dp = [amount+1]*(amount+1)

        dp[0]=0

        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]= min (dp[i], 1 + dp[i-j])

        if dp[amount]== amount+1:
            return -1
        else:
            return dp[amount]