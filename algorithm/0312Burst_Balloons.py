class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_len = len(nums)
        indexs = [i for i in range(m_len)]
        memo = dict()

        def helper(indexs):
            if tuple(indexs) in memo:
                return memo[tuple(indexs)]
            m_len = len(indexs)
            totals = 0
            for i in range(m_len):
                pos = indexs[i]
                left = nums[indexs[i-1]] if i != 0 else 1
                right = nums[indexs[i+1]] if i != m_len-1 else 1
                totals = max(left*nums[pos]*right+helper(indexs[:i]+indexs[i+1:]), totals)
            memo[tuple(indexs)] = totals
            return totals
        return helper(indexs)

    def maxCoins2(self, nums):
        new_nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(new_nums)
        if n == 0:
            return 0

        dp = [[0]*n for _ in range(n)]
        for k in range(2, n):
            for left in range(0, n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], dp[left][i]+dp[i][right]+new_nums[left]*new_nums[i]*new_nums[right])
        return dp[0][n-1]

if __name__ == '__main__':
    s = Solution()
    # print(s.maxCoins([3,1,5,8]))
    print(s.maxCoins([3,2]))
