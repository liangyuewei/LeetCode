class Solution(object):
    def coinChange(self,coins, amount):
        dp = [anount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount):
            for j in range(0, len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]]) + 1
        return dp[amount] if dp[amount] > amount else -1
