class CoinChange:
    def __init__(self, coins, amount, approach):
        self.coins = coins
        self.amount = amount
        self.approach = approach
        # self.recursion_count = 0
        if self.approach == "dp_bottom_up":
            self.dp = [self.amount+1]*(self.amount+1)
            self.dp[0] = 0
            print(self.dp_bottom_up())
        elif self.approach == "dp_top_down":
            self.memo = {}
            print(self.dp_top_down(self.amount))
        elif self.approach == "recursion":
            print(self.recursion(self.amount))
        elif self.approach == "greedy":
            print(self.greedy())

    def dp_bottom_up(self):
        for i in range(1, self.amount+1):
            for coin in self.coins:
                if i - coin >= 0:
                    self.dp[i] = min(self.dp[i], self.dp[i-coin]+1)
        return self.dp[self.amount] if self.dp[self.amount] != self.amount+1 else -1

    def dp_top_down(self, amount):
        if amount in self.memo:
            return self.memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        min_coins = float('inf')
        for coin in self.coins:
            # print("Call #", self.recursion_count)
            # self.recursion_count += 1
            min_coins = min(min_coins, self.dp_top_down(amount-coin) + 1)
        self.memo[amount] = min_coins
        return min_coins if min_coins != float('inf') else -1

    def recursion(self, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        min_coins = float('inf')
        for coin in self.coins:
            # print("Call #", self.recursion_count)
            # self.recursion_count += 1
            min_coins = min(min_coins, self.recursion(amount-coin) + 1)
        return min_coins if min_coins != float('inf') else -1

    def greedy(self):
        self.coins.sort(reverse=True)
        count = 0
        for coin in self.coins:
            count += self.amount // coin
            self.amount %= coin
        return count if self.amount == 0 else -1