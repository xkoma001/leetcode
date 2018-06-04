class Solution:
    memo = {}

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount in self.memo:
            return self.memo[amount]

        if amount == 0:
            self.memo[0] = 0
            return 0

        least = -1
        for coin in coins:
            if amount >= coin:
                if amount-coin not in self.memo:
                    cur_kinds = self.coinChange(coins, amount-coin)
                    self.memo[amount-coin] = cur_kinds
                if self.memo[amount-coin] != -1:
                    least = min(self.memo[amount-coin]+1, least) if least != -1 else self.memo[amount-coin]+1
            else:
                pass

        return least

    def coinChange2(self, coins, amount):
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] < amount+1 else -1

if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([2], 1))
