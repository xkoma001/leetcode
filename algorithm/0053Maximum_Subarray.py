class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        m = len(nums)
        dp = [0]*m

        dp[0], max_sum = nums[0], nums[0]
        for i in range(1, m):
            dp[i] = dp[i-1]+nums[i] if dp[i-1] > 0 else nums[i]
            max_sum = dp[i] if dp[i] > max_sum else max_sum
        return max_sum

