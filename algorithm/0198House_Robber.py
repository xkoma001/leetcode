class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_len = len(nums)
        dp = [0] * m_len
        max_amount = 0

        for i in range(m_len):
            if i >= 3:
                dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            elif i >= 2:
                dp[i] = nums[i] + dp[i-2]
            else:
                dp[i] = nums[i]
            max_amount = max(dp[i], max_amount)
        return max_amount

    def rob2(self, nums):
        a, b = 0, 0
        m_len = len(nums)

        for i in range(m_len):
            if i % 2 == 0:
                a = max(a+nums[i], b)
            else:
                b = max(b+nums[i], a)
        return max(a, b)
