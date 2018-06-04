class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m_len = len(nums)
        dp = [[0] * m_len for _ in range(m_len)]

        totals = 0
        for i in range(m_len):
            for j in range(i, m_len):
                if i == 0:
                    dp[i][j] = nums[j] + dp[i][j-1] if j != i else nums[j]
                else:
                    dp[i][j] = dp[i-1][j] - nums[i-1]
                if dp[i][j] == k:
                    totals += 1
        return totals

    def subarraySum2(self, nums, k):
        from collections import defaultdict
        hash_nums = defaultdict(int)

        cur_sum = 0
        totals = 0
        hash_nums[0] = 1
        for num in nums:
            cur_sum += num
            if cur_sum-k in hash_nums:
                totals += hash_nums[cur_sum-k]
            hash_nums[cur_sum] += 1
        return totals


