class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        totals = sum(nums)
        if totals & 1:
            return False
        half = totals >> 1
        dp = [0]*(half+1)
        dp[0] = 1

        for num in nums:
            for i in range(half, num-1, -1):
                dp[i] += dp[i-num]
                if i == half and dp[i] > 0:
                    return True
        return False
